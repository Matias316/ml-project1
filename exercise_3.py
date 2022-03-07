import exercise_1

df_income_demographics = exercise_1.get_income_demographics()

# Univariate analysis over age variable
print("Min and max ages in dataset", df_income_demographics['age'].min().astype(int), df_income_demographics['age'].max().astype(int))
print("Average age in dataset", df_income_demographics['age'].mean().astype(int))
print("Median age in dataset", df_income_demographics['age'].median().astype(int))
print("Is age populated in all records in dataset?", df_income_demographics['age'].isna().sum() == 0, '\n')

# Univariate analysis over number of hours reported
print("Min and max number of hours reported in dataset", df_income_demographics['number_hours'].min().astype(int), df_income_demographics['number_hours'].max().astype(int))
print("Average number of hours reported in dataset", df_income_demographics['number_hours'].mean().astype(int))
print("Median number of hours reported in dataset", df_income_demographics['number_hours'].median().astype(int))
print("Is number of hours reported populated in all records in dataset?", df_income_demographics['number_hours'].isna().sum() == 0, '\n')

# Univariate analysis over savings variable in demographics dataset
print("Min and max savings in dataset", df_income_demographics['savings'].min().round(2), df_income_demographics['savings'].max().round(2))
print("Average savings in dataset", df_income_demographics['savings'].mean().round(2))
print("Median savings in dataset", df_income_demographics['savings'].median().round(2))
print("Is savings populated in all records in dataset?", df_income_demographics['savings'].isna().sum() == 0, '\n')

# Univariate analysis over target variable in demographics dataset
print("Is target populated in all records in dataset?", df_income_demographics['target'].isnull().sum() == 0)
print("Distribution of people per income in dataset\n", df_income_demographics['target'].value_counts().to_string())

