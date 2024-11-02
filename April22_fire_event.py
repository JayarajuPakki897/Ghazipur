# import pandas as pd
# import matplotlib.pyplot as plt

# # Load your CSV file
# data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Raw_data_15Min_2018_site_1423_Jahangirpuri_Delhi_DPCC_15Min.csv'
# df = pd.read_csv(data_path)
# print(df.keys())
# # Convert the Timestamp column to datetime if it's not already in datetime format
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# # Define the central date
# central_date = pd.Timestamp('2018-10-23')

# # Find the index of the central date in the Timestamp column
# central_index = df[df['Timestamp'] == central_date].index[0]

# # Calculate the index range for 7 days before and 7 days after the central date
# start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
# end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# # Select the rows within the calculated range
# selected_data = df.iloc[start_index:end_index]

# # Remove outliers using IQR method
# Q1 = selected_data['PM2.5 (µg/m³)'].quantile(0.25)
# Q3 = selected_data['PM2.5 (µg/m³)'].quantile(0.75)
# IQR = Q3 - Q1
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR
# selected_data = selected_data[(selected_data['PM2.5 (µg/m³)'] >= lower_bound) & (selected_data['PM2.5 (µg/m³)'] <= upper_bound)]

# # Apply moving average
# window_size = 5  # Adjust window size as needed
# selected_data['Smoothed_PM2.5'] = selected_data['PM2.5 (µg/m³)'].rolling(window=window_size, min_periods=1).mean()

# # Plot the time series with moving average
# plt.figure(figsize=(10, 6))
# plt.plot(selected_data['Timestamp'], selected_data['Smoothed_PM2.5'], linestyle='-', label='PM$_{2.5}$')
# plt.title('Smoothed PM$_{2.5}$ Time Series')
# plt.xlabel('Date')
# plt.ylabel('Concentration (µg/m³)')
# #plt.grid(True)
# plt.xticks(rotation=45)

# # Highlight October 22nd
# oct_22_index = selected_data[selected_data['Timestamp'].dt.date == pd.Timestamp('2018-10-22').date()].index[0]
# plt.axvline(x=selected_data.loc[oct_22_index, 'Timestamp'], color='r', linestyle='--', linewidth=2)
# plt.annotate('October 22nd', xy=(selected_data.loc[oct_22_index, 'Timestamp'], selected_data.loc[oct_22_index, 'Smoothed_PM2.5']),
#              xytext=(-100, 50), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black'))

# plt.tight_layout()
# plt.legend()
# #plt.show()






# import pandas as pd
# import matplotlib.pyplot as plt

# # Load your CSV file
# data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Raw_data_15Min_2018_site_1423_Jahangirpuri_Delhi_DPCC_15Min.csv'
# df = pd.read_csv(data_path)

# # Convert the Timestamp column to datetime if it's not already in datetime format
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# # Define the central date
# central_date = pd.Timestamp('2018-10-23')

# # Find the index of the central date in the Timestamp column
# central_index = df[df['Timestamp'] == central_date].index[0]

# # Calculate the index range for 7 days before and 7 days after the central date
# start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
# end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# # Select the rows within the calculated range
# selected_data = df.iloc[start_index:end_index]

# # Remove outliers using IQR method
# Q1 = selected_data['CO (mg/m³)'].quantile(0.25)
# Q3 = selected_data['CO (mg/m³)'].quantile(0.75)
# IQR = Q3 - Q1
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR
# selected_data = selected_data[(selected_data['CO (mg/m³)'] >= lower_bound) & (selected_data['CO (mg/m³)'] <= upper_bound)]

# # Apply moving average
# window_size = 10  # Adjust window size as needed
# selected_data['Smoothed_PM2.5'] = selected_data['CO (mg/m³)'].rolling(window=window_size, min_periods=1).mean()

# # Plot the time series with moving average
# plt.figure(figsize=(10, 6))
# plt.plot(selected_data['Timestamp'], selected_data['Smoothed_PM2.5'], linestyle='-', label='CO (mg/m³)')
# plt.title('Smoothed CO (mg/m³) Time Series')
# plt.xlabel('Date')
# plt.ylabel('Concentration (µg/m³)')
# #plt.grid(True)
# plt.xticks(rotation=45)

