import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import random


def plot_world_map():
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

    # Define city locations
    cities = {
        "London": (-0.1276474, 51.5073219),
        "Paris": (2.3522219, 48.856614),
        "Berlin": (13.4105300, 52.5243700),
        "New York": (-74.0059740, 40.7127770),
        "Sofia": (23.3218670, 42.6975100),
        "Istanbul": (28.9745630, 41.0128610),
        "Tokyo": (139.6917060, 35.6894870),
    }

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
    ax.set_extent([-180.0, 180.0, -65.0, 90.0], ccrs.PlateCarree())  # Adjusted extent
    plt.savefig(f"maps/world_map_{fn}.png", dpi=300)
    # Show the plot
    plt.show()


# Call the function to generate the map
plot_world_map()
