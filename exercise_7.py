import exercise_1

df_income_demographics = exercise_1.get_income_demographics()
only_private_workers = df_income_demographics[df_income_demographics['type_work'].str.strip() == 'Private']
only_private_workers_with_salary_greater_than_350000 = only_private_workers[only_private_workers['savings'] > 350000]

print(
    only_private_workers_with_salary_greater_than_350000.groupby(['age', 'study']).agg({"savings": "mean"}).sort_values(
        by="savings", ascending=False).head(10))
