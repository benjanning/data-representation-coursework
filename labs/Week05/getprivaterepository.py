import requests
import json
from config import config as cfg
from config import apikey 

filename = "repos-private.json"

url = 'https://api.github.com/benjanning/aprivateone/'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)


response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)