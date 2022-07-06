import requests
import json
import sqlalchemy as db
import pandas as pd
import pprint

api_key = ''
channelId = input("Enter Channel ID: ")
videoID = input("Enter Video ID: ")


urlForVideoStats = f'https://www.googleapis.com/youtube/v3/videos?id={videoID}&part=statistics&key={api_key}'
url_jsonrForVideoStats = requests.get(urlForVideoStats).json()
pprint.pprint(url_jsonrForVideoStats)
videoStats = url_jsonrForVideoStats['items'][1]['statistics']

print('countViews = ' + url_jsonrForVideoStats['items'][1]['statistics']['viewCount'])
print('countLikes = ' + url_jsonrForVideoStats['items'][1]['statistics']['likeCount'])
print('countDislikes = ' + url_jsonrForVideoStats['items'][1]['statistics']['dislikeCount'])
print('countComments = ' + url_jsonrForVideoStats['items'][1]['statistics']['commentCount'])

df = pd.DataFrame(videoStats, index=[0])
print(df)

engine = db.create_engine('sqlite:///df.db')
df.to_sql('df', con=engine, if_exists='replace', index=False)
queryResult = engine.execute("SELECT * FROM df;").fetchall()


print(pd.DataFrame(queryResult))

