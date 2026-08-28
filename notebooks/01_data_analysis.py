import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/recovery_data.csv")

print("\n========== RECOVERX DATA ANALYSIS ==========\n")

# 1. Dataset shape
print("1. Dataset Shape:")
print(df.shape)

# 2. Column names
print("\n2. Columns:")
print(df.columns.tolist())

# 3. First 5 records
print("\n3. First 5 Records:")
print(df.head())

# 4. Data types
print("\n4. Data Types:")
print(df.dtypes)

# 5. Missing values
print("\n5. Missing Values:")
print(df.isnull().sum())

# 6. Duplicate records
print("\n6. Duplicate Rows:")
print(df.duplicated().sum())

# 7. Recovery distribution
print("\n7. Recovery Distribution:")
print(df["recovered"].value_counts())

# 8. Recovery percentage
print("\n8. Recovery Percentage:")
print(
    df["recovered"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

# 9. Numerical statistics
print("\n9. Numerical Statistics:")
print(df.describe().round(2))

print("\n============================================")
print("EDA CHECK COMPLETE")
print("============================================")