import geopandas as gpd
import matplotlib.pyplot as plt

# Define the path to the shapefile
shapefile_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\DL_FIRE_J1V-C2_477351\fire_nrt_J1V-C2_477351.shx'

# Load the shapefile
gdf = gpd.read_file(shapefile_path)

# Plot the shapefile
gdf.plot()

# Show the plot
plt.show()
