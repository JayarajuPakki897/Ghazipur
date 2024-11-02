# Clear workspace and load necessary libraries
rm(list = ls())

# Define necessary packages for installation and loading
packages <- c("tidyverse", "lubridate", "openair", "gdata", "readxl", "readr")

# Install packages if not already installed
installed_packages <- rownames(installed.packages())
for (pkg in packages) {
  if (!(pkg %in% installed_packages)) {
    install.packages(pkg, dependencies = TRUE)
  }
}

# Load required libraries
library(tidyverse)
library(lubridate)
library(openair)
library(gdata)
library(readxl)
library(readr)

# Set working directory
setwd("F:/Ph.D/Project_Landfill_fires/Data/2024/Ghazipur")

# Read Excel file, assuming it has multiple sheets and you want the second sheet
xl_file_path <- "F:/Ph.D/Project_Landfill_fires/Data/2024/Ghazipur/Patparganj_2024.xlsx"

# Read the second sheet from the Excel file
Data1 <- read_xlsx(xl_file_path, sheet = 2)

# Convert 'From Date' column to POSIXct date-time format
Data1 <- Data1 %>%
  mutate(`From Date` = dmy_hm(`From Date`))

# Define the periods for before, during, and after the fire
before_fire <- Data1 %>%
  filter(`From Date` >= as.POSIXct("2024-04-19") & `From Date` < as.POSIXct("2024-04-22"))

during_fire <- Data1 %>%
  filter(`From Date` >= as.POSIXct("2024-04-22") & `From Date` < as.POSIXct("2024-04-25"))

after_fire <- Data1 %>%
  filter(`From Date` >= as.POSIXct("2024-04-25") & `From Date` < as.POSIXct("2024-04-28"))

# Function to convert necessary columns to numeric and handle NA values
prepare_data <- function(data) {
  data <- data %>%
    mutate(
      WS = as.numeric(as.character(WS)),
      WD = as.numeric(as.character(WD)),
      PM10 = as.numeric(as.character(PM10)),
      PM2.5 = as.numeric(as.character(PM2.5))
    ) %>%
    na.omit()
  return(data)
}

# Prepare data for each period
before_fire <- prepare_data(before_fire)
during_fire <- prepare_data(during_fire)
after_fire <- prepare_data(after_fire)

# Function to save polar plots as PNG with bold labels and high resolution
save_polar_plot <- function(data, pollutant, period, filename) {
  png(filename = filename, width = 1600, height = 1200, res = 300)
  par(cex.main = 2, cex.lab = 1.5, cex.axis = 1.5, cex = 1.5, font = 2)  # Bold font
  polarPlot(data, pollutant = pollutant, x = "WS", wd = "WD", statistic = "nwr",
            key.header = pollutant, key.footer = expression(paste("[µg/m"^3, "]")),
            main = paste(pollutant, period, "Fire"), font.main = 2, font.lab = 2, font.axis = 2)
  dev.off()
}

# Save polar plots for PM10
save_polar_plot(before_fire, "PM10", "Before", "polar_plot_PM10_before_fire.png")
save_polar_plot(during_fire, "PM10", "During", "polar_plot_PM10_during_fire.png")
save_polar_plot(after_fire, "PM10", "After", "polar_plot_PM10_after_fire.png")

# Save polar plots for PM2.5
save_polar_plot(before_fire, "PM2.5", "Before", "polar_plot_PM2.5_before_fire.png")
save_polar_plot(during_fire, "PM2.5", "During", "polar_plot_PM2.5_during_fire.png")
save_polar_plot(after_fire, "PM2.5", "After", "polar_plot_PM2.5_after_fire.png")
