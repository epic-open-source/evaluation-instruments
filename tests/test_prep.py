import json
from collections import namedtuple
from unittest.mock import mock_open, patch
from pathlib import PureWindowsPath, PurePosixPath

import pytest

import evaluation_instruments.prep as undertest


class TestJsonFromColumnDecorator:
    """Tests for the json_from_column decorator functionality."""

    @pytest.mark.parametrize("data_path",[
                             "data",
                             "subdir/data",
                             "subdir\\data",
                             PurePosixPath("subdir/data"),
                             PureWindowsPath("subdir\\data"),
                              ])
    def test_with_data_path(self, data_path, tmp_path):
        """Test json_from_column with a data_path."""
        expected_data = {"testkey": "value"}
        expected_file = (tmp_path / data_path).with_suffix(".json")
        (expected_file.parent).mkdir(parents=True, exist_ok=True)
        with expected_file.open("w") as f:
            f.write(json.dumps(expected_data))

        # Create a mock sample
        Sample = namedtuple("Sample", ["file_id"])
        sample = Sample(file_id=data_path)


        # Act
        # Create a test function with data path
        @undertest.json_from_column(namedtuple_key="file_id", data_path=tmp_path)
        def test_fn(json_data):
            return json_data
        result = test_fn(sample)

        # Assert
        assert result == {"testkey": "value"}

    def test_file_not_found(self):
        """Test json_from_column when the file is not found."""

        @undertest.json_from_column(namedtuple_key="file_id", data_path="nonexistent_path")
        def test_fn(json_data):
            return json_data

        Sample = namedtuple("Sample", ["file_id"])
        sample = Sample(file_id="nonexistent_id")

        result = test_fn(sample)
        assert result == {}

    def test_missing_key(self):
        """Test json_from_column raises ValueError if namedtuple_key is not provided."""
        with pytest.raises(ValueError, match="namedtuple_key must be provided"):

            @undertest.json_from_column()
            def test_fn(json_data):
                return json_data


class TestToUserMessagesDecorator:
    """Tests for the to_user_messages decorator functionality."""

    def test_without_system(self):
        """Test to_user_messages decorator without system message."""

        @undertest.to_user_messages
        def test_prompt_fn():
            return "Test user prompt"

        result = test_prompt_fn()

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] == {"role": "user", "content": "Test user prompt"}

    def test_with_system(self):
        """Test to_user_messages decorator with system message."""

        @undertest.to_user_messages(system_message="System instructions")
        def test_prompt_fn():
            return "Test user prompt"

        result = test_prompt_fn()

        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0] == {"role": "system", "content": "System instructions"}
        assert result[1] == {"role": "user", "content": "Test user prompt"}

    def test_with_arguments(self):
        """Test to_user_messages decorator with function that takes arguments."""

        @undertest.to_user_messages
        def test_prompt_fn(arg1, arg2=None):
            return f"Prompt with {arg1} and {arg2}"

        result = test_prompt_fn("value1", arg2="value2")

        assert len(result) == 1
        assert result[0] == {"role": "user", "content": "Prompt with value1 and value2"}


