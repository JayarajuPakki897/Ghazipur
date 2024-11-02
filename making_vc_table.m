% Define the path to your NetCDF file and Excel file
nc_file_path = 'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\adaptor.mars.internal-1722173132.7202752-29675-6-75d58876-17ca-4df8-97b3-38b1b131e50c.nc';
excel_file_path = 'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx';

% Read the NetCDF file
time = ncread(nc_file_path, 'time');
blh = ncread(nc_file_path, 'blh');
u10 = ncread(nc_file_path, 'u10');
v10 = ncread(nc_file_path, 'v10');
lon = ncread(nc_file_path, 'longitude');
lat = ncread(nc_file_path, 'latitude');

% Define the base date
base_date = datetime(1900, 1, 1);

% Convert numeric dates to actual dates based on the units (hours since base date)
actual_dates = base_date + hours(time);

% Define the specific location Ghazipur
target_lat = 28.62537167346769;
target_lon = 77.32814453048788;

% Find the nearest grid points
[~, lat_idx] = min(abs(lat - target_lat));
[~, lon_idx] = min(abs(lon - target_lon));

% Select the expver level (1)
expver_idx = 1;

% Extract BLH values for the nearest grid points and expver = 1
blh_near = squeeze(blh(lon_idx, lat_idx, expver_idx, :));

% Extract wind components for the nearest grid points and expver = 1
u10_near = squeeze(u10(lon_idx, lat_idx, expver_idx, :));
v10_near = squeeze(v10(lon_idx, lat_idx, expver_idx, :));

% Calculate wind speed
wind_speed_near = sqrt(u10_near.^2 + v10_near.^2);

% Calculate the Ventilation Coefficient (VC)
ventilation_coefficient = blh_near .* wind_speed_near;

% Create a table for the entire NetCDF dataset
netcdf_table = table(actual_dates, blh_near, wind_speed_near, ventilation_coefficient, ...
                     'VariableNames', {'Date', 'BLH', 'WindSpeed', 'VentilationCoefficient'});

% Read the data from the Excel file
excel_data = readtable(excel_file_path, 'Sheet', 2);

% Convert the 'From Date' column to datetime
excel_data.FromDate = datetime(excel_data.FromDate, 'InputFormat', 'dd-MM-yyyy HH:mm', 'Format', 'yyyy-MM-dd HH:mm:ss');

% Remove rows with NaN values in the relevant columns
excel_data = rmmissing(excel_data, 'DataVariables', {'PM2_5', 'PM10', 'Toluene', 'Benzene', 'Ozone'});

% Convert table to timetable for resampling
excel_timetable = table2timetable(excel_data(:, {'FromDate', 'PM2_5', 'PM10', 'Toluene', 'Benzene', 'Ozone'}), 'RowTimes', 'FromDate');

% Resample the data to hourly resolution, taking the mean
resampled_timetable = retime(excel_timetable, 'hourly', 'mean');

% Convert the timetable back to a table
resampled_table = timetable2table(resampled_timetable);

% Rename columns to match with netcdf_table
resampled_table.Properties.VariableNames = {'Date', 'PM25', 'PM10', 'Toluene', 'Benzene', 'Ozone'};

% Merge the NetCDF table and resampled pollutant data based on dates
combined_table = outerjoin(netcdf_table, resampled_table, 'Keys', 'Date', 'MergeKeys', true);

% Remove rows with NaN values in PM2.5, PM10, Toluene, Benzene, Ozone, BLH, WindSpeed, or VentilationCoefficient
combined_table = rmmissing(combined_table);

% Calculate adjusted values (Pollutant / VentilationCoefficient)
combined_table.AdjustedPM25 = combined_table.PM25 ./ combined_table.VentilationCoefficient;
combined_table.AdjustedPM10 = combined_table.PM10 ./ combined_table.VentilationCoefficient;
combined_table.AdjustedToluene = combined_table.Toluene ./ combined_table.VentilationCoefficient;
combined_table.AdjustedBenzene = combined_table.Benzene ./ combined_table.VentilationCoefficient;
combined_table.AdjustedOzone = combined_table.Ozone ./ combined_table.VentilationCoefficient;

% Display the combined table
disp(combined_table);

% Save the combined table to a CSV file
output_file_path = 'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\combined_ventilation_coefficient_data.csv';
writetable(combined_table, output_file_path);

% Plot time series for Adjusted PM2.5, PM10, Toluene, Benzene, and Ozone
figure;

% Plot Adjusted PM2.5
subplot(3, 2, 1);
plot(combined_table.Date, combined_table.AdjustedPM25, '-o', 'DisplayName', 'Adjusted PM2.5');
xlabel('Date');
ylabel('Adjusted PM2.5');
title('Time Series of Adjusted PM2.5');
grid on;
legend;

% Plot Adjusted PM10
subplot(3, 2, 2);
plot(combined_table.Date, combined_table.AdjustedPM10, '-o', 'DisplayName', 'Adjusted PM10');
xlabel('Date');
ylabel('Adjusted PM10');
title('Time Series of Adjusted PM10');
grid on;
legend;

% Plot Adjusted Toluene
subplot(3, 2, 3);
plot(combined_table.Date, combined_table.AdjustedToluene, '-o', 'DisplayName', 'Adjusted Toluene');
xlabel('Date');
ylabel('Adjusted Toluene');
title('Time Series of Adjusted Toluene');
grid on;
legend;

% Plot Adjusted Benzene
subplot(3, 2, 4);
plot(combined_table.Date, combined_table.AdjustedBenzene, '-o', 'DisplayName', 'Adjusted Benzene');
xlabel('Date');
ylabel('Adjusted Benzene');
title('Time Series of Adjusted Benzene');
grid on;
legend;

% Plot Adjusted Ozone
subplot(3, 2, 5);
plot(combined_table.Date, combined_table.AdjustedOzone, '-o', 'DisplayName', 'Adjusted Ozone');
xlabel('Date');
ylabel('Adjusted Ozone');
title('Time Series of Adjusted Ozone');
grid on;
legend;

% Adjust layout
tight_layout;
