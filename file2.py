import requests
import json
import sqlalchemy as db
import pandas as pd
import pprint


url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

headers = {
	"X-RapidAPI-Key": "4386b895d6mshc4e43be45e4ac39p1385f8jsnf87c968c7233",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
city_name = input("Enter the name of city: ")
date = input("Enter the DATE (YYYY-MM-DD): ")

querystring = {"q":city_name,"dt":date}

def get_report(name, country, weather_condition, temp_f, temp_c, humidity,wind):
	dict = {
        'name':name,
        'country':country,
        'weather_condition':weather_condition,
        'temp_f':temp_f,
        'temp_c':temp_c,
        'humidity':humidity,
        'wind':wind
        }
    return dict


def get_forecast(city_name, date):
    response = requests.request("GET", url, headers=headers, params=querystring)
    response2 = response.json()

    name = response2['location']['name']
    country = response2['location']['country']
    weather_condition = response2['current']['condition']['text']
    temp_f = response2['current']['temp_f']
    temp_c = response2['current']['temp_c']
    humidity = response2['current']['humidity']
    wind = response2['current']['wind_mph']

    return get_report(name, country, weather_condition, temp_f, temp_c, humidity,wind)


forecast= get_forecast(city_name, date)
data = pd.DataFrame(forecast,index=[0])
tmp = (data.loc[0].at["temp_f"])
weather_cond = (data.loc[0]. at["weather_condition"])
engine = db.create_engine('sqlite:///data.db')
data.to_sql('data', con=engine, if_exists='replace', index=False)
queryResult = engine.execute("SELECT * FROM data;").fetchall()
print(pd.DataFrame(queryResult))


def num_of_employees(tmp):
    if tmp >=85:
        return 3 
    elif (tmp <= 85 and tmp >= 75):
        return 10
    elif (tmp <= 75 and tmp >= 70):
        return 5
    else:
        return 0


employees = num_of_employees(tmp)
print("\n" + str(employees) + " part time employees need to work today because the temperature is " + str(tmp) + "°f and it is " + str(weather_cond))
