import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("salary.csv")
# print(df)

avg_salary = df["salary"].mean()
# print(avg_salary)

highest = df["salary"].max()
# print(highest)

lowest = df["salary"].min()
# print(lowest)


dept_count = df["department"].value_counts()
# print(dept_count)

# histogram
plt.hist(df["salary"], bins=5)
plt.xlabel("salary")
plt.ylabel("number of employee")
plt.title("salary distribution")
plt.show()
