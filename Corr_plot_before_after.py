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
                       'Benzene', 'Toluene', 'RH', 'WS', 'WD', 'SR', 'BP', 
                       'AT']
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
    plt.show()
