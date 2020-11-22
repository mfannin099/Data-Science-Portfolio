import requests
import json
import os
import sqlite3
import time

from PlotVisualizations import visualize

def get_city_data(round, cur, conn):
    codes1 = ['Q60', 'Q65', 'Q1297', 'Q16555', 'Q1345', 'Q16556', 'Q975', 'Q16552', 'Q16557', 'Q16553']
    codes2 = ['Q16559', 'Q16568', 'Q62', 'Q6346', 'Q16567', 'Q16558', 'Q16565', 'Q5083', 'Q16554', 'Q16562']
    codes3 = ['Q12439', 'Q61', 'Q100', 'Q16563', 'Q23197', 'Q6106', 'Q34863', 'Q23768', 'Q43668', 'Q5092']
    codes4 = ['Q37836', 'Q34804', 'Q18575', 'Q43301', 'Q49261', 'Q18013', 'Q23556', 'Q41819', 'Q49258', 'Q8652']
    codes5 = ['Q41087', 'Q43199', 'Q16739', 'Q49259', 'Q17042', 'Q36091', 'Q44989', 'Q107126', 'Q49255', 'Q34404']
    codes6 = ['Q49266', 'Q37320', 'Q49256', 'Q22595', 'Q49247', 'Q18094', 'Q199797', 'Q49243', 'Q49242', 'Q49241']
    codes7 = ['Q49240', 'Q49267', 'Q28848', 'Q38022', 'Q43196', 'Q1342', 'Q49238', 'Q39450', 'Q51689', 'Q28260']
    codes8 = ['Q49233', 'Q49219', 'Q25395', 'Q49239', 'Q49229', 'Q49270', 'Q485172', 'Q26339', 'Q49236', 'Q16868']
    codes9 = ['Q43788', 'Q49272', 'Q40435', 'Q49273', 'Q49221', 'Q49225', 'Q485716', 'Q51684', 'Q49227', 'Q49231']
    codes10 = ['Q49222', 'Q49274', 'Q51690', 'Q49276', 'Q49220', 'Q35775', 'Q43421', 'Q28218', 'Q79867', 'Q39709']

    # full city_codes list
    city_codes = [codes1, codes2, codes3, codes4, codes5, codes6, codes7, codes8, codes9, codes10]

    base_url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/"
    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': "e9557b3be3msh2ca132a52dbbc5bp1e9aacjsna6acb3f99a0d"
    }

    results = []
    for code in city_codes[round - 1]:
        time.sleep(2)
        url = base_url + code
        response = requests.request("GET", url, headers=headers)
        data = json.loads(response.text)
        try:
            info = (data['data']['name'], data['data']['elevationMeters'], data['data']['population'], data['data']['timezone'])
            results.append(info)
        except:
            print(code)
    return results

def get_yelp_data(api_key, city):
    headers = {'Authorization': 'Bearer %s' % api_key}
    url='https://api.yelp.com/v3/businesses/search'
    params={'term':'restaurant', 'location': city }
    req = requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)
    return parsed

def get_google_data(data):
    lat_long_list = []
    api_key = ''
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={},{},{}&key={}'
    street = data[1]
    city = data[2]
    state = data[3]
    request_url = base_url.format(street, city, state, api_key)
    r = requests.get(request_url)
    data = r.text
    data_dict = json.loads(data)
    results = data_dict["results"]
    for result in results:
        lat = result["geometry"]['location']["lat"]
        lat_long_list.append(lat)
        lon = result["geometry"]['location']['lng']
        lat_long_list.append(lon)
    return lat_long_list

def get_city_list(cur, conn):
    cities = []
    cur.execute("SELECT city_name FROM CityPop")
    rows = cur.fetchall()
    for row in rows:
        cities.append(row[0])
    return cities

def get_restaurants_list(cur, conn):
    restaurants = []
    cur.execute("SELECT restaurant_id, address, city, state FROM YelpAddress")
    rows = cur.fetchall()
    for row in rows:
        restaurants.append((row[0], row[1], row[2], row[3]))
    return restaurants

def connect_db(filename):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+filename)
    cur = conn.cursor()
    return cur, conn

def create_google(cur, conn):
    cur.execute("DROP TABLE IF EXISTS Latitude")
    cur.execute("DROP TABLE IF EXISTS Longitude")
    cur.execute("CREATE TABLE IF NOT EXISTS Latitude (restaurant_id TEXT PRIMARY KEY, Latitude REAL)")
    cur.execute("CREATE TABLE IF NOT EXISTS Longitude (restaurant_id TEXT PRIMARY KEY, Longitude REAL)")
    conn.commit()

def create_yelp(cur, conn):
    cur.execute("DROP TABLE IF EXISTS Yelp")
    cur.execute("DROP TABLE IF EXISTS YelpAddress")
    cur.execute("CREATE TABLE Yelp (restaurant_id TEXT PRIMARY KEY, name TEXT, phone_num TEXT, rating REAL, reviews INTEGER)")
    cur.execute("CREATE TABLE YelpAddress (restaurant_id TEXT PRIMARY KEY, address TEXT, city TEXT, zipcode TEXT, state TEXT)")
    conn.commit()

