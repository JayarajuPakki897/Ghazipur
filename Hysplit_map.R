# Install necessary packages if not already installed
if (!requireNamespace("devtools", quietly = TRUE)) {
  install.packages("devtools")
}

if (!requireNamespace("splitr", quietly = TRUE)) {
  devtools::install_github("rich-iannone/splitr")
}

if (!requireNamespace("tidyverse", quietly = TRUE)) {
  install.packages("tidyverse")
}

if (!requireNamespace("leaflet", quietly = TRUE)) {
  install.packages("leaflet")
}

# Load necessary libraries
library(splitr)
library(tidyverse)
library(leaflet)

# Set the temporary directory for storing downloaded files
temp_dir <- tempdir()

# Create the HYSPLIT Particle Dispersion Model
dispersion_model_20 <- create_dispersion_model() %>%
  add_source(
    name = "particle", 
    lat = 28.626002819070532, lon = 77.32790847910893, height = 5,
    rate = 72.08, pdiam = 2.5, density = 1.5, shape_factor = 0.6,
    release_start = lubridate::ymd_hm("2024-04-22 10:00"),
    release_end = lubridate::ymd_hm("2024-04-25 19:00")
  ) %>%
  add_dispersion_params(
    start_time = lubridate::ymd_hm("2024-04-22 10:00"),
    end_time = lubridate::ymd_hm("2024-04-25 19:00"), 
    direction = "forward", 
    met_type = "gdas1",
    met_dir = temp_dir,  # Set the temporary directory
    exec_dir = temp_dir
  ) %>%
  run_model()

# Extract the Dispersion Data Table
dispersion_tbl_20 <- dispersion_model_20 %>% get_output_tbl()

# Create a function to plot the dispersion map
dispersion_plot_new <- function(x, color_scheme = "cycle_hues") {
  # Function code (same as before)
}

# Run the plot function to create the map
dispersion_plot_new(dispersion_tbl_20)
