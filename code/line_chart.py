
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "coffee_shops_clean.csv"
df = pd.read_csv(file_path)

# Convert observation times into a format Python can sort
df["Time"] = pd.to_datetime(df["Time"], format="%I:%M %p").dt.hour

# Calculate average people counted for each shop at each hour
averages = df.groupby(["Time", "Coffee Shop"])["People Counted"].mean().unstack()

# Create the line chart
ax = averages.plot(
    kind="line",
    marker="o",
    figsize=(9, 5),
    linewidth=2.5,
    color=["#A7D8F0", "#F4B6C2", "#C4A1E8"],
    markersize=7
)

# Add titles and labels
plt.title("Average Number of People by Time and Coffee Shop")
plt.xlabel("Time of Day")
plt.ylabel("Average People Counted")

# Display readable time labels
plt.xticks(
    ticks=averages.index,
    labels=[f"{hour % 12 or 12} {'AM' if hour < 12 else 'PM'}" for hour in averages.index]
)

plt.legend(title="Coffee Shop")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