def create_citypop(cur, conn):
    cur.execute("DROP TABLE IF EXISTS CityPop")
    cur.execute("CREATE TABLE CityPop (city_name TEXT PRIMARY KEY, population INTEGER)")
    conn.commit()

def insert_citypop(data, cur, conn):
    for item in data:
        cur.execute("INSERT INTO CityPop (city_name, population) VALUES (?,?)",(item[0],item[2]))
    conn.commit()

def create_cityinfo(cur, conn):
    cur.execute("DROP TABLE IF EXISTS CityInfo")
    cur.execute("CREATE TABLE CityInfo (city_name TEXT PRIMARY KEY, elevation INTEGER, timezone TEXT)")
    conn.commit()

def insert_cityinfo(data, cur, conn):
    for item in data:
        cur.execute("INSERT INTO CityInfo (city_name, elevation, timezone) VALUES (?,?,?)",(item[0],item[1],item[3]))
    conn.commit()

def insert_yelp(data, cur, conn):
    id_list = []
    name_list = []
    city_list = []
    address_list = []
    state_list = []
    zipcode_list = []
    phone_list = []
    rating_list = []
    reviewcount_list = []

    for count, rest in enumerate(data["businesses"]):
        ID = rest['id']
        id_list.append(ID)

        name = rest['name']
        name_list.append(name)

        city = rest['location']['city']
        city_list.append(city)

        address = rest['location']
        address_list.append(address['address1'])

        state = rest['location']['state']
        state_list.append(state)

        zipcode = rest['location']
        zipcode_list.append(zipcode["zip_code"])
        
        phone_num = rest['phone']
        phone_list.append(phone_num)

        rating = rest['rating']
        rating_list.append(rating)

        reviews = rest['review_count']
        reviewcount_list.append(reviews)

        # only want to store top 10 restaurants
        if count == 9:
            break

    for i in range(len(city_list)):
        try:
            cur.execute("INSERT INTO Yelp (restaurant_id ,name, phone_num, rating, reviews) VALUES (?,?,?,?,?)",(id_list[i],name_list[i], phone_list[i],rating_list[i],reviewcount_list[i]))
            cur.execute("INSERT INTO YelpAddress (restaurant_id, address, city, zipcode, state) VALUES (?,?,?,?,?)",(id_list[i],address_list[i],city_list[i],zipcode_list[i], state_list[i]))
        except:
            print(name_list[i], city_list[i])
    conn.commit()

def insert_lat(data, lat_long, cur, conn):
    lat = lat_long[0]     
    cur.execute("INSERT INTO Latitude (restaurant_id, Latitude) VALUES (?,?)",(data[0], lat))
    conn.commit()

def insert_long(data, lat_long, cur, conn):
    lon = lat_long[1]
    cur.execute("INSERT INTO Longitude (restaurant_id, Longitude) VALUES (?,?)",(data[0], lon))
    conn.commit()

def handle_cities(cur, conn):
    round = int(input("Enter data round number (1-10): "))
    if round == 1:
        create_citypop(cur, conn)
        create_cityinfo(cur, conn)
    data = get_city_data(round, cur, conn)
    insert_citypop(data, cur, conn)
    insert_cityinfo(data, cur, conn)

def handle_yelp(cur, conn):
    api_key='LS5XDJMhLBven3IcI5NFLb8Izy51zMVtz00PY7RpDtlUeOvoPr0jLmVIriDNjWcWft146AaheyIzozbdRgMSRwMS8edXYcjZQHob1dhg_FKyAbeRukYTOs3YSUHcXXYx'
    round = int(input("Enter data round number (1-100): "))
    cities = get_city_list(cur, conn)
    if round == 1:
        create_yelp(cur, conn)
    city = cities[round - 1]
    restaurants = get_yelp_data(api_key, city)
    insert_yelp(restaurants, cur, conn)

def handle_google(cur, conn):
    round = int(input("Enter data round number (1-100): "))
    restaurants = get_restaurants_list(cur, conn)
    if round == 1:
        create_google(cur, conn)
    round_start = 10 * (round - 1)
    round_end = 10 * round
    restaurants = restaurants[round_start:round_end]
    for restaurant in restaurants:
        lat_long = get_google_data(restaurant)
        insert_lat(restaurant, lat_long, cur, conn)
        insert_long(restaurant, lat_long, cur, conn)

def handle_clear(cur, conn):
    create_citypop(cur, conn)
    create_cityinfo(cur, conn)
    create_yelp(cur, conn)
    create_google(cur, conn)

def handle_visualize():
    visualize()

def main():
    phase = input("Enter phase: ")
    cur, conn = connect_db('data.db')
    if phase == "GeoDB":
        handle_cities(cur, conn)
    if phase == "Yelp":
        handle_yelp(cur, conn)
    if phase == "Google":
        handle_google(cur, conn)
    if phase == "Clear":
        handle_clear(cur, conn)
    if phase == "Visualize":
        handle_visualize()

if __name__ == "__main__":
    main()