# # Highlight October 22nd
# oct_22_index = selected_data[selected_data['Timestamp'].dt.date == pd.Timestamp('2018-10-22').date()].index[0]
# plt.axvline(x=selected_data.loc[oct_22_index, 'Timestamp'], color='r', linestyle='--', linewidth=2)
# plt.annotate('October 22nd', xy=(selected_data.loc[oct_22_index, 'Timestamp'], selected_data.loc[oct_22_index, 'Smoothed_PM2.5']),
#              xytext=(-100, 50), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black'))

# plt.tight_layout()
# plt.legend()
# save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Smoothed_CO_Time_Series.png'
# #plt.savefig(save_path)

# #plt.show()






# import pandas as pd
# import matplotlib.pyplot as plt

# # Load your CSV file
# data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Raw_data_15Min_2018_site_1423_Jahangirpuri_Delhi_DPCC_15Min.csv'
# df = pd.read_csv(data_path)

# # Convert the Timestamp column to datetime if it's not already in datetime format
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# # Define the central date
# central_date = pd.Timestamp('2018-10-23')

# # Find the index of the central date in the Timestamp column
# central_index = df[df['Timestamp'] == central_date].index[0]

# # Calculate the index range for 7 days before and 7 days after the central date
# start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
# end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# # Select the rows within the calculated range
# selected_data = df.iloc[start_index:end_index]

# # Remove outliers using IQR method
# Q1 = selected_data['Ozone (µg/m³)'].quantile(0.25)
# Q3 = selected_data['Ozone (µg/m³)'].quantile(0.75)
# IQR = Q3 - Q1
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR
# selected_data = selected_data[(selected_data['Ozone (µg/m³)'] >= lower_bound) & (selected_data['Ozone (µg/m³)'] <= upper_bound)]

# # Apply moving average
# window_size = 20  # Adjust window size as needed
# selected_data['Smoothed_PM2.5'] = selected_data['Ozone (µg/m³)'].rolling(window=window_size, min_periods=1).mean()

# # Plot the time series with moving average
# plt.figure(figsize=(10, 6))
# plt.plot(selected_data['Timestamp'], selected_data['Smoothed_PM2.5'], linestyle='-', label='Ozone (µg/m³)')
# plt.title('Smoothed Ozone (µg/m³) Time Series')
# plt.xlabel('Date')
# plt.ylabel('Concentration (µg/m³)')
# #plt.grid(True)
# plt.xticks(rotation=45)

# # Highlight October 22nd
# oct_22_index = selected_data[selected_data['Timestamp'].dt.date == pd.Timestamp('2018-10-22').date()].index[0]
# plt.axvline(x=selected_data.loc[oct_22_index, 'Timestamp'], color='r', linestyle='--', linewidth=2)
# plt.annotate('October 22nd', xy=(selected_data.loc[oct_22_index, 'Timestamp'], selected_data.loc[oct_22_index, 'Smoothed_PM2.5']),
#              xytext=(-100, 50), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black'))

# plt.tight_layout()
# plt.legend()
# save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Smoothed_Ozone_Time_Series.png'
# plt.savefig(save_path)

# plt.show()



import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes

# Load your CSV file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Anand_Vihar_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)

## Convert the 'From Date' column to datetime
df['From Date'] = pd.to_datetime(df['From Date'])

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


# Plot windrose
ax = WindroseAxes.from_ax()
ax.bar(selected_data['WD'], selected_data['WS'], normed=True, opening=0.8, edgecolor='white')
ax.set_legend()

# Save the figure
save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Windrose.png'
plt.savefig(save_path)

plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt

# # Load your CSV file
# data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Raw_data_15Min_2018_site_1423_Jahangirpuri_Delhi_DPCC_15Min.csv'
# df = pd.read_csv(data_path)

# # Convert the Timestamp column to datetime if it's not already in datetime format
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# # Define the central date
# central_date = pd.Timestamp('2018-10-23')

# # Find the index of the central date in the Timestamp column
# central_index = df[df['Timestamp'] == central_date].index[0]

# # Calculate the index range for 7 days before and 7 days after the central date
# start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
# end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# # Select the rows within the calculated range
# selected_data = df.iloc[start_index:end_index]

