rm(list = ls())
library(openair)

library(tidyverse)
library(lubridate)
library(ggplot2)
library(hrbrthemes)
library(xts)
library(ggpubr)
library(devtools)
library(stats)
library(psych)
library(corrplot)
library(RColorBrewer)
library(graphics)
install.packages("boxplotcluster")

# Pearson Correlation
describe(Data1$PM10)
describe(Data1$WS)
setwd("C:/Users/Hp/OneDrive/Documents/All documents/Data")
#Boxplot
boxplot(Data1$PM10 ~ Data1$Dwarka, xlab = "Dwarka sector 8", 
        ylab = "PM10 Concentrations", col = c("#999999", "#E69F00", "#56B4E9","green"))




+scale_fill_manual+values=c("#999999", "#E69F00", "#56B4E9")






p <- ggplot(Data1, aes(x=Jahangirpuri, y=PM10)) + 
  geom_boxplot()
p + theme_classic()
p + scale_fill_brewer(palette="Dark2") + theme_minimal()


p+scale_fill_manual(values=c("#999999", "#E69F00", "#56B4E9"))
p+scale_fill_brewer(palette="Dark2")
p + scale_fill_brewer(palette="Dark2") + theme_minimal()

rm(list = ls())
Data1 <- read.csv("D31c.csv",header = TRUE, sep = ",")
cor(Data1, use='complete.obs')
cor(Data1, use = 'complete.obs')

c<- cor(Data1, use = 'complete.obs')
corrplot()
corrplot(c,type = "lower")
corrplot(c, method= "circle", type = "full", order = "hclust", addCoef.col ="black", tl.col = "black", diag = FALSE)
corrplot.mixed(c, order = "hclust", type = "lower")
corr
setwd("C:/Users/Hp/OneDrive/Documents/Sampling_dataIITB/Grimm")
# Adding Data
setwd("C:/Users/Hp/OneDrive/Documents/All documents/Data")
rm(list = ls())
Data1 <- read.csv("IJ23.csv",header = TRUE, sep = ",")
windRose(Data1, ws="WS", wd="WD")

polarPlot(Data1, pollutant = "PM10",  x="WS", wd="WD", statistic = "nwr")


Data1$date <- ymd_hms(Data1$date)  #date format change



timeVariation(DataS4, pollutant = "PM10")


ggscatter(Data1, x = "PM10", y = "WS", 
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson")

is.na(cor(Data1))
na.omit(cor(Data1))

#boxplot

boxplot(Data1, main= "Boxplot", xlab="Pm10 conc.", ylab="Sites")
glimpse(Data1)
ggplot(my-, aes(x= Site, y= PM10)) + geom_boxplot(show.legend = FALSE)
       
       