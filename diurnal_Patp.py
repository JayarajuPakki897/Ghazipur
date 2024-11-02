import pandas as pd
import matplotlib.pyplot as plt

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)
print(df.keys())

# Convert the 'From Date' column to datetime with the correct format
df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# Define the central date
central_date = pd.Timestamp('2024-04-22')

# Check if the central date exists in the DataFrame
if central_date not in df['From Date'].values:
    raise ValueError(f"The central date {central_date} is not found in the 'From Date' column of the DataFrame.")

# Find the index of the central date
central_index = df[df['From Date'] == central_date].index[0]

# Calculate the index range for 7 days before and 7 days after the central date
start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# Select the rows within the calculated range
selected_data = df.iloc[start_index:end_index]

# Remove outliers using the IQR method
Q1 = selected_data['NO2'].quantile(0.25)
Q3 = selected_data['NO2'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
selected_data = selected_data[(selected_data['NO2'] >= lower_bound) & (selected_data['NO2'] <= upper_bound)]

# Extract the hour from the 'From Date' column
selected_data['Hour'] = selected_data['From Date'].dt.hour

# Group by the hour of the day and calculate the mean NO2 concentration
diurnal_data = selected_data.groupby('Hour')['NO2'].mean()

# Plot the diurnal pattern
plt.figure(figsize=(10, 6))
plt.plot(diurnal_data.index, diurnal_data.values, marker='o', linestyle='-', label='NO2')
plt.title('Diurnal Pattern of NO2 (µg/m³) Concentrations')
plt.xlabel('Hour of the Day')
plt.ylabel('Mean NO2 Concentration (µg/m³)')
plt.xticks(range(0, 24))
plt.grid(True)
plt.legend()

# Save the diurnal plot
#diurnal_save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Diurnal_NO2_Patparganj_2024.png'
#plt.savefig(diurnal_save_path)

#plt.show()





import pandas as pd
import matplotlib.pyplot as plt

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)
print(df.keys())

# Convert the 'From Date' column to datetime with the correct format
df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# Define the central date
central_date = pd.Timestamp('2024-04-22')

# Check if the central date exists in the DataFrame
if central_date not in df['From Date'].values:
    raise ValueError(f"The central date {central_date} is not found in the 'From Date' column of the DataFrame.")

# Find the index of the central date
central_index = df[df['From Date'] == central_date].index[0]

# Calculate the index range for 7 days before and 7 days after the central date
start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# Select the rows within the calculated range
selected_data = df.iloc[start_index:end_index]

# Remove outliers using the IQR method
Q1 = selected_data['PM2.5'].quantile(0.25)
Q3 = selected_data['PM2.5'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
selected_data = selected_data[(selected_data['PM2.5'] >= lower_bound) & (selected_data['PM2.5'] <= upper_bound)]

# Extract the hour from the 'From Date' column
selected_data['Hour'] = selected_data['From Date'].dt.hour

# Group by the hour of the day and calculate the mean PM2.5 concentration
diurnal_data = selected_data.groupby('Hour')['PM2.5'].mean()

# Plot the diurnal pattern
plt.figure(figsize=(10, 6))
plt.plot(diurnal_data.index, diurnal_data.values, marker='o', linestyle='-', label='PM2.5')
plt.title('Diurnal Pattern of PM2.5 (µg/m³) Concentrations')
plt.xlabel('Hour of the Day')
plt.ylabel('Mean PM2.5 Concentration (µg/m³)')
plt.xticks(range(0, 24))
plt.grid(True)
plt.legend()

# Save the diurnal plot
# diurnal_save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Diurnal_PM2.5_Patparganj_2024.png'
# plt.savefig(diurnal_save_path)

# plt.show()








import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)
print(df.keys())

# Convert the 'From Date' column to datetime with the correct format
df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# Define the central date
central_date = pd.Timestamp('2024-04-22')

# Check if the central date exists in the DataFrame
if central_date not in df['From Date'].values:
    raise ValueError(f"The central date {central_date} is not found in the 'From Date' column of the DataFrame.")

# Find the index of the central date
central_index = df[df['From Date'] == central_date].index[0]

# Calculate the index range for 7 days before and 7 days after the central date
start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# Select the rows within the calculated range
selected_data = df.iloc[start_index:end_index]

# Extract 'WS' and 'WD' data
ws = selected_data['WS']
wd = selected_data['WD']

# Create wind rose plot
plt.figure(figsize=(10, 6))
ax = WindroseAxes.from_ax()
ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
ax.set_title('Wind Rose Plot')
ax.set_legend()

# Save the wind rose plot
# windrose_save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Windrose_Patparganj_2024.png'
# plt.savefig(windrose_save_path)

# plt.show()






import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)
print(df.keys())

# Convert the 'From Date' column to datetime with the correct format
df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# Define the central date
central_date = pd.Timestamp('2024-04-22')

# Check if the central date exists in the DataFrame
if central_date not in df['From Date'].values:
    raise ValueError(f"The central date {central_date} is not found in the 'From Date' column of the DataFrame.")

# Find the index of the central date
central_index = df[df['From Date'] == central_date].index[0]

# Calculate the index range for 7 days before and 7 days after the central date
start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# Select the rows within the calculated range
selected_data = df.iloc[start_index:end_index]

# List of pollutants to plot
pollutants = ['PM10', 'NO', 'NO2', 'NOx', 'NH3', 'SO2', 'CO', 'Ozone','Benzene','Toluene']

# Create diurnal plots for each pollutant
for pollutant in pollutants:
    if pollutant not in selected_data.columns:
        print(f"{pollutant} not found in the DataFrame.")
        continue

    # Remove outliers using the IQR method
    Q1 = selected_data[pollutant].quantile(0.25)
    Q3 = selected_data[pollutant].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    filtered_data = selected_data[(selected_data[pollutant] >= lower_bound) & (selected_data[pollutant] <= upper_bound)]

    # Extract the hour from the 'From Date' column
    filtered_data['Hour'] = filtered_data['From Date'].dt.hour

    # Group by the hour of the day and calculate the mean and standard deviation of concentrations
    diurnal_data = filtered_data.groupby('Hour')[pollutant].agg(['mean', 'std'])

    # Plot the diurnal pattern with error bars
    plt.figure(figsize=(10, 6))
    plt.errorbar(diurnal_data.index, diurnal_data['mean'], yerr=diurnal_data['std'], fmt='o-', label=pollutant, capsize=5)
    plt.title(f'Diurnal Pattern of {pollutant} (µg/m³) Concentrations')
    plt.xlabel('Hour of the Day')
    plt.ylabel(f'Mean {pollutant} Concentration (µg/m³)')
    plt.xticks(range(0, 24))
    #plt.grid(True)
    plt.legend()

    # Save the diurnal plot
    diurnal_save_path = fr'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Diurnal_{pollutant}_Patparganj_2024.png'
    plt.savefig(diurnal_save_path)

    plt.show()
