import requests
import pprint
import pandas as pd
import sqlalchemy as db
import html
#FryingPan channel ID: UCfeMEuhdUtxtaUMNSvxq_Xg
#https://www.googleapis.com/youtube/v3/videos, videos endpoint, would want to 
#use statistics parameter to get the views

API_KEY = 'AIzaSyD9ZjC6u0PfNFtOswEZR-x2IvZ6dF3H-ec'  #global
# implement user input later


def channel():
  PART_CHANNEL = 'contentDetails'
  USERNAME = 'FryingPan'

  params_channel = {
    'part': PART_CHANNEL,
    'forHandle': USERNAME,
    'key': API_KEY
  }
  CHANNEL_URL = 'https://www.googleapis.com/youtube/v3/channels'

  channel_info = requests.get(CHANNEL_URL, params=params_channel)
  channel_dict = channel_info.json()
  return channel_dict['items'][0]['id']


def search(id, query=None):
  ORDER = 'viewCount'
  PART_POPULAR = 'snippet'
  TYPE = 'video'
  CHANNEL_ID = id
  Q = query


  params_search = {
    'part': PART_POPULAR,
    'order': ORDER,
    'maxResults': 10,
    'type': TYPE,
    'key': API_KEY,
    'channelId': CHANNEL_ID
  }

  if query:
    params_search['q'] = 'Q'

  SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

  search_result = requests.get(SEARCH_URL, params=params_search)
  search_dict = search_result.json()
  #pprint.pprint(search_dict)

  return populate_dict(search_dict) # pull titles, make dict with titles as keys


def populate_dict(info):

  sql_dict = {}

  for i in range(len(info['items'])): # make a dict mapping video titles to their video id's and date published
    curr_dict = info['items'][i]
    sql_dict[html.unescape(curr_dict['snippet']['title'])] = [curr_dict['id']['videoId'], curr_dict['snippet']['publishedAt']]
    # use this html method to avoid errors caused by accidental html chars
  return sql_dict


def videos(video_dict):
  ids = []
  for key in video_dict.keys():
    ids.append(video_dict[key][0])

  id_string = ','.join(ids)
  
  ID = id_string
  PART = 'snippet', 'statistics'

  params_videos = {
    'part': PART,
    'id': ID,
    'key': API_KEY
  }

  VIDEOS_URL = 'https://www.googleapis.com/youtube/v3/videos'

  video_stats = requests.get(VIDEOS_URL, params = params_videos)
  video_info = video_stats.json()
  

  for item in video_info['items']:
    curr_title = html.unescape(item['snippet']['title']) # use this html method to avoid errors caused by accidental html chars
    curr_views = item['statistics']['viewCount']

    if curr_title in video_dict:
      video_dict[curr_title].append(curr_views)
    else:
      print("")
      print(curr_title)
      print("")

  return video_dict

id = channel()
dict_test = search(id)
final_dict = videos(dict_test) 
pprint.pprint(final_dict)


df = pd.DataFrame.from_dict(final_dict, orient = 'index') # nice

engine = db.create_engine('sqlite:///ytinfo.db')

df.to_sql('final_dict', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM final_dict;")).fetchall()
   print(pd.DataFrame(query_result))
