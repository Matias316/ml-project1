import matplotlib.pyplot as plt
import exercise_1

df_income_demographics = exercise_1.get_income_demographics()

plt.scatter(x=df_income_demographics['age'],
            y=df_income_demographics['number_hours'],
            s=10,
            alpha=0.1)
plt.xlabel('Age')
plt.ylabel('Number of hours reported')
plt.title('Age vs Reported hours')
plt.show()
