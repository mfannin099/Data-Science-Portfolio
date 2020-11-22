library('rio')
library('dplyr')
library('tidyverse')
setwd('C:\\Users\\Matt\\Desktop\\dataProjects\\tesla_stock')
#set directory using stack: https://stackoverflow.com/questions/5568847/how-to-open-csv-file-in-r-when-r-says-no-such-file-or-directory


#import data from a file
tesla <- import("TSLA.csv")
head(tesla)

#creating a data frame from file
tesla_df <- data.frame(tesla)
head(tesla_df)

#remove a column
select(tesla, -c('Adj Close'))

#set up for plot
y <- tesla_df$Close

#plots, Using the index, as Days Since IPO column
plot(y, main = "Tesla Stock Prices", ylab = "Price in US Dollars", 
     xlab = 'Days Since IPO', type = "l")

#correlation between various columns
cor(tesla$Close, tesla$Volume) #.505
cor(tesla$Open, tesla$Close) #.998

#linear regression model
model <- lm(Open ~ Close, data = tesla)
summary(model)
# r = .9978

#plot Open vs Close, with regression line shown
plot(tesla$Open, tesla$Close, ylab = "Closing Price", 
     xlab = "Opening Price", main = "Opening vs Closing", col = 'blue',
)
abline(lm(Open ~ Close, data = tesla))

# To see what comes up, when plotted
plot(model)


#More Practice with manipulation of Data frame
tesla_volume_100 <- subset(tesla_df, subset = Open >= 100)
head(tesla_volume_100)

#Moving average and plot
library('TTR')
moving_average100 <- SMA(tesla$Close, 25)
plot(moving_average100, type = 'l')

#Try to predict future price of shares, used tutorial: https://www.youtube.com/watch?v=N_XKJqr-VT4
library('MASS')
library('tseries')
library('forecast')

lnstock = log(tesla$Close[1:2400]) #training data

pricearima <- ts(lnstock, start = c(2010, 2020), frequency = 10)
fitlnstock <- auto.arima(pricearima)
fitlnstock
plot(pricearima, type = 'l')
exp(lnstock)

forvalue_ln <- forecast(fitlnstock, h = 26)
forvalue_ln
plot(forvalue_ln)
