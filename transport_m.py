import matplotlib.pyplot as plt
import numpy as np

# Data input
data = {
    "M1": {
        "Buraki": [20, 217.927, 0, 0, 0, 0],
        "Kapusta": [80, 45.213, 0, 0, 0, 0],
        "Marchew": [60, 80, 0, 0, 0, 0],
        "Ziemniaki": [240, 4.666, 0, 0, 0, 0]
    },
    "M2": {
        "Buraki": [0, 0, 0, 35.665, 0, 0],
        "Kapusta": [0, 0, 0, 12.138, 0, 0],
        "Marchew": [0, 0, 0, 22.197, 0, 0],
        "Ziemniaki": [0, 0, 0, 30, 0, 0]
    },
    "M3": {
        "Buraki": [0, 0, 0, 0, 90, 0],
        "Kapusta": [0, 0, 0, 0, 230, 0],
        "Marchew": [0, 0, 0, 0, 210, 0],
        "Ziemniaki": [0, 0, 0, 0, 100, 0]
    }
}

# Create a single plot with 3 subplots side by side, sharing the same y-axis scale
fig, axs = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Plotting each subplot
for ax, (M, veg_data) in zip(axs, data.items()):
    x = np.arange(len(next(iter(veg_data.values()))))  # Create x values based on the length of any data list
    bar_width = 0.2

    for idx, (veg, amounts) in enumerate(veg_data.items()):
        ax.bar(x + idx * bar_width, amounts, width=bar_width, label=veg)

    ax.set_xlabel('Products')
    ax.set_title(f'Transport to {M}')
    ax.set_xticks(x + bar_width)
    ax.set_xticklabels(['P1', 'P2', 'P3', 'P4', 'P5', 'P6'])
    if ax == axs[0]:
        ax.set_ylabel('Amount')

# Add a single legend for all subplots
handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right')

plt.tight_layout()
plt.show()
