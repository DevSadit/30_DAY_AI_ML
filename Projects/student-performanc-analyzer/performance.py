# Load the dataset
# Find each student’s average score
# Find the top 3 performers
# Find subject-wise highest & lowest score
# Make a bar chart showing each student’s average
# Create a pass/fail column (pass = avg > 60)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
# print(df)

# average for all students
df["average"] = df[["math", "science", "english"]].mean(axis=1)
# print(df)


# top 3 performers
top_3 = df["average"].sort_values("average", ascending=False)
print(top_3)
