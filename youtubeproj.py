import requests

API_KEY = 'AIzaSyD9ZjC6u0PfNFtOswEZR-x2IvZ6dF3H-ec'
CHANNEL_ID = 'UCfeMEuhdUtxtaUMNSvxq_Xg'
PART = 'snippet'
MAX_RESULTS = 10

params = {
  'part': PART,
  'channelId': CHANNEL_ID,
  'maxResults': MAX_RESULTS,
  'key': API_KEY
}

BASE_URL = 'https://www.googleapis.com/youtube/v3/playlists'

response = requests.get(BASE_URL, params=params)
print(response.json())
#works!
#git add, git commit, git push (will send it to remote once working)