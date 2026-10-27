import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "424 data Assignment 2 - Sheet1.csv"

df = pd.read_csv(file_path)

print("Total observations:", len(df))
print("\nObservations per coffee shop:")
print(df["Coffee Shop"].str.strip().value_counts())

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# Save the cleaned dataset
output_file = project_folder / "data" / "coffee_shops_clean.csv"
df.to_csv(output_file, index=False)

print("\nCleaned data saved to:", output_file)
