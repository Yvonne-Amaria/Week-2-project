import requests
import json
import sqlalchemy as db
import pandas as pd
import pprint


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
print(data)
tmp = (data.loc[0].at["temp_f"])
weather_cond = (data.loc[0]. at["weather_condition"])
engine = db.create_engine('sqlite:///data.db')
data.to_sql('data', con=engine, if_exists='replace', index=False)
queryResult = engine.execute("SELECT * FROM data;").fetchall()

#print(pd.DataFrame(queryResult))
if tmp >=85:
    print ("\nOnly 3 part time employees need to work today because the temperature is " + str(tmp) + "°f and it is " + str(weather_cond))
elif (tmp <= 85 and tmp >= 75):
    print("\n10 part employees need to work today because the temperature is " + str(tmp) + "°f and it is " + str(weather_cond))
elif (tmp <= 75 and tmp >= 70):
	print("\n5 part time employees need  to work today because the temperature is " + str(tmp) + "°f and it is " + str(weather_cond))
else:
	print("\nno part time employees need for  today because the temperature is " + str(tmp) + "°f and it is " + str(weather_cond))
