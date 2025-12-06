import pandas as pd

df = pd.read_csv("grades.csv")
# print(df)

math_avg = df["math"].mean()
eng_avg = df["english"].mean()
sci_avg = df["science"].mean()

print("math average ", math_avg)
print("english average ", eng_avg)
print("science average ", sci_avg)
