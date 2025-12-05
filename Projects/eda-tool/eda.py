import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

# print("Shape:", df.shape)
# print("\nHead:\n", df.head(2))
# print("\nMissing Values:\n", df.isnull().sum())
# print("\nData Types:\n", df.dtypes)


print("\nStatistics:\n", df.describe())


# correlation matrix
corr = df.corr(numeric_only=True)
corr.to_csv("correlation_matrix.csv")
print("\nCorrelation Matrix saved.")


df.hist(figsize=(10, 8))
plt.savefig("histograms.png")

df.boxplot(figsize=(10, 8))
plt.savefig("boxplot.png")


with open("report.txt", "w") as f:
    f.write("Shape:\n" + str(df.shape) + "\n\n")
    f.write("Missing Values:\n" + str(df.isnull().sum()) + "\n\n")
    f.write("Data Types:\n" + str(df.dtypes) + "\n\n")
    f.write("Stats:\n" + str(df.describe()) + "\n\n")
