from pathlib import Path

import pandas as pd


def load_dataframe(
    csv_path: Path, start_year: int = -1, end_year: int = -1
) -> pd.DataFrame:
    if end_year != -1:
        assert end_year >= start_year

    df = pd.read_csv(csv_path, parse_dates=["dt"])

    if start_year != -1:
        df = df[df.dt.dt.year >= start_year]
    if end_year != -1:
        df = df[df.dt.dt.year <= end_year]

    return df


def get_city_mean_annual_temperature(df: pd.DataFrame, city: str) -> pd.Series:
    city_avgtemp_df = df[df.City == city]
    city_avgtemp_series = city_avgtemp_df.groupby(
        city_avgtemp_df.dt.dt.year
    ).mean(numeric_only=True)["AverageTemperature"]

    return city_avgtemp_series
