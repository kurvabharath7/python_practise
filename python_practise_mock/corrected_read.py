import pandas as pd

df = pd.read_csv("corrected_csv")

print("Original Data:")
print(df)

# Remove duplicate records
df_clean = df.drop_duplicates()

# Remove rows with null values
df_clean = df_clean.dropna()

# Display cleaned data
print("\nAfter Removing Duplicate and Null Values:")
print(df_clean)

