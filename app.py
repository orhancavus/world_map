import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 6), facecolor="black")

# Create a Basemap instance
m = Basemap(projection="mill", lon_0=0, resolution="c", ax=ax)

# Draw coastlines and countries, but in black to match the background
m.drawcoastlines(color="black")
m.drawcountries(color="black")

# Generate latitude and longitude values for the dots
num_dots = 2000
lats = np.random.uniform(-90, 90, num_dots)
lons = np.random.uniform(-180, 180, num_dots)

# Convert latitudes and longitudes to map coordinates
x, y = m(lons, lats)

# Plot the dots
m.scatter(x, y, color="white", marker="o", s=1, alpha=0.8)

# Hide the axis
ax.axis("off")

# Save and show the plot
plt.savefig(
    "world_map_dots.png",
    dpi=300,
    bbox_inches="tight",
    pad_inches=0,
    facecolor=fig.get_facecolor(),
)
plt.show()
