import pandas as pd

# Load dataset
df = pd.read_csv("data/supermarket_sales.csv")

print("\nBEFORE CLEANING")
print(df)

# 1. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 2. Clean column names
df.columns = df.columns.str.strip().str.lower()

# 3. Convert Date column to datetime
df['date'] = pd.to_datetime(df['date'])

print("\nAFTER CLEANING")
print(df)

print("\nDATA TYPES AFTER CLEANING")
print(df.dtypes)
