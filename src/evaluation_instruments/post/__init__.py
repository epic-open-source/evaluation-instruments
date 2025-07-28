import pandas as pd

def frame_from_evals(full_output: dict) -> pd.DataFrame:
    """
    Convert the output of the evaluation into a DataFrame.

    Handles direct, singly valued rubric outputs as well as nested dictionaries of key-value
    such as {score: int, explanation: str} pairs.

    Parameters
    ----------
    full_output : dict
        The full output of the evaluation, typically a dictionary with keys as the primary keys and values as dictionaries
        containing the criteria and their respective outputs.

    Returns
    -------
    pd.DataFrame
        _description_
    """
    if not full_output:
        return pd.DataFrame()

    # Assume that first item is representative of the structure.
    output0 = next(iter(full_output.values()), None)

    if not isinstance(output0, dict):
        raise ValueError("The output must be a dictionary with index-oriented dictionary with column-value pairs")
    if (item := next(iter(output0.values()), None)):
        if not isinstance(item, dict):
            return pd.DataFrame.from_dict(full_output, orient="index")

    reformatted = {
        row: {
            (group, col): val
                for group, subdict in groupdict.items()
                for col, val in subdict.items()
        }
        for row, groupdict in full_output.items()
    }

    df = pd.DataFrame.from_dict(reformatted, orient="index")
    df.columns = pd.MultiIndex.from_tuples(df.columns)

    return df
