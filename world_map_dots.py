import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import random
import json
import argparse


def plot_world_map(cities):
    # Define colors for land hatch patterns
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
    fig, ax = plt.subplots(
        figsize=(15, 10), subplot_kw={"projection": ccrs.PlateCarree()}
    )

    # Add coastlines and borders
    ax.add_feature(cfeature.COASTLINE, edgecolor="black", linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, edgecolor="black", linewidth=0.5)

    # Get the Natural Earth shapefile for land
    land_shp = shpreader.natural_earth(
        resolution="110m", category="physical", name="land"
    )
    reader = shpreader.Reader(land_shp)

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
            alpha=0.7,
        )

    # Plot cities on the map
    for city, coords in cities.items():
        ax.scatter(
            coords[0],
            coords[1],
            color="silver",
            s=100,
            transform=ccrs.PlateCarree(),
            zorder=10,
            alpha=0.7,
        )

    # Set the background color to black
    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")

    # Remove axes
    ax.axis("off")

    # Set the title
    plt.title("World Map with Cities", color="white", fontsize=20)

    # Adjust layout and display the map
    plt.tight_layout(pad=0)
    plt.subplots_adjust(top=0.95)  # Adjust top margin to prevent title cutoff

    # Save the plot
    fn = random.randint(1, 1000000)

    # Set the position and size of the image
    # The position and size of the image as tuple (left, right, bottom, top) in data coordinates.
    ax.set_extent([-180.0, 180.0, -65.0, 90.0], ccrs.PlateCarree())  # Adjusted extent
    plt.savefig(f"maps/world_map_{fn}.png", dpi=300)
    # Show the plot
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a world map with cities.")
    parser.add_argument("cities_file", type=str, help="Path to the JSON file containing city data.")
    args = parser.parse_args()

    with open(args.cities_file, "r") as f:
        cities = json.load(f)

    plot_world_map(cities)
