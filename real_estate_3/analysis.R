library('rio')
library('tidyverse')

setwd('C:\\Users\\Matt\\Desktop\\dataProjects\\real_estate')
data <- import('real_estate_data.csv')
head(data)
cities <- data.frame(data)

#Should you rent traditionally? Or rent through Airbnb? - Airbnb makes more 
#Best cities to have a rental property in? - San Fran, Nashville, Boston, Austin, 
#What affects the income a rental property can bring in? - property value, not # of neighborhoods, have more occupants



#Comparing average rents of Airbnb vs traditional listings, for all cities. Trying out piping 
cities %>%
  summarize(airbnb_rent_avg = mean(avg_airbnb_rental), traditional_rent_avg = mean(avg_traditional_rental),
            airbnb_roi = mean(avg_airbnb_roi), traditional_roi = mean(avg_traditional_roi))

#seems that you can make 529.31 dollars more by listing on Airbnb and Airbnb's ROI is .65 higher (on average)


# Calculating how much you can make per year with rental property, and calculated time to pay off property (price / income)
cities %>%
  select(city, avg_property_price, avg_nightly_price) %>%
  mutate(income_per_year = avg_nightly_price * 365) %>%
  arrange(desc(income_per_year)) %>%
  mutate(time_to_payoff = avg_property_price / income_per_year) %>%
  head(5)
#San Fran properties make the most ($83,941), Nashville ($83,796), Boston ($78,006), Austin (71,135), and San Jose ($69,806)
#take 20.2 years, 5.6 years, 13.26, 8.84, 15.5 years to pay off the properties just using rental income for those 5 cities in order


#Biggest Investment Property Markets, traditional listings and Airbnb listings
cities %>% 
  select(city, investment_properties, airbnb_listings, traditional_listings) %>%
  mutate(total = investment_properties + airbnb_listings + traditional_listings) %>%
  arrange(desc(total)) %>%
  head(10)
#Top 10 : NYC, LA, Las Vegas, Dallas, Philly, San Antonio, Nashville, San Diego, Fort Worth, and DC


#Can you make more rental income if the property is more expensive?
t.test(cities$avg_property_price, cities$average_rental)
rental_income <- (cities$avg_airbnb_rental + cities$avg_traditional_rental) / 2
cities$average_rental <- rental_income

plot(cities$avg_property_price, cities$average_rental, ylab = "Rental Price", xlab = "Property Price", 
     main = "Property Value vs Rental Income", abline(lm(average_rental ~ avg_property_price, data = cities)))

#linear regression model
model <- lm(average_rental ~ avg_property_price, data = cities)
summary(model)

cor(cities$avg_property_price, cities$average_rental) #r = .948
#Yes, strong positive correlation to higher rental incomes when the properties' value is higher


#More Occupants, more money?
t.test(cities$avg_occupancy, cities$average_rental)
plot(cities$avg_occupancy, cities$average_rental, xlab = 'Average Rental Income', ylab = 'Average # of Guests',
     main = "Rental Income vs Number of Guests", abline(lm(average_rental ~ avg_occupancy, cities)))
cor(cities$avg_occupancy, cities$average_rental) #r = .654
summary(cities$avg_occupancy)
summary(cities$average_rental)

model <- lm(average_rental ~ avg_occupancy, cities)
model

predict_average_rental <-predict(model, data.frame(avg_occupancy = 50)) #predicts # of people who will stay at property for given rental income
predict_average_rental
#It appears the more occupants in a rental property, the more money in income it will bring in (Makes sense for Airbnb, not for traditional)


#More Neighborhoods, more competition, what does it do to prices for an overnight stay?
cor(cities$neighborhoods, cities$avg_nightly_price) #r = -.26 
t.test(cities$neighborhoods, cities$avg_nightly_price)
plot(cities$neighborhoods, cities$avg_nightly_price, xlab = 'Number of Neighborhoods', ylab = 'Nightly Rental Price',
     main = 'Competition in Rental Prices', abline(lm(cities$neighborhoods~cities$avg_nightly_price)))
cities%>% 
  select(city, neighborhoods, avg_nightly_price) %>%
  arrange(desc(neighborhoods)) %>%
  head(5)
  #Most Neighborhoods: San Antonio, Baltimore, Columbus, NYC, and Nashville

cities%>% 
  select(city, neighborhoods, avg_nightly_price) %>%
  arrange(desc(avg_nightly_price)) %>%
  head(5)
  #Highest Nightly Price: San Fran, Nashville, Boston, Austin, San Jose

#No, neighborhoods don't impact the nightly price of rentals, only one in common among top 5


#More practice with visualizations, and using different parameters 
barplot(cities$avg_property_price, names.arg = cities$city, horiz = T, las = 1, xlab = 'Average Price of Property')
boxplot(cities$avg_property_price, ylab = 'Average Price of Property')
