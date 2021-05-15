import os

import pandas as pd
from pandas import DataFrame


def processed(path: str):
    name, ext = os.path.splitext(path)
    return f'{name}_processed{ext}'


def read_data(file: str, **kwargs) -> DataFrame:
    if os.path.exists(proc := processed(file)):
        file = proc

    if not kwargs:
        kwargs = dict(
            sep=',',
            parse_dates=['date'],
            infer_datetime_format=True,
        )

    return pd.read_csv(file, **kwargs)


def read_groups(file: str):
    return pd.read_csv(
        file,
        sep=';',
    )


def clean_data(file: str, outliers: set[int]):
    proc = processed(file)
    if os.path.exists(proc):
        return

    df = pd.read_csv(file)
    df = df[~df.id_card.isin(outliers)]
    df.to_csv(proc)
