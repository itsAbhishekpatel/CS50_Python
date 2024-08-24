# APIs - Application programming interface 
"""third party servies - live on the internet 
so you can write the code which act like a browser and interact with the APIs"""

# using requests package, you are browser in yourself
import requests
import sys
import json
# if len(sys.argv) !=2:
#     exit()

# get is the fucntion inside the requests packages which get respose from the server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")  
# for items in response.json():
#     print(items)

# format the json data fetch by api 
print(json.dumps(response.json(), indent=2))


"""JSON - javascript object notation: text which is formatted """