import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import random
from cartopy.io import shapereader

colors = [
    "blue",
    "red",
    "orange",
    "green",
    "gray",
    "magenta",
    "brown",
    "cyan",
    "purple",
    "pink",
    "yellow",
    "teal",
    "lavender",
    "lime",
    "turquoise",
    "maroon",
    "gold",
    "olive",
    "navy",
]


# Create a new figure and axis with a specific projection
fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={"projection": ccrs.PlateCarree()})

# Add coastlines and borders
ax.add_feature(cfeature.COASTLINE, edgecolor="black", linewidth=0.5)
ax.add_feature(cfeature.BORDERS, edgecolor="black", linewidth=0.5)

# Get the Natural Earth shapefile for land
shapename = "physical"
land_shp = shapereader.natural_earth(resolution="110m", category=shapename, name="land")
reader = shapereader.Reader(land_shp)

# Add land feature with a white dot pattern
for geometry in reader.geometries():
    random_color = random.choice(colors)
    ax.add_geometries(
        [geometry],
        ccrs.PlateCarree(),
        facecolor="none",
        edgecolor="orange",
        linewidth=0.1,
        hatch=".",
    )

# Add points for London and Paris


# Set the background color to black
ax.set_facecolor("black")
fig.patch.set_facecolor("black")

# Remove axes
ax.axis("off")

# Set the title
plt.title("World Map", color="white", fontsize=20)

# Adjust layout and display the map
plt.tight_layout()

fn = random.randint(1, 1000000)
plt.savefig(f"maps/world_map_{fn}.png", dpi=300)
plt.show()
