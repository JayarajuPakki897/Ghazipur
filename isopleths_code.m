% Define the NetCDF file path
filename = 'FR0020R.20150101100028.20170731000000.ads_tube..air.20mo.34h.FR01L_PerkinElmer.FR01L_NMHC_analysis.lev2.nc';

% Define base time
base_time = datetime(1900, 1, 1, 0, 0, 0); % Base time for conversion

% Get information about the NetCDF file
info = ncinfo(filename);

% Initialize cell arrays for variable names
amean_vars = {};
time_var = 'time';  % Name of the time variable

% Loop through all variables in the NetCDF file
for i = 1:length(info.Variables)
    var_name = info.Variables(i).Name;
    % Check if the variable name ends with '_amean'
    if endsWith(var_name, '_amean')
        amean_vars{end+1} = var_name; % Append to the list
    end
end

% Display the variable names ending with '_amean'
disp('Variables ending with ''_amean'':');
disp(amean_vars);

% Initialize a structure to hold the data arrays
data_arrays = struct();

% Function to sanitize field names
sanitize_field_name = @(name) matlab.lang.makeValidName(name);

% Add the 'time' variable to the structure
if ismember(time_var, {info.Variables.Name})
    % Read the 'time' variable data
    time_data = ncread(filename, time_var);
    % Convert time data to datetime format
    % Assuming 'time' is in days since the base time
    time_dates = base_time + days(time_data);
    
    % Sanitize the variable name
    valid_time_var_name = sanitize_field_name(time_var);
    % Store the 'time' data in the structure
    data_arrays.(valid_time_var_name) = time_dates;
end

% Loop through the list of '_amean' variables
for i = 1:length(amean_vars)
    var_name = amean_vars{i};
    % Sanitize the variable name to make it a valid field name
    valid_field_name = sanitize_field_name(var_name);
    % Read the variable data from the NetCDF file
    data = ncread(filename, var_name);
    % Store the data array in the structure with a valid field name
    data_arrays.(valid_field_name) = data;
end

% Display the field names (variable names) in the structure
disp('Data arrays loaded:');
disp(fieldnames(data_arrays));


data_table = struct2table(data_arrays);

csv_filename = 'VOCs_mean_data_arrays.csv';

% Write the table to a CSV file
writetable(data_table, csv_filename);

disp(['Data successfully saved to ', csv_filename]);