import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.patches as mpatches
from cartopy.io import shapereader

# Create a new figure and axis with a specific projection
fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={"projection": ccrs.PlateCarree()})

# Add coastlines and borders
ax.add_feature(cfeature.COASTLINE, edgecolor="gray", linewidth=0.5)
ax.add_feature(cfeature.BORDERS, edgecolor="gray", linewidth=0.5)

# Get the Natural Earth shapefile for land
shapename = "physical"
land_shp = shapereader.natural_earth(resolution="110m", category=shapename, name="land")
reader = shapereader.Reader(land_shp)

# Add land feature with a white dot pattern
for geometry in reader.geometries():
    ax.add_geometries(
        [geometry],
        ccrs.PlateCarree(),
        facecolor="none",
        edgecolor="gray",
        linewidth=0.5,
        hatch="...",
    )

# Set the background color to black
ax.set_facecolor("black")
fig.patch.set_facecolor("black")

# Remove axes
ax.axis("off")

# Set the title
plt.title("World Map", color="white", fontsize=20)

# Adjust layout and display the map
plt.tight_layout()
plt.show()
