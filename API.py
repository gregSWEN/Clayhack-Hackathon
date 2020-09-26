import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
#print(response.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

parameters = {
    "lat": 40.71,
    "lon": -74
}

response2 = requests.get(" http://api.open-notify.org/iss-pass.json", params=parameters)
print(response2.status_code)
#print(response.json())


def jprint2(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint2(response2.json())

pass_times = response2.json()['response']
jprint2(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

from datetime import datetime
times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)


