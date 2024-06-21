import requests
import pprint
#FryingPan channel ID: UCfeMEuhdUtxtaUMNSvxq_Xg

API_KEY = 'AIzaSyD9ZjC6u0PfNFtOswEZR-x2IvZ6dF3H-ec'
PART_CHANNEL = 'contentDetails'
USERNAME = 'FryingPan'

params_channel = {
  'part': PART_CHANNEL,
  'forHandle': USERNAME,
  'key': API_KEY
}
CHANNEL_URL = 'https://www.googleapis.com/youtube/v3/channels'

response = requests.get(CHANNEL_URL, params=params_channel)
channel_info = response.json()

ID = channel_info['items'][0]['contentDetails']['relatedPlaylists']['uploads']
PART_VIDS = 'snippet'
MAX_RESULTS = 2

params_playlistItems = {
  'part': PART_VIDS,
  'playlistId': ID,
  'maxResults': MAX_RESULTS,
  'key': API_KEY
}

PLAYLISTS_URL = 'https://www.googleapis.com/youtube/v3/playlistItems'

upload_info = requests.get(PLAYLISTS_URL, params=params_playlistItems)
uploads = upload_info.json()

#pprint.pprint(uploads)

titles = []

for i in range(len(uploads['items'])):#successfully populates a list of titles!
  #items is a list of every vid
  titles.append(uploads['items'][i]['snippet']['title'])
print(titles)
#works nice!

#git add, git commit, git push (will send it to remote once working)