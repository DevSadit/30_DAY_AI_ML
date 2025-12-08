import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
# print(df)

# average collumn
df["average"] = df[["math", "science", "english"]].mean(axis=1)
# print(df["average"])


# top 3 performance
top_3 = df.sort_values("average", ascending=False).head(3)
# print(top_3)


# subject wise highest and lowest
highest_math = df.loc[df["math"].idxmax()]
lowest_math = df.loc[df["math"].idxmin()]

print(highest_math, lowest_math)
