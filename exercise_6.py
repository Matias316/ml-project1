import matplotlib.pyplot as plt
import exercise_1

df_income_demographics = exercise_1.get_income_demographics()

df_income_demographics.groupby('biological_sex')['number_hours', 'age'].mean().plot(kind='bar')
plt.tight_layout()
plt.show()
