# Clear workspace and load necessary libraries
rm(list = ls())

# Define necessary packages for installation and loading
packages <- c(
  "tidyverse", "lubridate", "openair", "gdata", "readxl"
)

# Install packages if not already installed
install.packages(packages)

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
csv_file_path <- "F:/Ph.D/Project_Landfill_fires/Data/2024/Ghazipur/updated_combined_data.csv"

# Read the CSV file
Data1 <- read_csv(csv_file_path)
Data1 <- na.omit(Data1)

# Clean data by removing rows with NA values
unique_values <- unique(Data1$ExcelWindDirection)
print(unique_values)


# Convert necessary columns to numeric and date/time formats
Data1$WS <- as.numeric(as.character(Data1$ExcelWindSpeed))
Data1 <- na.omit(Data1)

Data1$WD <- as.numeric(as.character(Data1$ExcelWindDirection))
Data1 <- na.omit(Data1)

Data1$PM10 <- as.numeric(as.character(Data1$AdjustedPM10))
Data1 <- na.omit(Data1)

Data1$PM2.5 <- as.numeric(as.character(Data1$AdjustedPM25))
Data1 <- na.omit(Data1)

# Print structure of Data1 to check if everything is correctly read and converted
str(Data1)

png(filename = "polar_plot_ADJPM10.png", width = 800, height = 600)
par(cex.main = 2, cex.lab = 1.5, cex.axis = 1.5, cex = 1.5)
polarPlot(Data1, pollutant = "PM10", x = "WS", wd = "WD", statistic = "nwr",
          main = "Polar Plot for PM10")
dev.off()

# Save polar plot for PM2.5 as PNG
png(filename = "polar_plot_ADJPM2.5.png", width = 800, height = 600)
par(cex.main = 2, cex.lab = 1.5, cex.axis = 1.5, cex = 1.5)
polarPlot(Data1, pollutant = "PM2.5", x = "WS", wd = "WD", statistic = "nwr",
          main = "Polar Plot for PM2.5")
dev.off()
