import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Load the data
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "coffee_shops_clean.csv"
df = pd.read_csv(file_path)

# Convert times into hours so they can be sorted correctly
df["Time Hour"] = pd.to_datetime(
    df["Time"], format="%I:%M %p"
).dt.hour

# Calculate the average number of people for each shop and time
heatmap_data = df.pivot_table(
    index="Coffee Shop",
    columns="Time Hour",
    values="People Counted",
    aggfunc="mean"
)

# Sort the times from earliest to latest
heatmap_data = heatmap_data.reindex(
    sorted(heatmap_data.columns), axis=1
)

# Make missing observations appear gray instead of inventing values
data = np.ma.masked_invalid(heatmap_data.to_numpy())

cmap = plt.get_cmap("RdYlGn").copy()
cmap.set_bad(color="#D9D9D9")

# Create the heatmap
fig, ax = plt.subplots(figsize=(11, 5.5))

image = ax.imshow(
    data,
    aspect="auto",
    cmap=cmap,
    interpolation="nearest",
    vmin=0
)

# Add the average value inside each cell
for row in range(data.shape[0]):
    for col in range(data.shape[1]):
        value = data[row, col]

        if not np.ma.is_masked(value):
            text_color = "black"

            ax.text(
                col, row, f"{value:.1f}",
                ha="center",
                va="center",
                color=text_color,
                fontsize=10,
                fontweight="bold"
            )

# Label the shops and observation times
ax.set_yticks(range(len(heatmap_data.index)))
ax.set_yticklabels(heatmap_data.index)

ax.set_xticks(range(len(heatmap_data.columns)))
ax.set_xticklabels([
    f"{hour % 12 or 12} {'AM' if hour < 12 else 'PM'}"
    for hour in heatmap_data.columns
])

ax.set_title("Average Number of People by Coffee Shop and Time")
ax.set_xlabel("Time of Day")
ax.set_ylabel("Coffee Shop")

# Add a legend showing what the colors mean
colorbar = fig.colorbar(image, ax=ax)
colorbar.set_label("Average People Counted")

plt.tight_layout()
plt.show()