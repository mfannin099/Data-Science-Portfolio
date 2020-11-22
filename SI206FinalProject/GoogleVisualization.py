import matplotlib
import matplotlib.pyplot as plt
import sqlite3
import os

def connect_db(filename):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+filename)
    cur = conn.cursor()
    return cur, conn


def plot_lat_long(cur, conn):
    lat = []
    lon = []
    cur.execute("SELECT Latitude, Longitude, Latitude.restaurant_id FROM Latitude INNER JOIN Longitude ON Latitude.restaurant_id = Longitude.restaurant_id")
    rows = cur.fetchall()
    for i in rows:
        lat.append(i[0])
        lon.append(i[1])
    
    
    plt.scatter(lon,lat, c = 'Black', marker = "x")
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Latitude and Longitude of Restaurants in US Cities')
    plt.savefig("lat_long.png", bbox_inches = 'tight')



def main():
    cur, conn = connect_db('data.db')
    plot_lat_long(cur,conn)
    

if __name__ == "__main__":
    main()