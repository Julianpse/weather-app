import json
import datetime
import psycopg2
import requests
#
# #Opens Data to be rendered on results page
#
# with open("data.json") as json_file:
#     json_data = json.load(json_file)
#
#
# #prints temperature
# print(int(json_data["main"]["temp"]))
#
# #prints what the sky is
# print(json_data["weather"][0]["main"])
#
# #prints the location
# print(json_data["name"])
#
#
# #prints the timestamp and converts it into readable
# unix_time = json_data["dt"]
# readable_time = datetime.datetime.fromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')
# print (readable_time)



# This is the sql to add the data to the database
# INSERT INTO weather(city_name, temperature, time_of_day) VALUES('Houston', 57, localtimestamp);


def weather_request():
    payload = {'q': "Los Angeles", "APPID": "ec4678cf0af0d362007a3348b7c53b7a", "units": "imperial"}
    r = requests.get('https://api.openweathermap.org/data/2.5/weather', params = payload)

    data = r.json()

    location = data["name"]
    temperature = int(data["main"]["temp"])


    try:
        conn = psycopg2.connect("dbname='weatherapp' user='julianse' host='localhost' password=''")
        cur = conn.cursor()
    except:
        print("I am unable to connect to the database, please check your connection")


    cur.execute("INSERT INTO weather(city_name, temperature, time_of_day) VALUES (%s, %s, LOCALTIMESTAMP)", (location, temperature))
    conn.commit()
    cur.close()
    conn.close()



weather_request()
