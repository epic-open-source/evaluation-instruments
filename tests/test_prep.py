import json
from collections import namedtuple
from unittest.mock import mock_open, patch

import pytest

import evaluation_instruments.prep as undertest


class TestJsonFromColumnDecorator:
    """Tests for the json_from_column decorator functionality."""

    def test_basic_functionality(self):
        """Test basic json_from_column decorator functionality."""

        # Create a test function to decorate
        @undertest.json_from_column(namedtuple_key="file_id")
        def test_fn(json_data):
            return json_data

        # Create a mock sample with file_id
        Sample = namedtuple("Sample", ["file_id"])
        sample = Sample(file_id="test_id")

        # Mock the open function to return a specific JSON
        test_json = {"key": "value"}
        m = mock_open(read_data=json.dumps(test_json))

        with patch("builtins.open", m), patch("os.path.isfile", return_value=True):
            result = test_fn(sample)
            assert result == test_json
            m.assert_called_once_with("test_id.json", "r")

    def test_with_data_path(self):
        """Test json_from_column with a data_path."""

        # Create a test function with data path
        @undertest.json_from_column(namedtuple_key="file_id", data_path="/data")
        def test_fn(json_data):
            return json_data

        # Create a mock sample
        Sample = namedtuple("Sample", ["file_id"])
        sample = Sample(file_id="test_id")

        # Mock the open function
        test_json = {"key": "value"}
        m = mock_open(read_data=json.dumps(test_json))

        with patch("builtins.open", m), patch("os.path.isfile", return_value=True), patch(
            "os.path.join", return_value="/data/test_id.json"
        ):
            result = test_fn(sample)
            assert result == test_json
            m.assert_called_once_with("/data/test_id.json", "r")

    def test_file_not_found(self):
        """Test json_from_column when the file is not found."""

        @undertest.json_from_column(namedtuple_key="file_id")
        def test_fn(json_data):
            return json_data

        Sample = namedtuple("Sample", ["file_id"])
        sample = Sample(file_id="nonexistent_id")

        with patch("os.path.isfile", return_value=False):
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
