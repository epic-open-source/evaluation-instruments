import json
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from evaluation_instruments._evaluation import Evaluation
from evaluation_instruments.model import TokenUsage

def example_dict():
    return {
            "choices": [{"message": {"content": json.dumps({"result": "success"})}}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        }

class CompletionObj:
    def __init__(self, response_dict):
        self.response_dict = response_dict

    def dict(self):
        return self.response_dict

    def json(self):
        return json.dumps(self.response_dict)

@pytest.fixture
def sample_evaluation_obj():
    """
    Create a basic evaluation instance with mock functions
    Returns an object with a dict method, like Openai
    """
    prep_fn = MagicMock(return_value="test prompt")
    completion_fn = MagicMock(
        return_value=CompletionObj(example_dict())
    )
    post_fn = MagicMock(
        return_value=({"result": "success"}, {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15})
    )

    return Evaluation(
        prep_fn=prep_fn,
        completion_fn=completion_fn,
        post_process_fn=post_fn,
        log_enabled=False,
        model_args={},
        max_tokens=1000,
    )

@pytest.fixture
def sample_evaluation():
    """
    Create a basic evaluation instance with mock functions.
    Directly returns a dictionary
    """
    prep_fn = MagicMock(return_value="test prompt")
    completion_fn = MagicMock(
        return_value=example_dict()
    )
    post_fn = MagicMock(
        return_value=({"result": "success"}, {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15})
    )

    return Evaluation(
        prep_fn=prep_fn,
        completion_fn=completion_fn,
        post_process_fn=post_fn,
        log_enabled=False,
        model_args={},
        max_tokens=1000,
    )


def static_completion(prompt, **kwargs):
    """Fake completion function to simulate OpenAI API response."""
    return example_dict()


def static_prep(sample):
    """Static preparation function to simulate prompt generation."""
    return "test prompt"


def fake_post_override(response):
    """Static post-processing function to simulate response handling."""
    if isinstance(response, dict) and "choices" in response:
        content = response["choices"][0]["message"]["content"]
        return json.loads(content), response["usage"]
    else:
        return {}, {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}


class TestEvaluation:
    def test_evaluation_initialization(self):
        """Test that Evaluation class initializes correctly with default and custom parameters."""
        # Test with defaults
        eval_default = Evaluation()
        assert eval_default._prep_fn is None
        assert eval_default._completion_fn is None
        assert eval_default._post_fn == eval_default.post_process_default
        assert eval_default._log_enabled is True
        assert eval_default._model_args == {}
        assert eval_default.capacity.total_tokens == 10_000

    def test_evaluation_constructor_maps_as_expected(self):
        eval_custom = Evaluation(
            prep_fn=static_prep,
            completion_fn=static_completion,
            post_process_fn=fake_post_override,
            log_enabled=False,
            model_args={"temperature": 0.7},
            max_tokens=5000,
        )

        assert eval_custom._prep_fn is static_prep
        assert eval_custom._completion_fn is static_completion
        assert eval_custom._post_fn is fake_post_override
        assert eval_custom._log_enabled is False
        assert eval_custom._model_args == {"temperature": 0.7}
        assert eval_custom.capacity.total_tokens == 5000

    @pytest.mark.parametrize(
        "attr_name, attr_value",
        [("prep_fn", static_prep), ("completion_fn", static_completion), ("post_fn", fake_post_override)],
    )
    def test_property_setters(self, attr_name, attr_value, sample_evaluation):
        """Test property setters for Evaluation class using parametrization."""
        # Set the property using setattr
        setattr(sample_evaluation, attr_name, attr_value)

        # Check that the internal attribute was updated correctly
        internal_attr_name = f"_{attr_name}"
        assert getattr(sample_evaluation, internal_attr_name) is attr_value

    @pytest.mark.parametrize("initial_state", [True, False])
    def test_toggle_logging(self, initial_state, sample_evaluation):
        """Test that toggle_logging method works correctly."""
        sample_evaluation.log_enabled = initial_state
        assert sample_evaluation.log_enabled == initial_state

        sample_evaluation.toggle_logging()
        result = sample_evaluation.log_enabled
        assert result == (not initial_state)

    def test_run_dataset(self, sample_evaluation):
        """Test that run_object returns the expected output."""
        # Create a mock DataFrame
        df = pd.DataFrame({"id": [1, 2], "data": ["test1", "test2"]})

        # Run the dataset
        outputs, usage = sample_evaluation.run_dataset(df)

        # Check that prep_fn, completion_fn, and post_fn were called for each sample
        assert sample_evaluation._prep_fn.call_count == 2
        assert sample_evaluation._completion_fn.call_count == 2
        assert sample_evaluation._post_fn.call_count == 2

        # Check outputs and usage
        assert len(outputs) == 2
        assert all(v == {"result": "success"} for v in outputs.values())
        assert usage == TokenUsage(20, 10, 30)

    def test_run_dataset(self, sample_evaluation_obj):
        """Test that run_object returns the expected output."""
        # Create a mock DataFrame
        df = pd.DataFrame({"id": [1, 2], "data": ["test1", "test2"]})

        # Run the dataset
        outputs, usage = sample_evaluation_obj.run_dataset(df)

        # Check that prep_fn, completion_fn, and post_fn were called for each sample
        assert sample_evaluation_obj._prep_fn.call_count == 2
        assert sample_evaluation_obj._completion_fn.call_count == 2
        assert sample_evaluation_obj._post_fn.call_count == 2

        # Check outputs and usage
        assert len(outputs) == 2
        assert all(v == {"result": "success"} for v in outputs.values())
        assert usage == TokenUsage(20, 10, 30)

    def test_run_dataset_empty(self, sample_evaluation, caplog):
        """Test the run_dataset method processes samples correctly."""

        with caplog.at_level(30, logger="evaluation"):
            outputs, usage = sample_evaluation.run_dataset(pd.DataFrame(columns=["id", "data"]))

        assert outputs == {}
        assert usage == TokenUsage(0, 0, 0)
        assert "Empty DataFrame" in caplog.text

    def test_capacity_limit(self, sample_evaluation):
        """Test that run_dataset stops when capacity is reached."""
        # Create a mock DataFrame with many samples
        df = pd.DataFrame({"id": list(range(100)), "data": ["test"] * 100})
        # Set a low capacity
        sample_evaluation.capacity = TokenUsage(None, None, 15)

        # Run the dataset
        outputs, usage = sample_evaluation.run_dataset(df)

        # Should stop after processing just 2 sample (15 is exact so continues)
        assert len(outputs) == 2
        assert usage.total_tokens == 30

    def test_adhoc_capacity_limit(self, sample_evaluation):
        """Test that run_dataset stops when capacity is reached."""
        # Create a mock DataFrame with many samples
        df = pd.DataFrame({"id": list(range(100)), "data": ["test"] * 100})
        # Set a low capacity
        sample_evaluation.capacity = TokenUsage(None, None, 15)

        # Run the dataset
        outputs, usage = sample_evaluation.run_dataset(df, capacity=35)

        # Should stop after processing just 2 sample (15 is exact so continues)
        assert len(outputs) == 3
        assert usage.total_tokens == 45

    @pytest.mark.parametrize(
        "prop_name, expected_attr",
        [
            ("prep_fn", "_prep_fn"),
            ("completion_fn", "_completion_fn"),
            ("post_fn", "_post_fn"),
            ("log_enabled", "_log_enabled"),
        ],
    )
    def test_property_getters(self, sample_evaluation, prop_name, expected_attr):
        """Test that properties return the correct values."""
        assert getattr(sample_evaluation, prop_name) == getattr(sample_evaluation, expected_attr)

    def test_model_args_property(self):
        """Test setting and getting model_args property."""
        new_model_args = {"temperature": 0.5, "max_tokens": 200}

        eval = Evaluation(model_args=new_model_args)

        assert eval._model_args == new_model_args

    def test_log_enabled_property(self, sample_evaluation):
        """Test setting and getting log_enabled property."""
        initial_state = sample_evaluation.log_enabled
        sample_evaluation.log_enabled = not initial_state
        assert sample_evaluation._log_enabled == (not initial_state)

    def test_capacity_property(self, sample_evaluation):
        """Test setting and getting capacity property."""
        new_capacity = TokenUsage(prompt_tokens=100, completion_tokens=50, total_tokens=150)
        sample_evaluation.capacity = new_capacity
        assert sample_evaluation.capacity.prompt_tokens == 100
        assert sample_evaluation.capacity.completion_tokens == 50
        assert sample_evaluation.capacity.total_tokens == 150


class Test_PostProcess:
    def test_post_process_default_with_valid_json(self):
        """Test the default post-processing function with valid JSON content."""
        eval_obj = Evaluation()

        openai_json = {
            "choices": [{"message": {"content": '{"key": "value"}'}}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        }

        response, usage = eval_obj.post_process_default("ix", openai_json)
        assert response == {"key": "value"}
        assert usage == {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}

    def test_post_process_default_with_invalid_json(self):
        """Test the default post-processing function with invalid JSON content."""
        eval_obj = Evaluation()

        openai_json = {
            "choices": [{"message": {"content": "not json"}}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        }

        response, usage = eval_obj.post_process_default("ix", openai_json)
        assert response == {}
        assert usage == {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}

    def test_post_process_default_with_missing_fields(self):
        """Test the default post-processing function with missing fields in response."""
        eval_obj = Evaluation()

        # Test with incomplete response structure
        incomplete_response = {"choices": [{"message": {}}]}

        response, usage = eval_obj.post_process_default("ix", incomplete_response)
        assert response == {}
        assert usage == {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}

    def test_litellm_example(self, sample_evaluation):
        """Test the post-processing function with Litellm response."""
        expected_usage = TokenUsage(12, 34, 46)
        expected_output = {"Grade": 1, "Description": "This is a hardcoded test"}

        litellm_response = {
            "id": "randomguid",
            "created": 12345,
            "model": "myfancymodel",
            "object": "chat.completion",
            "system_fingerprint": None,
            "choices": [
                {
                    "finish_reason": "stop",
                    "index": 0,
                    "message": {
                        "content": '{"Grade":1,"Description":"This is a hardcoded test"}',
                        "role": "assistant",
                        "tool_calls": None,
                        "function_call": None,
                    },
                }
            ],
            "usage": {
                "completion_tokens": 34,
                "prompt_tokens": 12,
                "total_tokens": 46,
                "completion_tokens_details": None,
                "prompt_tokens_details": {"audio_tokens": None, "cached_tokens": 0},
                "cache_creation_input_tokens": 0,
                "cache_read_input_tokens": 0,
            },
        }

        response, usage = sample_evaluation.post_process_default("ix", litellm_response)

        assert TokenUsage(**usage) == expected_usage
        assert response == expected_output


@patch("tempfile.gettempdir")
def test_dump_to_temp(mock_temp, sample_evaluation, tmp_path):
    """Test that _dump_to_temp creates proper temp files."""
    mock_temp.return_value = tmp_path

    sample_evaluation._dump_to_temp(sample_ix="test_sample", raw_content={"test": "data"})
    # Verify that the temp directory is initially empty
    assert len(list(tmp_path.iterdir())) == 0

    # Enable logging
    sample_evaluation.log_enabled = True
    sample_evaluation._dump_to_temp(sample_ix="test_01", raw_content={"test": "data"})
    sample_evaluation._dump_to_temp(sample_ix="test_02", raw_content={"test": "data"})

    tmp_dir_contents = list((tmp_path / "evaluation_logs").iterdir())
    assert len(tmp_dir_contents) == 1

    log_dir = tmp_dir_contents[0]
    assert tmp_dir_contents[0].is_dir()

    # Check that the files were created with the expected names
    log_files = sorted(log_dir.iterdir())
    assert len(log_files) == 2
    assert log_files[0].name.startswith("test_01_raw_")
    assert log_files[1].name.startswith("test_02_raw_")
