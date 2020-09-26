import requests
import json

response = requests.get("http://api.open-notofy.org/iss-pass.json")
# print(response.status_code)
# print(response.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


"""response2 = requests.get("http://api.open-notofy.org/iss-pass.json")


def jprint2(obj2):
    cord = json.dumps(obj2, sort_keys=True, indent=3)
    print(cord)


jprint2(response.json())
"""

