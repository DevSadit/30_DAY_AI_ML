import pandas as pd
import matplotlib.pyplot as plt

# read and make df
df = pd.read_csv("expense.csv")

# transform to date
df["date"] = pd.to_datetime(df["date"])

# total amount
total = df["amount"].sum()

# per category total
category_total = df.groupby("category").amount.sum()

# monthly spending
df["month"] = df["date"].dt.month
monthly_totals = df.groupby("month")["amount"].sum()
print(monthly_totals)


# chart

category_total.plot(kind="bar")
# monthly_totals.plot(kind="bar")
# total.plot(kind="bar")
plt.title("Expense by category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()

df.to_csv("cleaned_expenses.csv", index=False)
