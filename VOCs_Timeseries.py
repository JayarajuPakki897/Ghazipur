import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Load the specific sheet from the Excel file
data_path = r'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Sector_1_Noida_UPPCB.xlsx'
df = pd.read_excel(data_path, sheet_name=1)

# Convert the 'From Date' column to datetime with the correct format
df['From Date'] = pd.to_datetime(df['From Date'], format='%d-%m-%Y %H:%M', dayfirst=True)

# Remove NaN values
df.dropna(subset=['Benzene', 'Toluene', 'PM2.5'], inplace=True)

# Calculate VOCs (sum of Benzene and Toluene)
df['VOCs'] = df['Benzene'] + df['Toluene']

# Resample to daily means
df.set_index('From Date', inplace=True)
daily_mean = df.resample('D')['PM2.5'].mean()
daily_std = df.resample('D')['PM2.5'].std()
daily_count = df.resample('D')['PM2.5'].count()

# Calculate the 95% confidence intervals
confidence_level = 0.95
degrees_freedom = daily_count - 1
confidence_interval = stats.t.ppf((1 + confidence_level) / 2, degrees_freedom)
margin_of_error = daily_std / np.sqrt(daily_count) * confidence_interval

# Plotting the time series with 95% confidence intervals
plt.figure(figsize=(12, 6))
plt.plot(daily_mean.index, daily_mean, linestyle='-', color='b', label='Daily Mean PM2.5')
plt.fill_between(daily_mean.index, daily_mean - margin_of_error, daily_mean + margin_of_error, color='b', alpha=0.2, label='95% Confidence Interval')

# Highlight fire days (22nd, 23rd, and 24th of April)
fire_dates = pd.to_datetime(['2024-04-22', '2024-04-23', '2024-04-24'])
plt.axvspan(fire_dates[0], fire_dates[-1], color='red', alpha=0.3, label='Fire Days')

plt.title('Daily Mean Time Series of PM2.5 with 95% Confidence Intervals at Sector_1_Noida_UPPCB')
plt.xlabel('Date')
plt.ylabel('Concentration ($\mu$g/m^3$)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
#plt.grid(True)

# Save plot as an image file (optional)
plt.savefig('PM2.5_Time_Series_Confidence_Intervals_Sector_1_Noida_UPPCB.png')

plt.show()
