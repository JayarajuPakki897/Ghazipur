import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem, t

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)

# Convert the 'From Date' column to datetime with the correct format
df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

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

# Filter the DataFrame for the selected time period
filtered_df = df.iloc[start_index:end_index]

# Drop rows with NaN values
filtered_df = filtered_df.dropna(subset=['PM2.5'])

# Create a new column for the date without time
filtered_df['Date'] = filtered_df['From Date'].dt.date

# Group by the new date column and calculate daily mean and confidence intervals
grouped = filtered_df.groupby('Date')['PM2.5']

daily_mean = grouped.mean()
daily_count = grouped.count()
daily_std_err = grouped.apply(sem)
confidence_interval = daily_std_err * t.ppf((1 + 0.95) / 2, daily_count - 1)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(daily_mean.index, daily_mean, label='Daily Mean of PM2.5', color='blue')
plt.fill_between(daily_mean.index, daily_mean - confidence_interval, daily_mean + confidence_interval, 
                 color='lightblue', alpha=0.5, label='95% Confidence Interval')

# Highlight the fire event date
plt.axvline(central_date.date(), color='red', linestyle='--', linewidth=1.5, label='Fire Event')
plt.text(central_date.date(), plt.ylim()[1]*0.9, 'Fire Event', color='red', horizontalalignment='right')

plt.xlabel('Date')
plt.ylabel('PM2.5')
plt.title('Daily Mean PM2.5 with 95% Confidence Interval')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
# diurnal_save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\PM25WITHci95.png'
# plt.savefig(diurnal_save_path)
# plt.show()




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem, t

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)

# Convert the 'From Date' column to datetime with the correct format
df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# Drop rows with NaN values in PM2.5
df = df.dropna(subset=['PM2.5'])

# Create a new column for the date without time
df['Date'] = df['From Date'].dt.date

# Group by the new date column and calculate daily mean and confidence intervals
grouped = df.groupby('Date')['PM2.5']

daily_mean = grouped.mean()
daily_count = grouped.count()
daily_std_err = grouped.apply(sem)
confidence_interval = daily_std_err * t.ppf((1 + 0.95) / 2, daily_count - 1)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(daily_mean.index, daily_mean, label='Daily Mean of PM2.5', color='blue')
plt.fill_between(daily_mean.index, daily_mean - confidence_interval, daily_mean + confidence_interval, 
                 color='lightblue', alpha=0.5, label='95% Confidence Interval')

# Highlight the fire event date range (21st April to 23rd April)
fire_start = pd.Timestamp('2024-04-21')
fire_end = pd.Timestamp('2024-04-23')

plt.axvspan(fire_start, fire_end, color='red', alpha=0.3, label='Fire Event')

plt.xlabel('Date')
plt.ylabel('PM2.5')
plt.title('Daily Mean PM2.5 with 95% Confidence Interval')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
# diurnal_save_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\PM25WITHci95INsummer.png'
# plt.savefig(diurnal_save_path)
# plt.show()





import pandas as pd
import matplotlib.pyplot as plt

# Load your Excel data (assuming 'From Date' and 'Wind Direction' columns exist)
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx'
df = pd.read_excel(data_path, sheet_name=1)

# Assuming 'Wind Direction' is a categorical column indicating wind direction
# Example: 'Wind Direction' column should contain categories like 'N', 'NE', 'E', etc.

# Calculate frequency of counts by wind direction
wind_direction_counts = df['WD'].value_counts(normalize=True) * 100  # Convert to percentage

# Plotting the results
plt.figure(figsize=(8, 6))
wind_direction_counts.plot(kind='bar', color='skyblue')
plt.title('Frequency of Counts by Wind Direction (%)')
plt.xlabel('Wind Direction')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
