import pandas as pd


def get_income():
    """Returns income dataframe from CSV file data source"""
    column_names = ['id', 'savings', 'capital_gain', 'capital_loss', 'number_hours', 'country', 'target']
    df_income = pd.read_csv('datasource/_income_.csv', names=column_names, header=None)
    return df_income


def get_demographics():
    """Returns demographics dataframe from CSV file data source"""
    column_names = ['id', 'age', 'type_work', 'study', 'study_coded', 'marital_status', 'activity', 'type_relationship', 'ethnic_group', 'biological_sex']
    df_demographics = pd.read_csv('datasource/_demographics_.csv', names=column_names, header=None)
    return df_demographics
