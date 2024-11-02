filen='adaptor.mars.internal-1722173132.7202752-29675-6-75d58876-17ca-4df8-97b3-38b1b131e50c.nc';
% Define the path to your NetCDF file and shapefile
nc_file_path = 'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\adaptor.mars.internal-1722173132.7202752-29675-6-75d58876-17ca-4df8-97b3-38b1b131e50c.nc';
shapefile_path = 'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\India_Shape\india_st.shx';

% Read the NetCDF file
time = ncread(nc_file_path, 'time');
blh = ncread(nc_file_path, 'blh');
lon = ncread(nc_file_path, 'longitude');
lat = ncread(nc_file_path, 'latitude');

% Define the base date
base_date = datetime(1900, 1, 1);

% Convert numeric dates to actual dates based on the units (hours since base date)
actual_dates = base_date + hours(time);

% Select a specific time step (e.g., the first one)
time_step = 1;
expver_index = 1;  % Selecting the first index for expver

% Extract the BLH data for the specific time step and first expver level
blh_selected = squeeze(blh(:, :, expver_index, time_step));

% Create the plot
figure;
mymap = pcolor(lon, lat, blh_selected.');
mymap.EdgeAlpha = 0; % Remove edges for a smoother look
colorbar;
colormap jet(256);
hold on;

% Overlay the shapefile of India
shp = shaperead(shapefile_path);
mapshow(shp, 'FaceColor', 'none', 'EdgeColor', 'k'); % Show shapefile with black edges

% Add a marker for the specific location
marker_lat = 28.62537167346769;
marker_lon = 77.32814453048788;
plot(marker_lon, marker_lat, 'ro', 'MarkerSize', 8, 'LineWidth', 2); % Red circle marker

% Set plot limits (optional)
% ylim([4.5 36.5]);
% xlim([66.5 97.5]);

% Set color limits (optional)
% caxis([0 50]);

% Add labels and title
xlabel('Longitude');
ylabel('Latitude');
ylabel(colorbar, 'BLH (m)', 'FontSize', 15);
title(['Boundary Layer Height (BLH) for ', datestr(actual_dates(time_step))]);

% Additional plot settings
set(gca, 'FontSize', 12);
hold off;


filen = 'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\adaptor.mars.internal-1722173132.7202752-29675-6-75d58876-17ca-4df8-97b3-38b1b131e50c.nc';

% Read the NetCDF file
lon = ncread(filen, 'longitude');
lat = ncread(filen, 'latitude');
u10 = ncread(filen, 'u10');
v10 = ncread(filen, 'v10');
time = ncread(filen, 'time');

% Define the base date
base_date = datetime(1900, 1, 1);
actual_dates = base_date + hours(time);

% Define the specific location
target_lat = 28.62537167346769;
target_lon = 77.32814453048788;

% Find the nearest grid points
[~, lat_idx] = min(abs(lat - target_lat));
[~, lon_idx] = min(abs(lon - target_lon));

% Select the expver level (1)
expver_idx = 1;

% Extract u10 and v10 values for the nearest grid points and expver = 1
u10_near = squeeze(u10(lon_idx, lat_idx, expver_idx, :));
v10_near = squeeze(v10(lon_idx, lat_idx, expver_idx, :));

% Calculate the average values for each hour (since only one point, average is the value itself)
u10_avg = u10_near; % no need to average since it's a single point
v10_avg = v10_near; % no need to average since it's a single point
blh_near = squeeze(blh(lon_idx, lat_idx, expver_idx, :));

wind_speed = sqrt(u10_near.^2 + v10_near.^2);
wind_direction = mod(atan2d(u10_near, v10_near) + 180, 360);
vc = blh_near .* wind_speed;

% Display the results with the corresponding dates
for i = 1:length(actual_dates)
    fprintf('Date: %s, Average u10: %.2f, Average v10: %.2f\n', datestr(actual_dates(i)), u10_avg(i), v10_avg(i));
end






% Define the path to your Excel file
data_path = 'F:\Ph.D\Project_Landfill_fires\Data\2024\Ghazipur\Patparganj_2024.xlsx';

% Read the data from the specified sheet (sheet index 1) as a table
data_table = readtable(data_path, 'Sheet', 1);

% Display the first few rows of the table to verify the contents
disp(data_table(1:5, :));

% Extract 'From Date' and 'To Date' columns as cell arrays
from_date_col = data_table.PrescribedStandards;
to_date_col = data_table.Var2;

% Convert 'From Date' and 'To Date' columns to datetime format
from_dates = datetime(from_date_col, 'InputFormat', 'dd-MM-yyyy HH:mm');
to_dates = datetime(to_date_col, 'InputFormat', 'dd-MM-yyyy HH:mm');

% Read the NetCDF file and extract the time variable
time = ncread(nc_file_path, 'time');

% Define the base date
base_date = datetime(1900, 1, 1);

% Convert numeric dates to actual dates based on the units (hours since base date)
actual_dates = base_date + hours(time);

% Display the first few rows of the date columns and actual dates
disp('From Dates:');
disp(from_dates(1:5));
disp('To Dates:');
disp(to_dates(1:5));
disp('Actual Dates from NetCDF:');
disp(actual_dates(1:5));

% Match the dates between Excel and NetCDF
matching_indices = ismember(actual_dates, from_dates);

% Display matching dates and their indices
disp('Matching Dates:');
disp(actual_dates(matching_indices));
disp('Indices of Matching Dates:');
disp(find(matching_indices));


excell_ws=data_table.NA_2;