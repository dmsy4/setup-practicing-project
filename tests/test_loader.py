from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from temperature_package.loader import load_dataframe


@pytest.fixture
def get_df(start_year: int, end_year: int) -> pd.DataFrame:
    return load_dataframe(Path("./data/archive.zip"), start_year, end_year)


@pytest.mark.parametrize(
    "start_year, end_year",
    [
        (1900, 1900),
        (1917, 1923),
        (2000, 2001),
        (-1, -1),
        (-1, 1999),
        (2000, -1),
    ],
)
def test_df_datarange(
    get_df: pd.DataFrame, start_year: int, end_year: int
) -> None:
    df = get_df
    min_df_year = df.dt.dt.year.min()
    max_df_year = df.dt.dt.year.max()

    if start_year <= min_df_year:
        start_year = min_df_year
    if end_year >= max_df_year or end_year == -1:
        end_year = max_df_year

    df_years = sorted(pd.unique(df.dt.dt.year))
    expected_dates = np.arange(start_year, end_year + 1)

    np.testing.assert_array_equal(df_years, expected_dates)
