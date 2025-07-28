import pandas as pd
from pandas.testing import assert_frame_equal

from evaluation_instruments.post import frame_from_evals


def evaluation_output():
    return {
        "sample1": {
            "criteria1": {"class":"strong evidence", "score": 5, "notes": "additional info"},
            "criteria2": {"class":"weak evidence", "score": 2, "notes": "notes"},
        },
        "sample2": {
            "criteria1": {"class":"moderate evidence", "score": 3, "notes": "more info"},
            "criteria2": {"class":"no evidence", "score": 1, "notes": "other notes"},
        },
    }


def test_frame_from_evals_with_details():
    """Test basic conversion of evaluation outputs to pandas DataFrame."""
    expected_data = {
        ("criteria1", "class"): ["strong evidence", "moderate evidence"],
        ("criteria1", "score"): [5, 3],
        ("criteria1", "notes"): ["additional info", "more info"],
        ("criteria2", "class"): ["weak evidence", "no evidence"],
        ("criteria2", "score"): [2, 1],
        ("criteria2", "notes"): ["notes", "other notes"],
    }
    expected_df = pd.DataFrame(
        expected_data, index=["sample1", "sample2"], columns=pd.MultiIndex.from_tuples(expected_data.keys())
    )
    output = evaluation_output()

    # Act
    result_df = frame_from_evals(output)

    # Verify exact match with expected DataFrame
    assert_frame_equal(result_df, expected_df)


def test_frame_from_evals_score():
    """Test frame_from_evals with custom output names."""
    # Sample evaluation output
    output = {"sample1": {"criteria1": 5, "criteria2": 2},
              "sample2": {"criteria1": 3, "criteria2": 1}}

    expected_df = pd.DataFrame(
        {"criteria1": [5, 3],"criteria2": [2, 1]}, index=["sample1", "sample2"]
    )

    # Convert to DataFrame with custom output columns
    result_df = frame_from_evals(output)

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



def test_frame_from_evals_single_score_multiple_items():
    """Test frame_from_evals with multiple items but only single score values (no evidence)."""
    # Sample with single score per criteria, multiple items
    eval_output = {
        "sample1": {
            "criteria1": 4,
            "criteria2": 3,
        },
        "sample2": {
            "criteria1": 5,
            "criteria2": 2,
        },
    }
    expected_df = pd.DataFrame(
        {"criteria1": [4, 5], "criteria2": [3, 2]},
        index=["sample1", "sample2"]
    )

    # Act
    result_df = frame_from_evals(eval_output)

    # Verify exact match with expected DataFrame
    assert_frame_equal(result_df, expected_df)