# # Remove outliers using IQR method
# Q1 = selected_data['SO2 (µg/m³)'].quantile(0.25)
# Q3 = selected_data['SO2 (µg/m³)'].quantile(0.75)
# IQR = Q3 - Q1
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR
# selected_data = selected_data[(selected_data['SO2 (µg/m³)'] >= lower_bound) & (selected_data['SO2 (µg/m³)'] <= upper_bound)]

# # Apply moving average
# window_size = 5  # Adjust window size as needed
# selected_data['Smoothed_PM2.5'] = selected_data['SO2 (µg/m³)'].rolling(window=window_size, min_periods=1).mean()

# # Plot the time series with moving average
# plt.figure(figsize=(10, 6))
# plt.plot(selected_data['Timestamp'], selected_data['Smoothed_PM2.5'], linestyle='-', label='SO2 (µg/m³)')
# plt.title('Smoothed SO2 (µg/m³) Time Series')
# plt.xlabel('Date')
# plt.ylabel('Concentration (µg/m³)')
# #plt.grid(True)
# plt.xticks(rotation=45)

# # Highlight October 22nd
# oct_22_index = selected_data[selected_data['Timestamp'].dt.date == pd.Timestamp('2018-10-22').date()].index[0]
# plt.axvline(x=selected_data.loc[oct_22_index, 'Timestamp'], color='r', linestyle='--', linewidth=2)
# plt.annotate('October 22nd', xy=(selected_data.loc[oct_22_index, 'Timestamp'], selected_data.loc[oct_22_index, 'Smoothed_PM2.5']),
#              xytext=(-100, 50), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black'))

# plt.tight_layout()
# plt.legend()
# # save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Smoothed_SO2_Time_Series.png'
# # plt.savefig(save_path)

# # plt.show()


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

# Apply moving average
window_size = 5  # Adjust window size as needed
selected_data['Smoothed_NO2'] = selected_data['NO2'].rolling(window=window_size, min_periods=1).mean()

# Plot the time series with moving average
plt.figure(figsize=(10, 6))
plt.plot(selected_data['From Date'], selected_data['Smoothed_NO2'], linestyle='-', label='NO2')
plt.title('Smoothed NO2 (µg/m³) Time Series')
plt.xlabel('Date')
plt.ylabel('Concentration (µg/m³)')
plt.xticks(rotation=45)

