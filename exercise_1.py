import read_data_source as ds
import pandas as pd


def get_income_demographics():
    """Returns income-demographics dataframe"""
    df_income = ds.get_income()
    df_demographics = ds.get_demographics()
    df_income_demographics = pd.merge(df_income, df_demographics, on="id")
    return df_income_demographics
