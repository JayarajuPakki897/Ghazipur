# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load the specific sheet from the Excel file
# data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
# df = pd.read_excel(data_path, sheet_name=1)
# print(df.keys())

# # Convert the 'From Date' column to datetime with the correct format
# df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# # Define the date ranges
# before_fire_start = pd.Timestamp('2024-04-15')
# before_fire_end = pd.Timestamp('2024-04-21')
# during_fire_start = pd.Timestamp('2024-04-22')
# during_fire_end = pd.Timestamp('2024-04-24')
# after_fire_start = pd.Timestamp('2024-04-25')
# after_fire_end = pd.Timestamp('2024-05-10')

# # Filter the data for each period
# before_fire_data = df[(df['From Date'] >= before_fire_start) & (df['From Date'] <= before_fire_end)]
# during_fire_data = df[(df['From Date'] >= during_fire_start) & (df['From Date'] <= during_fire_end)]
# after_fire_data = df[(df['From Date'] >= after_fire_start) & (df['From Date'] <= after_fire_end)]

# # Function to remove outliers using the IQR method
# def remove_outliers(data, column):
#     Q1 = data[column].quantile(0.25)
#     Q3 = data[column].quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#     return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# # Function to plot diurnal patterns for a given dataset
# def plot_diurnal(data, period_name):
#     # Remove NaNs
#     data = data.dropna(subset=['Ozone', 'Benzene', 'Toluene'])
    
#     # Remove outliers
#     data = remove_outliers(data, 'Ozone')
#     data = remove_outliers(data, 'Benzene')
#     data = remove_outliers(data, 'Toluene')

#     # Extract the hour from the 'From Date' column
#     data['Hour'] = data['From Date'].dt.hour

#     # Group by the hour of the day and calculate the mean and standard deviation of concentrations
#     diurnal_data_ozone = data.groupby('Hour')['Ozone'].agg(['mean', 'std'])
#     diurnal_data_benzene = data.groupby('Hour')['Benzene'].agg(['mean', 'std'])
#     diurnal_data_toluene = data.groupby('Hour')['Toluene'].agg(['mean', 'std'])

#     # Apply rolling mean to smooth the data
#     diurnal_data_ozone['mean_smooth'] = diurnal_data_ozone['mean'].rolling(window=3, center=True).mean()
#     diurnal_data_benzene['mean_smooth'] = diurnal_data_benzene['mean'].rolling(window=3, center=True).mean()
#     diurnal_data_toluene['mean_smooth'] = diurnal_data_toluene['mean'].rolling(window=3, center=True).mean()

#     fig, ax1 = plt.subplots(figsize=(10, 6))

#     # Plot Ozone on the left y-axis
#     ax1.plot(diurnal_data_ozone.index, diurnal_data_ozone['mean_smooth'], 'o-', label='Ozone', color='black')
#     ax1.set_xlabel('Hour of the Day')
#     ax1.set_ylabel('Mean Ozone Concentration (µg/m³)')
#     ax1.tick_params(axis='y', labelcolor='black')
#     ax1.spines['left'].set_color('black')
#     # ax1.spines['left'].set_linewidth(2)  # Make the vertical line more prominent

#     # Create a secondary y-axis for Benzene
#     ax2 = ax1.twinx()
#     ax2.plot(diurnal_data_benzene.index, diurnal_data_benzene['mean_smooth'], 'o-', label='Benzene', color='green')
#     ax2.set_ylabel('Mean Benzene Concentration (µg/m³)', color='green')
#     ax2.tick_params(axis='y', labelcolor='green')
#     ax2.spines['right'].set_color('green')

#     # Create a tertiary y-axis for Toluene
#     ax3 = ax1.twinx()
#     ax3.spines['right'].set_position(('outward', 60))  # Move the third axis outwards
#     ax3.plot(diurnal_data_toluene.index, diurnal_data_toluene['mean_smooth'], 'o-', label='Toluene', color='red')
#     ax3.set_ylabel('Mean Toluene Concentration (µg/m³)', color='red')
#     ax3.tick_params(axis='y', labelcolor='red')
#     ax3.spines['right'].set_color('red')

#     # Combine legends from all axes
#     lines, labels = ax1.get_legend_handles_labels()
#     lines2, labels2 = ax2.get_legend_handles_labels()
#     lines3, labels3 = ax3.get_legend_handles_labels()
#     ax1.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc='upper left')

#     plt.title(f'Diurnal Pattern of Ozone, Benzene, and Toluene Concentrations (µg/m³) - {period_name}')
#     plt.xticks(range(0, 24))

#     # Save the combined diurnal plot with high resolution
#     diurnal_save_path = f'F:\\Ph.D\\Project_Landfill_fires\\Data\\2024\\Ghazipur\\Diurnal_Ozone_Benzene_Toluene_{period_name}_Patparganj_2024.png'
#     plt.savefig(diurnal_save_path, dpi=300, bbox_inches='tight')

#     plt.show()

# # Plot diurnal patterns for each period
# plot_diurnal(before_fire_data, 'Before_Fire')
# plot_diurnal(during_fire_data, 'During_Fire')
# plot_diurnal(after_fire_data, 'After_Fire')






import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)

# Print the column names to verify
print(df.columns)

# Convert the 'From Date' column to datetime with the correct format
df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# Define the date ranges for before, during, and after
date_ranges = {
    'Before': ('2024-04-15', '2024-04-21'),
    'During': ('2024-04-22', '2024-04-24'),
    'After': ('2024-04-25', '2024-05-05')
}

# Define the columns of interest
columns_of_interest = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'SO2', 'CO', 'Ozone', 
                       'Benzene', 'Toluene', 'RH', 'SR', 'AT']

# Filter the data according to the date ranges and plot correlation heatmaps
for period, (start_date, end_date) in date_ranges.items():
    mask = (df['From Date'] >= start_date) & (df['From Date'] <= end_date)
    df_period = df.loc[mask, columns_of_interest]
    
    # Calculate correlation matrix
    corr_matrix = df_period.corr()
    
    # Plot heatmap
    plt.figure(figsize=(14, 12))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(f'Correlation Heatmap - {period} Fire')
    
    # Save the plot to a file
    plt.savefig(f'correlation_heatmap_{period}.png')
    
    # Display the plot
    plt.show()
