import requests
import json

parameters = {
            "client_id": 'BKHY0INWOHKC4ZAIEH1PGUH2R1NTZH3E0U0TYDTV1ITOX1VT',
            "client_secret": '0J24EJI4NOMHGYBH3JVSCXMNJ5VX0WUZFEXG0TZLIEW51SXD',
            "v": 20180323,
            "ll": ("43.09, -77.64"),
            "query": "coffee",
            "limit": 1
}

response = requests.get("https://api.foursquare.com/v2/venues/search", params=parameters)
print(response.status_code)
print(response.json())
"""
responsedict = dict(response.json())
print(responsedict)
print(type(responsedict))
print(responsedict.keys())
#print(type(response))
print(responsedict["response"][1]["name"])


for key,value in responsedict:
    if key == response:
        print(responsedict[key])"""

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
