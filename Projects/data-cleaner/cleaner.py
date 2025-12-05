import pandas as pd

df = pd.read_csv("sample.csv")

# Fix column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove duplicates
df = df.drop_duplicates()

# Convert to numeric (important!)
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["score"] = pd.to_numeric(df["score"], errors="coerce")

# Handle missing values
df["age"] = df["age"].fillna(df["age"].mean())
df["score"] = df["score"].fillna(df["score"].mean())
df["city"] = df["city"].fillna(df["city"].mode()[0])
df["name"] = df["name"].fillna("Unknown")

# Convert dtypes for final output
df["age"] = df["age"].astype(int)
df["score"] = df["score"].astype(int)

df.to_csv("cleaned_sample.csv", index=False)
print("Cleaning complete!")
