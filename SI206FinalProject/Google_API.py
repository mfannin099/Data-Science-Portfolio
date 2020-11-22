import requests 
import json
import re
import sqlite3
import os


def get_Google_data(data):

    lat_long_list = []
    api_key = 'AIzaSyAg9jsCeHF3VjdMJqEAuT90fpArAXQZld4'
    #API key given from Google
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={},{},{}&key={}'
    #From Documentation

    #data = re.sub(r'[^\w\s]','',data)
    #To get rid of the comma, and to forget the zip code
    #data_pieces = data.split()
    # street1 = data_pieces[0:-3]
    # s = " "
    # street = s.join(street1) 
    # city = data_pieces[-3]
    # state = data_pieces[-2]
    #Need to split up data, into pieces of address in order to put them in url
    street = data[1]
    city = data[2]
    state = data[3]

    request_url = base_url.format(street, city, state, api_key)
    #Need to pass in these parameters in order to have a complete request
    r = requests.get(request_url)
    data = r.text
    data_dict = json.loads(data)
    
    #print(json.dumps(data_dict,indent=4))
    results = data_dict["results"]
    for result in results:
        lat = result["geometry"]['location']["lat"]
        lat_long_list.append(lat)
        lon = result["geometry"]['location']['lng']
        lat_long_list.append(lon)
    
    return lat_long_list
#Returns Latitude and Longitude


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn
# Function to set up the main database, called final.db

def restaurant_list_creator(cur, conn):
    restaurants = []
    cur.execute("SELECT restaurant_id, address, city, state FROM YelpAddress")
    rows = cur.fetchall()
    for row in rows:
        restaurants.append((row[0], row[1], row[2], row[3]))
    return restaurants

def clear_databases(cur, conn):
    cur.execute("DROP TABLE IF EXISTS Latitude")
    cur.execute("DROP TABLE IF EXISTS Longitude")
    conn.commit()


def latDatabase(data, lat_and_long, cur, conn):
    lat = lat_and_long[0]     
    cur.execute("INSERT INTO Latitude (restaurant_id, Latitude) VALUES (?,?)",(data[0], lat))
    conn.commit()

def longDatabase(data, lat_and_long, cur, conn):
    lon = lat_and_long[1]
    cur.execute("INSERT INTO Longitude (restaurant_id, Longitude) VALUES (?,?)",(data[0], lon))
    conn.commit()

def main():
    cur_ll, conn_ll = setUpDatabase('Lat&Long.db')
    cur_y, conn_y = setUpDatabase('yelp.db')

    clear_databases(cur_ll, conn_ll)

    restaurants = restaurant_list_creator(cur_y, conn_y)

    cur_ll.execute("CREATE TABLE IF NOT EXISTS Latitude (restaurant_id TEXT PRIMARY KEY, Latitude REAL)")
    cur_ll.execute("CREATE TABLE IF NOT EXISTS Longitude (restaurant_id TEXT PRIMARY KEY, Longitude REAL)")
    conn_ll.commit()
    
    for i in restaurants:
        lat_and_long = get_Google_data(i)
        latDatabase(i, lat_and_long, cur_ll, conn_ll)
        longDatabase(i, lat_and_long, cur_ll, conn_ll)

if __name__ == "__main__":
    main()



