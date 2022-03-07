import read_data_source as ds
import exercise_1

df_income = ds.get_income()
df_demographics = ds.get_demographics()
df_income_demographics = exercise_1.get_income_demographics()

print("Number of rows and columns for income dataframe:",  df_income.shape)
print("Number of rows and columns for demographics dataframe:", df_demographics.shape)
print("Number of rows and columns for income + demographics dataframe:", df_income_demographics.shape)
