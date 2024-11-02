import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the path to your Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'

# Load the Excel file into a DataFrame, assuming the second sheet (index 1)
df = pd.read_excel(data_path, sheet_name=1)

# Assuming 'WD' is the column for Wind Direction and 'WS' for Wind Speed
wind_direction = df['WD'].values
wind_speed = df['WS'].values

# Remove NaN values from both wind_direction and wind_speed
valid_indices = ~np.isnan(wind_direction) & ~np.isnan(wind_speed)
wind_direction = wind_direction[valid_indices]
wind_speed = wind_speed[valid_indices]

# Convert wind direction from degrees to radians for plotting
wind_direction_rad = np.radians(wind_direction)

# Create a wind rose plot using seaborn
plt.figure(figsize=(10, 8))
sns.set(style="white", palette="pastel")
ax = plt.subplot(111, projection='polar')
ax.set_theta_direction(-1)  # Ensure clockwise direction

# Bin wind directions into 16 sectors
n_direction_bins = 16
direction_bins = np.linspace(0, 2 * np.pi, n_direction_bins + 1)

# Aggregate wind speeds in each direction bin
wind_speed_bins = []
for i in range(n_direction_bins):
    if i == n_direction_bins - 1:
        indices = np.where((wind_direction_rad >= direction_bins[i]) | (wind_direction_rad < direction_bins[0]))
    else:
        indices = np.where((wind_direction_rad >= direction_bins[i]) & (wind_direction_rad < direction_bins[i + 1]))
    wind_speed_bins.append(np.mean(wind_speed[indices]))

# Plot wind rose segments
bars = ax.bar(direction_bins[:-1], wind_speed_bins, width=np.diff(direction_bins), edgecolor='grey', linewidth=1)

plt.title('Wind Rose Plot')
plt.show()
