import pandas as pd


def frame_from_evals(full_output: dict, criteria_outputs: list[str] = None) -> pd.DataFrame:
    if not full_output:
        return pd.DataFrame()

    criteria_outputs = criteria_outputs or ["evidence", "score"]

    reformatted = {}
    for pk, criteria in full_output.items():
        reformatted[pk] = {}
        for crit, values in criteria.items():
            for name, val in zip(criteria_outputs, values):
                reformatted[pk][(crit, name)] = val

    df = pd.DataFrame.from_dict(reformatted, orient="index")
    df.columns = pd.MultiIndex.from_tuples(df.columns)

    return df
