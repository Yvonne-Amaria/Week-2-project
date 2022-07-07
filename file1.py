import requests
import json
import sqlalchemy as db
import pandas as pd
import pprint

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
