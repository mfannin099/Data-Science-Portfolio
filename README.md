
# **Python:**

---
## SI 206 Final Project:
Worked in a team of three, utilized Yelp’s, Google’s Geocoder, and GeoDB web API’s to gather data. This data was gathered in JSON, and converted into python lists. Then, a six-table database was created with 1,000 rows. Lastly, Visualizations were created using Matplotlib.

Yelp API: businesses name, city, rating, address, phone number, total reviews, price range, and category.

Geocoder: city population, elevation, and timezone

Google Map: Latitude and Longitude

Data was gathered for the most populated 100 US cities, along with top rated restuarants. 

![](/images/lat_long.png)

[Link to code](https://github.com/mfannin099/data-science-portfolio/tree/main/SI206FinalProject)

---

## SI 330 Final Project: 
Goal was to determine whether or not the frequency of a company in the news had any impact on the company's stock price. Data was collected from two web API's: Alpha Vantage and News API. Data recieved from News API wasn't sufficient in answering research question because you can only import a small number of news articles. 

In addition to this, I conducted natural langauge processing on the articles descriptions to see if there was any common langauge used. I used regular expressions to remove unwanted characters and preprocessed the data. I then created a Word2Vec model and made a wordcloud with the most simlar words.

![](/images/stocks_1.png)

[Link to Code](https://github.com/mfannin099/data-science-portfolio/tree/main/SI330_final)

---

## SI 370 Final Project: 
Worked for the Ann Arbor District Library to determine how many points, how players scored points in their Summer Games. The dataset was over 12 million rows and reduced to 4 million when working with data from 2018-2020. Findings and methodologies are dicussed in the report.

![](/images/logo.jpg)

[Link to Code](https://github.com/mfannin099/SI-370-Final)

---

## Machine Learning: Amazon Best Selling Books

Creating and tuning machine learning model to predict price of books. Dataset was gotten from Kaggle and consisted of 550 rows of the top 50 best selling books from 2009 to 2019.

![](/images/final_predictions.jpg)

[Link to Code](https://github.com/mfannin099/machine-learning-bestsellers)

## College_basketball_1: Pandas 
The first project during summer 2020, I used data that was found on Kaggle that had statistics about different teams from 2015- 2019. I used pandas to analyze why Umich was so successful in 2018, which team is the most successful in the BIG-10, which Power 5 conference wins the most, and whether offensive or defensive efficiency correlates to winning games.

To begin I studied Umich, looking at their wins per season. I took all of the statistics in the dataset and ranked them using pandas rank method. A 5 represents the highest value, and a 1 represents the smallest. The team was so successful in 2018, because they were such a well-rounded team, with no apparent weaknesses. 

![](/images/basketball_1.jpg)

I then studied the BIG 10 conference and found that Michigan State wins the most games per season (on average). They are followed by: Purdue, Michigan, Wisconsin, and Maryland. I ranked the columns and averaged the scores and found that Purdues average rank was 3.6 and Michigan State's was 3.13.

![](/images/basketball_2.jpg)

Lastly, I wanted to find correlation between offensive stats and defensive. I created two seperate dataframes and used .corr(). It appeared that offensive efficency had a higher corrleation to winning than defense did.

[Link to Code](https://github.com/mfannin099/data-science-portfolio/tree/main/college_basketball_1)

---

## Crypto_4: SQL 
This project helped me practice SQL that I learned from coursework in addition to what was covered in an Introduction to SQL, on Coursera. 

I used the coinpaprika API to get data, stored it in python lists in order to put it into my SQL database. I created 7 tables in total. After all the data was inputted, I practiced more SQL commands and conducted some simple analysis.

![](/images/crypto_1.jpg)

[Link to code](https://github.com/mfannin099/summer2020-4)

---

## Sentiment_analysis_6: nltk
I gathered data from the Office API, I took first name, last name, and the quote to form a data frame. Following the same process getting the title of an episode and description in another data frame. 

To process the text data I concatenated the two dataframes and the text was put into a list.

I cleaned the data; made them lowercase, used regular expressions to remove unwanted characters, created tokens, removed punctuation, stop words were removed. 

I then found the words that were most common and created a line chart showing the frequency.

![](/images/nltk_1.jpg)

I then used NLTK methods, and then made a word cloud. 

![](/images/nltk_2.jpg)

Lastly, I made a Word2Vec model and found the most similar words to some of the most common words that appeared in the text.

![](/images/nltk_3.jpg)

[Link to code](https://github.com/mfannin099/project2020-6)

---

hw5 - Kaggle titanic competition, used machine learning to predict survivabilty 

---

# **R:**

## tesla_stock_2: R 
This is my first time using R, I learned it from: reading articles, documentation, and watching tutorials. 

I imported a dataset from Kaggle. Then, made some basic plots to visualize the data, and find correlation between columns to begin. 

![](/images/tesla_1.jpg)

I made a linear regression model based on the opening and closing prices. 

![](/images/tesla_2.jpg)

I then calculate a moving average of the closing price. Lastly, made a machine learning model in an attempt to predict its future price.

![](/images/tesla_3.jpg)

[Link to code](https://github.com/mfannin099/data-science-portfolio/tree/main/tesla_stock_2)

---

## real_estate_3: R
This project expanded my knowledge in R and helped me become more fluent with syntax. I utilized piping, and more statistical analysis tools that R offers.

I first gathered data by making calls to the Mashvisor API getting the most populated cities in the United States, and created a CSV file to import into RStudio.

What are the best cities to have rental property? To maximize income should property owners rent traditionally or on Airbnb?

![](/images/real_estate_1.jpg)

Made predictions based on linear regression models. Inputting an average occupancy of 50 guests, the model then predicts the average rental income the property will bring in. 

![](/images/real_estate_2.jpg)

**Findings:** The best cities to have rental property in are: Nashville, San Francisco, Boston, and Austin. They have the highest nightly cost, and produce the most passive income per year. 

[Link to code](https://github.com/mfannin099/data-science-portfolio/tree/main/real_estate_3)

---

# **Tableau:**

## Tableau_practice: Tableau 
This project consists of multiple smaller projects. I am taking data from Kaggle, imported it into Tableau in order to make interesting, simple, and insightful visualizations so I can learn from the data. I downloaded the student free trial, coupled with Tableau’s own tutorials and YouTube videos I felt ready to dive in for myself.

![](/images/tableau_1.jpg)

![](/images/tableau_2.jpg)

![](/images/tableau_3.jpg)

[Link to code](https://github.com/mfannin099/summer2020-5)

