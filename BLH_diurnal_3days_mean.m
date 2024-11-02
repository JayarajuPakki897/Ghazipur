% Define the path to your NetCDF file
nc_file_path = 'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\adaptor.mars.internal-1722173132.7202752-29675-6-75d58876-17ca-4df8-97b3-38b1b131e50c.nc';

% Read the NetCDF file
time = ncread(nc_file_path, 'time');
blh = ncread(nc_file_path, 'blh');
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

% Define the date ranges
date_ranges = {
    datetime(2024, 4, 19), datetime(2024, 4, 21), 'Before Landfill Fire';  % Before event
    datetime(2024, 4, 22), datetime(2024, 4, 24), 'During Landfill Fire';  % During event
    datetime(2024, 4, 25), datetime(2024, 4, 27), 'After Landfill Fire'    % After event
};

% Create figure for plots
figure;
hold on;

% Loop through each date range
for i = 1:size(date_ranges, 1)
    start_date = date_ranges{i, 1};
    end_date = date_ranges{i, 2};
    event_label = date_ranges{i, 3};
    
    % Find indices for the specified date range
    date_indices = (actual_dates >= start_date) & (actual_dates <= end_date);
    
    % Extract BLH values and corresponding times for the specified date range
    blh_selected = blh_near(date_indices);
    times_selected = actual_dates(date_indices);
    
    % Calculate the mean BLH for each hour
    hours_of_day = hour(times_selected);
    mean_blh_per_hour = arrayfun(@(h) mean(blh_selected(hours_of_day == h)), 0:23);
    
    % Plot the diurnal variation for the current date range
    plot(0:23, mean_blh_per_hour, '-o', 'DisplayName', event_label);
end

% Customize plot
xlabel('Hour of Day');
ylabel('Mean BLH (m)');
title('Diurnal Variation of Mean BLH Before, During, and After Landfill Fire');
grid on;
set(gca, 'XTick', 0:23);
xlim([0 23]);
legend;
hold off;
