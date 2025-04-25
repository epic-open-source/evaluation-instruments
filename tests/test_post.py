import pandas as pd
from pandas.testing import assert_frame_equal

from evaluation_instruments.post import frame_from_evals


def evaluation_output():
    return {
        "sample1": {
            "criteria1": ["strong evidence", 5, "additional info"],
            "criteria2": ["weak evidence", 2, "notes"],
        },
        "sample2": {
            "criteria1": ["moderate evidence", 3, "more info"],
            "criteria2": ["no evidence", 1, "other notes"],
        },
    }


def test_frame_from_evals_basic():
    """Test basic conversion of evaluation outputs to pandas DataFrame."""
    expected_data = {
        ("criteria1", "evidence"): ["strong evidence", "moderate evidence"],
        ("criteria1", "score"): [5, 3],
        ("criteria2", "evidence"): ["weak evidence", "no evidence"],
        ("criteria2", "score"): [2, 1],
    }
    expected_df = pd.DataFrame(
        expected_data, index=["sample1", "sample2"], columns=pd.MultiIndex.from_tuples(expected_data.keys())
    )
    output = evaluation_output()

    # Act
    result_df = frame_from_evals(output)

    # Verify exact match with expected DataFrame
    assert_frame_equal(result_df, expected_df)


def test_frame_from_evals_custom_outputs():
    """Test frame_from_evals with custom output names."""
    # Sample evaluation output
    output = evaluation_output()
    expected_data = {
        ("criteria1", "explanation"): ["strong evidence", "moderate evidence"],
        ("criteria1", "rating"): [5, 3],
        ("criteria1", "notes"): ["additional info", "more info"],
        ("criteria2", "explanation"): ["weak evidence", "no evidence"],
        ("criteria2", "rating"): [2, 1],
        ("criteria2", "notes"): ["notes", "other notes"],
    }
    expected_df = pd.DataFrame(
        expected_data, index=["sample1", "sample2"], columns=pd.MultiIndex.from_tuples(expected_data.keys())
    )

    # Convert to DataFrame with custom output columns
    result_df = frame_from_evals(output, criteria_outputs=["explanation", "rating", "notes"])

    # Verify exact match with expected DataFrame
    assert_frame_equal(result_df, expected_df)


def test_frame_from_evals_empty():
    """Test frame_from_evals with empty input."""
    # Empty evaluation output
    eval_output = {}

    # Convert to DataFrame
    result_df = frame_from_evals(eval_output)

    # Verify empty frame is created
    assert result_df.empty


def test_frame_from_evals_single_item():
    """Test frame_from_evals with a single item."""
    # Sample with single item

    expected_df = pd.DataFrame(
        {("criteria1", "evidence"): ["evidence"], ("criteria1", "score"): [4]},
        index=["sample1"],
        columns=pd.MultiIndex.from_tuples([("criteria1", "evidence"), ("criteria1", "score")]),
    )

    eval_output = {"sample1": {"criteria1": ["evidence", 4]}}

    # Act
    result_df = frame_from_evals(eval_output)

    # Verify exact match with expected DataFrame
    assert_frame_equal(result_df, expected_df)
