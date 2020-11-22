import sqlite3
import os

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn
# Function to set up the main database, called final.db

def setUpCityLatDatabase(city_list, lat_list , long_list, cur, conn):
    restaurant_name_list = []
    lat_li = []
    long_li = []

    cur.execute("DROP TABLE IF EXISTS RestaurantLocations")
    cur.execute("CREATE TABLE RestaurantLocations (Restaurant_Name TEXT, Latitude REAL, Longitude REAL)")

    for i in city_list:
        restaurant_name_list.append(i)
    for i in lat_list:
        lat_li.append(i)
    for i in long_list:
        long_li.append(i)

    for i in range(len(restaurant_name_list)):
        cur.execute("INSERT INTO RestaurantLocations (Restaurant_Name, Latitude, Longitude) VALUES (?,?,?)",(restaurant_name_list[i], lat_li[i], long_li[i]))
    conn.commit()

def main():
    cur, conn = setUpDatabase('Lat&Long.db')
    city_list = ["Detroit", "Atlanta"]
    lat_list = [42.347473, -83.0655422]
    long_list = [-83.0655422, 42.347473]
    setUpCityLatDatabase(city_list, lat_list, long_list, cur, conn)
    for i in listx:
        getGoogleData(i)
        
if __name__ == "__main__":
    main()