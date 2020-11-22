import requests
import json
import os
import sqlite3
import time

def get_data(round, cur, conn):
    city_codes1 = ['Q60', 'Q65', 'Q1297', 'Q16555', 'Q1345', 'Q16556', 'Q975', 'Q16552', 'Q16557', 'Q16553', 'Q16559', 'Q16568', 'Q62', 'Q6346', 'Q16567', 'Q16558', 'Q16565', 'Q5083', 'Q16554', 'Q16562']
    city_codes2 = ['Q12439', 'Q61', 'Q100', 'Q16563', 'Q23197', 'Q6106', 'Q34863', 'Q23768', 'Q43668', 'Q5092', 'Q37836', 'Q34804', 'Q18575', 'Q43301', 'Q49261', 'Q18013', 'Q23556', 'Q41819', 'Q49258', 'Q8652']
    city_codes3 = ['Q41087', 'Q43199', 'Q16739', 'Q49259', 'Q17042', 'Q36091', 'Q44989', 'Q107126', 'Q49255', 'Q34404', 'Q49266', 'Q37320', 'Q49256', 'Q22595', 'Q49247', 'Q18094', 'Q199797', 'Q49243', 'Q49242', 'Q49241']
    city_codes4 = ['Q49240', 'Q49267', 'Q28848', 'Q38022', 'Q43196', 'Q1342', 'Q49238', 'Q39450', 'Q51689', 'Q28260', 'Q49233', 'Q49219', 'Q25395', 'Q49239', 'Q49229', 'Q49270', 'Q485172', 'Q26339', 'Q49236', 'Q16868']
    city_codes5 = ['Q43788', 'Q49272', 'Q40435', 'Q49273', 'Q49221', 'Q49225', 'Q485716', 'Q51684', 'Q49227', 'Q49231', 'Q49222', 'Q49274', 'Q51690', 'Q49276', 'Q49220', 'Q35775', 'Q43421', 'Q28218', 'Q79867', 'Q39709']

    # full city_codes list
    city_codes = [city_codes1, city_codes2, city_codes3, city_codes4, city_codes5]

    # overwrote with just Q60 for testing, remove to run actual code
    # city_codes = [['Q60'], ['Q12439'], ['Q41087'], ['Q49240'], ['Q43788']]

    base_url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/"
    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': "e9557b3be3msh2ca132a52dbbc5bp1e9aacjsna6acb3f99a0d"
    }

    results = []

    if round == 1:
        create_citypop(cur, conn)
        create_cityinfo(cur, conn)

    for code in city_codes[round - 1]:
        time.sleep(2)
        url = base_url + code
        response = requests.request("GET", url, headers=headers)
        data = json.loads(response.text)
        try:
            info = (data['data']['name'], data['data']['elevationMeters'], data['data']['population'], data['data']['timezone'])
            results.append(info)
        except:
            print()
            print(code)
            print(data)
            print()

    return results

# 2 tables
# table 1: key = city name, column(s) = population
# table 2: key = city name, column(s) = elevationMeters, timezone
def connect_db(filename):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+filename)
    cur = conn.cursor()
    return cur, conn

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

def main():
    round = int(input("Enter data round number (1-5): "))
    cur, conn = connect_db('cities.db')
    data = get_data(round, cur, conn)
    insert_citypop(data, cur, conn)
    insert_cityinfo(data, cur, conn)

if __name__ == "__main__":
    main()