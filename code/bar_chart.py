
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "coffee_shops_clean.csv"
df = pd.read_csv(file_path)

# Calculate average people counted at each shop
averages = df.groupby("Coffee Shop")["People Counted"].mean()

# Create a lavender bar chart
ax = averages.plot(kind="bar", color="#C4A1E8", figsize=(8, 5))

# Add titles and labels
plt.title("Average Number of People by Coffee Shop")
plt.xlabel("Coffee Shop")
plt.ylabel("Average People Counted")
plt.xticks(rotation=0)

# Add small number labels above each bar
ax.bar_label(ax.containers[0], fmt="%.2f", padding=3, fontsize=5)

# Improve spacing
plt.tight_layout()
plt.show()