class TestPromptCompilation:
    """Tests for the prompt_compilation function."""

    def test_prompt_compilation_with_rubric_set(self):
        """Test prompt compilation with RUBRIC_SET placeholder."""
        prompt_pattern = "Here is the {task} with {variable}. {RUBRIC_SET}"
        pattern_kwargs = {"task": "evaluation", "variable": "context"}
        rubric_library = {"rubric1": "Evaluate clarity.", "rubric2": "Evaluate accuracy."}

        result = undertest.prompt_compilation(prompt_pattern, pattern_kwargs, rubric_library)

        assert "Here is the evaluation with context." in result
        assert "Evaluate clarity." in result
        assert "Evaluate accuracy." in result

    def test_prompt_compilation_with_no_rubric_set(self):
        """Test prompt compilation without RUBRIC_SET placeholder."""
        prompt_pattern = "Here is the {task} with {variable}."
        pattern_kwargs = {"task": "evaluation", "variable": "context"}
        rubric_library = {"rubric1": "Evaluate clarity.", "rubric2": "Evaluate accuracy."}

        result = undertest.prompt_compilation(prompt_pattern, pattern_kwargs, rubric_library)

        assert "Here is the evaluation with context." in result
        assert "Evaluate clarity." not in result
        assert "Evaluate accuracy." not in result

    @pytest.mark.parametrize(
        "rubric_keys,expected_rubrics",
        [
            (["rubric1"], ["Evaluate clarity."]),
            (["rubric2"], ["Evaluate accuracy."]),
            (["rubric1", "rubric2"], ["Evaluate clarity.", "Evaluate accuracy."]),
            (["rubric2", "rubric1"], ["Evaluate accuracy.", "Evaluate clarity."]),
        ],
    )
    def test_prompt_compilation_with_rubric_set_and_keys(self, rubric_keys, expected_rubrics):
        """Test prompt compilation with RUBRIC_SET placeholder and specific keys."""
        prompt_pattern = "Here is the {task} with {variable}. {RUBRIC_SET}"
        pattern_kwargs = {"task": "evaluation", "variable": "context"}
        rubric_library = {"rubric1": "Evaluate clarity.", "rubric2": "Evaluate accuracy."}

        result = undertest.prompt_compilation(prompt_pattern, pattern_kwargs, rubric_library, rubric_keys)

        assert "Here is the evaluation with context." in result
        for expected in expected_rubrics:
            assert expected in result

    def test_prompt_compilation_with_unknown_key_logs(self, caplog):
        """Test prompt compilation with RUBRIC_SET placeholder and missing keys."""
        prompt_pattern = "Here is the {task} with {variable}. {RUBRIC_SET}"
        pattern_kwargs = {"task": "evaluation", "variable": "context"}
        rubric_library = {"rubric1": "Evaluate clarity.", "rubric2": "Evaluate accuracy."}
        rubric_keys = ["rubric1", "nonexistent"]

        with caplog.at_level(10, logger="evaluation"):
            result = undertest.prompt_compilation(prompt_pattern, pattern_kwargs, rubric_library, rubric_keys)

        # Missing key is logged
        assert "Requested rubric" in caplog.text

        # Continues with good keys
        assert "Here is the evaluation with context." in result
        assert "Evaluate clarity." in result


class TestResolveInstructions:
    def test_resolve_score_is_base(self):
        instructions = ["First instruction.", "Second instruction."]
        overrides = {0: "Updated first instruction.",
                     1: "Updated second instruction."}
        expected = "\n".join(instructions)


        actual = undertest.resolve_instructions(instructions, overrides, default_mode='score_only')

        assert actual == expected


    @pytest.mark.parametrize('overrides,expected', [
        ({}, "\n".join(["First instruction.", "Second instruction."])),
        ({0: "Updated first instruction."}, "Updated first instruction.\nSecond instruction."),
        ({1: "Updated second instruction."}, "First instruction.\nUpdated second instruction."),
        ({0: "Updated first instruction.", 1: "Updated second instruction."}, "Updated first instruction.\nUpdated second instruction.")
    ])
    def test_resolve_explanation_is_merged(self, overrides, expected):
        instructions = ["First instruction.", "Second instruction."]

        actual = undertest.resolve_instructions(instructions, overrides, default_mode='with_explanation')

        assert actual == expected


@pytest.mark.parametrize('default',[
    ('score_only'), (undertest.OutputMode.SCORE),
    ('with_explanation'), (undertest.OutputMode.EXPLAINED_SCORE),
    ('default'), (undertest.OutputMode.DEFAULT)
])
class Test_ResolveMode:
    @pytest.mark.parametrize('mode,expected', [
        ('score_only', undertest.OutputMode.SCORE),
        (undertest.OutputMode.SCORE, undertest.OutputMode.SCORE),
        ('with_explanation', undertest.OutputMode.EXPLAINED_SCORE),
        (undertest.OutputMode.EXPLAINED_SCORE, undertest.OutputMode.EXPLAINED_SCORE),
    ])
    def test_explicit_mode_is_choosen(self, mode, expected, default):
        """Test that explicit mode is chosen over default."""
        assert expected == undertest.data_handler._resolve_mode(mode, default)

    def test_default_mode_used_when_string(self, default):
        assert undertest.OutputMode(default) == undertest.data_handler._resolve_mode('default', default)

    def test_default_mode_used_when_enum(self, default):
        assert undertest.OutputMode(default) == undertest.data_handler._resolve_mode(undertest.OutputMode.DEFAULT, default)
