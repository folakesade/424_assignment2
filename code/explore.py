
import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "coffee_shops_clean.csv"

df = pd.read_csv(file_path)

print("AVERAGE PEOPLE COUNTED BY SHOP")
print(df.groupby("Coffee Shop")["People Counted"].mean().round(2))

print("\nAVERAGE PEOPLE WORKING BY SHOP")
print(df.groupby("Coffee Shop")["People Working"].mean().round(2))

print("\nAVERAGE PEOPLE IN LINE BY SHOP")
print(df.groupby("Coffee Shop")["People in Line"].mean().round(2))

print("\nAVERAGE AVAILABLE SEATS BY SHOP")
print(df.groupby("Coffee Shop")["Available Seats"].mean().round(2))

print("\nPEOPLE COUNTED BY TIME")
print(df.groupby("Time")["People Counted"].mean().round(2))