# Highlight April 22nd
if central_date in selected_data['From Date'].values:
    central_index = selected_data[selected_data['From Date'] == central_date].index[0]
    plt.axvline(x=selected_data.loc[central_index, 'From Date'], color='r', linestyle='--', linewidth=2)
    plt.annotate('April 22nd', xy=(selected_data.loc[central_index, 'From Date'], selected_data.loc[central_index, 'Smoothed_NO2']),
                 xytext=(-100, 50), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black'))

plt.tight_layout()
plt.legend()

# Save the plot
save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Smoothed_NO2_Time_Series_Patparganj_2024.png'
plt.savefig(save_path)

plt.show()




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

# Define the central date
central_date = pd.Timestamp('2024-04-22')

# Check if the central date exists in the DataFrame
if central_date not in df['From Date'].values:
    raise ValueError(f"The central date {central_date} is not found in the 'From Date' column of the DataFrame.")

# Find the index of the central date
central_index = df[df['From Date'] == central_date].index[0]

# Calculate the index range for 7 days before and 7 days after the central date
start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
end_index = min(len(df), central_index + 16 * 24 * 4)  # Adding 8 days after, same calculation

# Select the rows within the calculated range
selected_data = df.iloc[start_index:end_index]

# Remove outliers using the IQR method
Q1 = selected_data['PM2.5'].quantile(0.25)
Q3 = selected_data['PM2.5'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
selected_data = selected_data[(selected_data['PM2.5'] >= lower_bound) & (selected_data['PM2.5'] <= upper_bound)]

# Group the data by day
selected_data['Date'] = selected_data['From Date'].dt.date
grouped_data = selected_data.groupby('Date')['PM2.5']

# Create a DataFrame for box plots
boxplot_data = [grouped_data.get_group(date) for date in sorted(grouped_data.groups.keys())]

# Define colors
colors = ['blue' if date < pd.Timestamp('2024-04-22').date() else 'red' if date <= pd.Timestamp('2024-04-24').date() else 'green' for date in sorted(grouped_data.groups.keys())]

# Create the box-and-whisker plots
plt.figure(figsize=(12, 8))
box = plt.boxplot(boxplot_data, patch_artist=True)

# Apply colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set x-axis labels
plt.xticks(ticks=range(1, len(boxplot_data) + 1), labels=[date.strftime('%Y-%m-%d') for date in sorted(grouped_data.groups.keys())], rotation=45)
plt.xlabel('Date')
plt.ylabel('PM2.5 Concentration (µg/m³)')
plt.title('Box-and-Whisker Plots of PM2.5 Concentrations for Each Day Patparganj')
plt.tight_layout()



import pandas as pd
import matplotlib.pyplot as plt

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Anand_Vihar_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)
print(df.keys())

# Convert the 'From Date' column to datetime
df['From Date'] = pd.to_datetime(df['From Date'])

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

# Group the data by day
selected_data['Date'] = selected_data['From Date'].dt.date
grouped_data = selected_data.groupby('Date')['NO2']

# Create a DataFrame for box plots
boxplot_data = [grouped_data.get_group(date) for date in sorted(grouped_data.groups.keys())]

# Create the box-and-whisker plots
plt.figure(figsize=(12, 8))
plt.boxplot(boxplot_data, patch_artist=True)

# Set x-axis labels
plt.xticks(ticks=range(1, len(boxplot_data) + 1), labels=[date.strftime('%Y-%m-%d') for date in sorted(grouped_data.groups.keys())], rotation=45)
plt.xlabel('Date')
plt.ylabel('NO2 Concentration (µg/m³)')
plt.title('Box-and-Whisker Plots of NO2 Concentrations for Each Day')
plt.tight_layout()

# Save the plot
save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\NO2_Box_Whisker_Plots.png'
plt.savefig(save_path)

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Anand_Vihar_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)
print(df.keys())

# Convert the 'From Date' column to datetime
df['From Date'] = pd.to_datetime(df['From Date'])

# Define the central date
central_date = pd.Timestamp('2024-04-22')

# Check if the central date exists in the DataFrame
if central_date not in df['From Date'].values:
    raise ValueError(f"The central date {central_date} is not found in the 'From Date' column of the DataFrame.")

# Find the index of the central date
central_index = df[df['From Date'] == central_date].index[0]

# Calculate the index range for 7 days before and 7 days after the central date
start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
end_index = min(len(df), central_index + 16 * 24 * 4)  # Adding 8 days after, same calculation

# Select the rows within the calculated range
selected_data = df.iloc[start_index:end_index]

