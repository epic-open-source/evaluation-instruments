import pandas as pd


def frame_from_evals(full_output: dict, criteria_outputs: list[str] = None) -> pd.DataFrame:
    """
    Convert the full output of the evaluation into a DataFrame.

    Useful for when the evaluation returns multiple outputs per criteria, such as a score plus evidence.

    Parameters
    ----------
    full_output : dict
        The full output of the evaluation, typically a dictionary with keys as the primary keys and values as dictionaries
        containing the criteria and their respective outputs.
    criteria_outputs : list[str], optional
        The names of the outputs to include in the DataFrame. If not provided, defaults to ["evidence", "score"].
        Specify [] or a single valued list to return a DataFrame with only one level, the criteria names.

    Returns
    -------
    pd.DataFrame
        _description_
    """
    if not full_output:
        return pd.DataFrame()

    criteria_outputs = criteria_outputs if criteria_outputs is not None else ["evidence", "score"]
    if len(criteria_outputs) < 2:
        return pd.DataFrame.from_dict(full_output, orient="index")

    reformatted = {}
    for pk, criteria in full_output.items():
        reformatted[pk] = {}
        for crit, values in criteria.items():
            for name, val in zip(criteria_outputs, values):
                reformatted[pk][(crit, name)] = val

    df = pd.DataFrame.from_dict(reformatted, orient="index")
    df.columns = pd.MultiIndex.from_tuples(df.columns)

    return df
