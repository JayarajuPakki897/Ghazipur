import pandas as pd
import matplotlib.pyplot as plt

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)

# Convert the 'From Date' column to datetime with the correct format
df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# Create the necessary columns
df['VOCs'] = df['Benzene'] + df['Toluene']
df['ratio'] = df['NOx'] / df['VOCs']

# Define the central date
central_date = pd.Timestamp('2024-04-22')

# Check if the central date exists in the DataFrame
if central_date not in df['From Date'].values:
    raise ValueError(f"The central date {central_date} is not found in the 'From Date' column of the DataFrame.")

# Find the index of the central date
central_index = df[df['From Date'] == central_date].index[0]

# Calculate the index range for 7 days before and 8 days after the central date
start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# Slice the DataFrame to get the desired date range
df_subset = df.iloc[start_index:end_index]

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot Ozone on the left Y-axis
ax1.plot(df_subset['From Date'], df_subset['Ozone'], color='blue', label='Ozone')
ax1.set_xlabel('Date')
ax1.set_ylabel('Ozone (ppb)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis for the ratio
ax2 = ax1.twinx()
ax2.plot(df_subset['From Date'], df_subset['ratio'], color='red', label='NOx/VOCs Ratio')
ax2.set_ylabel('NOx/VOCs Ratio', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add vertical line to indicate the fire event
ax1.axvline(central_date, color='green', linestyle='--', label='Fire Event')

# Adding legends
fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))

# Improving the layout
fig.tight_layout()

# Show plot
plt.title('Time Series of Ozone and NOx/VOCs Ratio with Fire Event on April 22, 2024')
# diurnal_save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\NOX_by_VOCs_Vs_Ozone.png'
# plt.savefig(diurnal_save_path)
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)

# Convert the 'From Date' column to datetime with the correct format
df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# Create the necessary columns
df['VOCs'] = df['Benzene'] + df['Toluene']
df['ratio'] = df['NOx'] / df['VOCs']

# Define the central date
central_date = pd.Timestamp('2024-04-22')

# Check if the central date exists in the DataFrame
if central_date not in df['From Date'].values:
    raise ValueError(f"The central date {central_date} is not found in the 'From Date' column of the DataFrame.")

# Find the index of the central date
central_index = df[df['From Date'] == central_date].index[0]

# Calculate the index range for 7 days before and 8 days after the central date
start_index = max(0, central_index - 7 * 24 * 4)  # 24 hours * 4 (4 intervals per hour)
end_index = min(len(df), central_index + 8 * 24 * 4)  # Adding 8 days after, same calculation

# Slice the DataFrame to get the desired date range
df_subset = df.iloc[start_index:end_index]

# Define the columns of interest
columns_of_interest = [
    'PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'SO2', 'CO', 'Ozone', 
    'Benzene', 'Toluene', 'RH', 'WS', 'WD', 'SR', 'BP',  'AT', 'RF'
]

# Calculate the correlation matrix for the specified columns within the date range
correlation_matrix = df_subset[columns_of_interest].corr()

# Plotting the heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix for Selected Columns (7 days before and 8 days after April 22, 2024)')
diurnal_save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Correlation_plot.png'
plt.savefig(diurnal_save_path)
plt.show()
