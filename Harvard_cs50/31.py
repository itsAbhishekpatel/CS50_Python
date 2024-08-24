import json
import requests 
import sys

# using python we interact with real world third party api
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=weezer")  

o = response.json()

# print song names associated with weezer band
for result in o["results"]:
    print(result["trackName"])