import requests
import json

input_query = input("Please enter what you're looking for! ")
input_limit = int(input("How many results would you like? (Depends on availability) "))

parameters = {
            "client_id": 'BKHY0INWOHKC4ZAIEH1PGUH2R1NTZH3E0U0TYDTV1ITOX1VT',
            "client_secret": '0J24EJI4NOMHGYBH3JVSCXMNJ5VX0WUZFEXG0TZLIEW51SXD',
            "v": 20180323,
            "ll": ("43.09, -77.64"),
            "query": input_query,
            "limit": input_limit
}

response = requests.get("https://api.foursquare.com/v2/venues/search", params=parameters)
#print(response.status_code)
#print(response.json())
data = json.dumps(response.json(), sort_keys=True, indent=4)
#print(data)


for i in range(0, input_limit):
    try:
        name = response.json()['response']['venues'][i]['name']
        location = response.json()["response"]["venues"][i]["location"]
        street_address = response.json()["response"]["venues"][i]["location"]["address"]
        city = response.json()["response"]["venues"][i]["location"]["city"]
        state = response.json()["response"]["venues"][i]["location"]["state"]
        zipcode = response.json()["response"]["venues"][i]["location"]["postalCode"]
        print("\n", "Name: ", name, sep="")
        print("Address:", street_address, city, state, zipcode)
    except KeyError:
        print("\n", "Data Error", sep="")
    except IndexError:
        print("\n", "Not enough ", str(input_query)+"s", sep="")
        break