# Remove outliers using the IQR method
Q1 = selected_data['PM2.5'].quantile(0.25)
Q3 = selected_data['PM2.5'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
selected_data = selected_data[(selected_data['PM2.5'] >= lower_bound) & (selected_data['PM2.5'] <= upper_bound)]

# Group the data by day
selected_data['Date'] = selected_data['From Date'].dt.date
grouped_data = selected_data.groupby('Date')['PM2.5']

# Create a DataFrame for box plots
boxplot_data = [grouped_data.get_group(date) for date in sorted(grouped_data.groups.keys())]

# Define colors
colors = ['blue' if date < pd.Timestamp('2024-04-22').date() else 'red' if date <= pd.Timestamp('2024-04-24').date() else 'green' for date in sorted(grouped_data.groups.keys())]

# Create the box-and-whisker plots
plt.figure(figsize=(12, 8))
box = plt.boxplot(boxplot_data, patch_artist=True)

# Apply colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set x-axis labels
plt.xticks(ticks=range(1, len(boxplot_data) + 1), labels=[date.strftime('%Y-%m-%d') for date in sorted(grouped_data.groups.keys())], rotation=45)
plt.xlabel('Date')
plt.ylabel('PM2.5 Concentration (µg/m³)')
plt.title('Box-and-Whisker Plots of PM2.5 Concentrations for Each Day')
plt.tight_layout()

# Define custom legend
legend_patches = [
    Patch(color='blue', label='Before Fire'),
    Patch(color='red', label='During Fire'),
    Patch(color='green', label='After Fire')
]
plt.legend(handles=legend_patches, loc='upper right')

# Save the plot
#save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\PM2.5_Box_Whisker_Plots.png'
#plt.savefig(save_path)

plt.show()




import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Anand_Vihar_2024.csv'
df = pd.read_csv(data_path)

# Convert the Timestamp column to datetime if it's not already in datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Define the central date
central_date = pd.Timestamp('2024-04-22')

# Find the index of the central date in the Timestamp column
central_index = df[df['Timestamp'] == central_date].index[0]

# Calculate the index range for 7 days before and 7 days after the central date
start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# Select the rows within the calculated range
selected_data = df.iloc[start_index:end_index]

# Remove outliers using IQR method for NO2
Q1_NO2 = selected_data['NO2 (µg/m³)'].quantile(0.25)
Q3_NO2 = selected_data['NO2 (µg/m³)'].quantile(0.75)
IQR_NO2 = Q3_NO2 - Q1_NO2
lower_bound_NO2 = Q1_NO2 - 1.5 * IQR_NO2
upper_bound_NO2 = Q3_NO2 + 1.5 * IQR_NO2
selected_data = selected_data[(selected_data['NO2 (µg/m³)'] >= lower_bound_NO2) & (selected_data['NO2 (µg/m³)'] <= upper_bound_NO2)]

# Remove outliers using IQR method for NOx
Q1_NOx = selected_data['NOx (ppb)'].quantile(0.25)
Q3_NOx = selected_data['NOx (ppb)'].quantile(0.75)
IQR_NOx = Q3_NOx - Q1_NOx
lower_bound_NOx = Q1_NOx - 1.5 * IQR_NOx
upper_bound_NOx = Q3_NOx + 1.5 * IQR_NOx
selected_data = selected_data[(selected_data['NOx (ppb)'] >= lower_bound_NOx) & (selected_data['NOx (ppb)'] <= upper_bound_NOx)]

# Remove outliers using IQR method for NO
Q1_NO = selected_data['NO (µg/m³)'].quantile(0.25)
Q3_NO = selected_data['NO (µg/m³)'].quantile(0.75)
IQR_NO = Q3_NO - Q1_NO
lower_bound_NO = Q1_NO - 1.5 * IQR_NO
upper_bound_NO = Q3_NO + 1.5 * IQR_NO
selected_data = selected_data[(selected_data['NO (µg/m³)'] >= lower_bound_NO) & (selected_data['NO (µg/m³)'] <= upper_bound_NO)]

# Apply moving average for NO2
window_size = 5  # Adjust window size as needed
selected_data['Smoothed_NO2'] = selected_data['NO2 (µg/m³)'].rolling(window=window_size, min_periods=1).mean()

# Apply moving average for NOx
selected_data['Smoothed_NOx'] = selected_data['NOx (ppb)'].rolling(window=window_size, min_periods=1).mean()

# Apply moving average for NO
selected_data['Smoothed_NO'] = selected_data['NO (µg/m³)'].rolling(window=window_size, min_periods=1).mean()

# Plot the time series with moving average
plt.figure(figsize=(10, 6))
plt.plot(selected_data['Timestamp'], selected_data['Smoothed_NO2'], linestyle='-', label='NO2 (µg/m³)')
plt.plot(selected_data['Timestamp'], selected_data['Smoothed_NOx'], linestyle='-', label='NOx (ppb)')
plt.plot(selected_data['Timestamp'], selected_data['Smoothed_NO'], linestyle='-', label='NO (µg/m³)')
plt.title('Smoothed Air Pollutants Time Series')
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Highlight October 22nd
oct_22_index = selected_data[selected_data['Timestamp'].dt.date == pd.Timestamp('2018-10-22').date()].index[0]
plt.axvline(x=selected_data.loc[oct_22_index, 'Timestamp'], color='r', linestyle='--', linewidth=2)
plt.annotate('October 22nd', xy=(selected_data.loc[oct_22_index, 'Timestamp'], selected_data.loc[oct_22_index, 'Smoothed_NO2']),
             xytext=(-100, 50), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black'))

# Save and show the plot
#save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Smoothed_Air_Pollutants_Time_Series.png'
plt.savefig(save_path)
plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load your CSV file
# data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Raw_data_15Min_2018_site_1423_Jahangirpuri_Delhi_DPCC_15Min.csv'
# df = pd.read_csv(data_path)

# # Convert the Timestamp column to datetime if it's not already in datetime format
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# # Define the central date
# central_date = pd.Timestamp('2018-10-23')

# # Find the index of the central date in the Timestamp column
# central_index = df[df['Timestamp'] == central_date].index[0]

# # Calculate the index range for 7 days before and 7 days after the central date
# start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
# end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# # Select the rows within the calculated range
# selected_data = df.iloc[start_index:end_index]

# # Select relevant columns
# selected_columns = ['NO2 (µg/m³)', 'NOx (ppb)', 'NO (µg/m³)', 'PM2.5 (µg/m³)', 'NH3 (µg/m³)', 'SO2 (µg/m³)', 'CO (mg/m³)', 'Ozone (µg/m³)', 'AT (°C)', 'RH (%)']
# selected_data = selected_data[selected_columns]

# # Calculate correlation matrix
# correlation_matrix = selected_data.corr()

# # Plotting the correlation matrix
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
# plt.title('Correlation Plot')
# plt.xticks(rotation=45)
# plt.yticks(rotation=0)
# plt.tight_layout()

# # Save and show the plot
# save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Correlation_Plot.png'
# plt.savefig(save_path)
# plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load your CSV file
# data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Raw_data_15Min_2018_site_1423_Jahangirpuri_Delhi_DPCC_15Min.csv'
# df = pd.read_csv(data_path)

# # Convert the Timestamp column to datetime if it's not already in datetime format
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# # Define the central date
# central_date = pd.Timestamp('2018-10-23')

# # Find the index of the central date in the Timestamp column
# central_index = df[df['Timestamp'] == central_date].index[0]

# # Calculate the index range for 7 days before and 7 days after the central date
# start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
# end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# # Select the rows within the calculated range
# selected_data = df.iloc[start_index:end_index]

# # Plot the time series for temperature (AT) and relative humidity (RH)
# fig, ax1 = plt.subplots(figsize=(10, 6))

# color = 'tab:red'
# ax1.set_xlabel('Date')
# ax1.set_ylabel('Temperature (°C)', color=color)
# ax1.plot(selected_data['Timestamp'], selected_data['AT (°C)'], color=color)
# ax1.tick_params(axis='y', labelcolor=color)

# ax2 = ax1.twinx()  
# color = 'tab:blue'
# ax2.set_ylabel('Relative Humidity (%)', color=color)  
# ax2.plot(selected_data['Timestamp'], selected_data['RH (%)'], color=color)
# ax2.tick_params(axis='y', labelcolor=color)

# # Trend lines for temperature
# z1 = np.polyfit(selected_data.index, selected_data['AT (°C)'], 1)
# p1 = np.poly1d(z1)
# ax1.plot(selected_data['Timestamp'], p1(selected_data.index), color='orange', linestyle='-', label='Trendline (Temperature)')

# # Trend lines for relative humidity
# z2 = np.polyfit(selected_data.index, selected_data['RH (%)'], 1)
# p2 = np.poly1d(z2)
# ax2.plot(selected_data['Timestamp'], p2(selected_data.index), color='purple', linestyle='-', label='Trendline (Relative Humidity)')

# fig.tight_layout()  

# # Highlight October 22nd
# oct_22_index = selected_data[selected_data['Timestamp'].dt.date == pd.Timestamp('2018-10-22').date()].index[0]
# ax1.axvline(x=selected_data.loc[oct_22_index, 'Timestamp'], color='r', linestyle='--', linewidth=2)
# ax1.annotate('October 22nd', xy=(selected_data.loc[oct_22_index, 'Timestamp'], selected_data.loc[oct_22_index, 'AT (°C)']),
#              xytext=(-100, 50), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black'))

# # Save and show the plot
# save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2018\Temperature_RH_Time_Series_with_Trendlines.png'
# plt.savefig(save_path)
# plt.legend()
# plt.show()
