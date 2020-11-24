**Data Science Portfolio**

Showcasing work that I have done for class projects, along with projects done by myself.

**Python:**

---
SI 206 Final Project: 
Worked in a team of three, utilized Yelp’s, Google’s Geocoder, and GeoDB web API’s to gather data. This data was gathered in JSON, and converted into python lists. Then, a six-table database was created with 1,000 rows. Lastly, Visualizations were created using Matplotlib.

Yelp API: businesses name, city, rating, address, phone number, total reviews, price range, and category.

Geocoder: city population, elevation, and timezone

Google Map: Latitude and Longitude

Data was gathered for the most populated 100 US cities, along with top rated restuarants. 

![](https://github.com/mfannin099/data-science-portfolio/blob/main/images/lat_long.png)

[Link to code](https://github.com/mfannin099/data-science-portfolio/tree/main/SI206FinalProject)

---

SI 330 Final Project: 
Goal was to determine whether or not the frequency of a company in the news had any impact on the company's stock price. Data was collected from two web API's: Alpha Vantage and News API. Data recieved from News API wasn't sufficient in answering research question because you can only import a small number of news articles. 

In addition to this, I conducted natural langauge processing on the articles descriptions to see if there was any common langauge used. I used regular expressions to remove unwanted characters and preprocessed the data. I then created a Word2Vec model and made a wordcloud with the most simlar words.

![](https://github.com/mfannin099/data-science-portfolio/blob/main/images/stocks_1.jpg)

[Link to Code](https://github.com/mfannin099/data-science-portfolio/tree/main/SI330_final)

---

College_basketball_1: Pandas 
The first project during summer 2020, I used data that was found on Kaggle that had statistics about different teams from 2015- 2019. I used pandas to analyze why Umich was so successful in 2018, which team is the most successful in the BIG-10, which Power 5 conference wins the most, and whether offensive or defensive efficiency correlates to winning games.

To begin I studied Umich, looking at their wins per season. I took all of the statistics in the dataset and ranked them using pandas rank method. A 5 represents the highest value, and a 1 represents the smallest. The team was so successful in 2018, because they were such a well-rounded team, with no apparent weaknesses. 

![](https://github.com/mfannin099/data-science-portfolio/blob/main/images/basketball_1.jpg)

I then studied the BIG 10 conference and found that Michigan State wins the most games per season (on average). They are followed by: Purdue, Michigan, Wisconsin, and Maryland. I ranked the columns and averaged the scores and found that Purdues average rank was 3.6 and Michigan State's was 3.13.

![](https://github.com/mfannin099/data-science-portfolio/blob/main/images/basketball_2.jpg)

Lastly, I wanted to find correlation between offensive stats and defensive. I created two seperate dataframes and used .corr(). It appeared that offensive efficency had a higher corrleation to winning than defense did.

[Link to Code](https://github.com/mfannin099/data-science-portfolio/tree/main/college_basketball_1)

---

Crypto_4 - Gathered data from web API, using mySQL created database and ran SQL commands

Sentiment_analysis_6 - Used nltk to process text data from web API 

hw5 - Kaggle titanic competition, used machine learning to predict survivabilty 



**R:**

tesla_stock_2 - First project using R, analyzed Tesla's stock data

real_estate_3 - compared traditonal renting versus Airbnb renting in largest cities in US


**Tableau:**

Tableau_practice - Used datasets to create visualizations 

