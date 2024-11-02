import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the shapefile
shapefile_path = r"C:\Users\hp\Downloads\India_Shape\india_st.shx"
gdf = gpd.read_file(shapefile_path)

#Step 2: Read the Excel file containing sampling locations
excel_file_path = r"C:\Users\hp\Downloads\India_Shape\sites_sampling_phd.xlsx"
df = pd.read_excel(excel_file_path)
print(df.keys())
# Step 3: Plot the shapefile
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, color='lightblue', edgecolor='black')

# Step 4: Plot the sampling locations
plt.scatter(df['Lon'], df['Lat'], color='red', label='Sampling Locations', s=25)
for i, txt in enumerate(df['location']):
    plt.annotate(txt, (df['Lon'][i], df['Lat'][i]))

plt.title("Sampling Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
output_file_path = r"C:\Users\hp\Downloads\India_Shape\India_Map_with_Sampling_Locations.png"
plt.savefig(output_file_path)

plt.show()
