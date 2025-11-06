import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Create a figure and axis with Plate Carrée projection
fig, ax = plt.subplots(subplot_kw={"projection": ccrs.PlateCarree()})

# Example: adding coastlines
ax.coastlines()

# Example: plotting data with Plate Carrée projection
ax.plot([-60, 60], [100, 100], color="blue", marker="o", transform=ccrs.PlateCarree())

plt.show()
