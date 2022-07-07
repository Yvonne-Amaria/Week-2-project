import requests
import json
import sqlalchemy as db
import pandas as pd
import pprint

'''
url = "https://weatherapi-com.p.rapidapi.com/current.json"


user = input("Enter your zipcode: ")
querystring = {"q":user}

headers = {
	"X-RapidAPI-Key": "4386b895d6mshc4e43be45e4ac39p1385f8jsnf87c968c7233",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response2 = response.json()
Report = response2['location']


data = pd.DataFrame(Report, index=[0])
print(data)

engine = db.create_engine('sqlite:///data.db')
data.to_sql('data', con=engine, if_exists='replace', index=False)
queryResult = engine.execute("SELECT * FROM data;").fetchall()

print(pd.DataFrame(queryResult))
'''


url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
city_name = input("Enter the name of city: ")
date = input("Enter the DATE (YYYY-MM-DD): ")

querystring = {"q":city_name,"dt":date}

headers = {
	"X-RapidAPI-Key": "4386b895d6mshc4e43be45e4ac39p1385f8jsnf87c968c7233",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response2 = response.json()
name = response2['location']['name']
country = response2['location']['country']
weather_condition = response2['current']['condition']['text']
temp_f = response2['current']['temp_f']
temp_c = response2['current']['temp_c']
humidity = response2['current']['humidity']
wind = response2['current']['wind_mph']

report ={'name':name,
       'country':country,
	   'weather_condition':weather_condition,
	   'temp_f':temp_f,
	   'temp_c':temp_c,
	   'humidity':humidity,
	   'wind':wind
      }
data = pd.DataFrame(report ,index =[0])
engine = db.create_engine('sqlite:///data.db')
data.to_sql('data', con=engine, if_exists='replace', index=False)
queryResult = engine.execute("SELECT * FROM data;").fetchall()

print(pd.DataFrame(queryResult))
