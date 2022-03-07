import matplotlib.pyplot as plt
import exercise_1

df_income_demographics = exercise_1.get_income_demographics()

fig, ax = plt.subplots(ncols=3)
fig.subplots_adjust(bottom=0.3, wspace=0.66)
df_income_demographics.groupby('target')['number_hours'].mean().sort_values().plot(kind='bar', color='red', ax=ax[0])
df_income_demographics.groupby('target')['age'].mean().sort_values().plot(kind='bar', color='green', ax=ax[1])
df_income_demographics.groupby('target')['savings'].mean().sort_values().plot(kind='bar', color='blue', ax=ax[2])
ax[0].legend(labels=['HOURS'], loc='upper center')
ax[1].legend(labels=['AGE'], loc='upper center')
ax[2].legend(labels=['SAVINGS'], loc='upper center')
plt.legend()
plt.show()
