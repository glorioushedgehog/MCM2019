import sys
import time

import requests
import re


def get_json(url):
    try:
        r = requests.get(url)
        try:
            r.raise_for_status()
            return r.json()  # TODO can a request ever not return json?
        except requests.exceptions.HTTPError as e:
            print("HTTP Error", e)
            return None
    except requests.exceptions.ConnectionError as e:
        print("Connection Error", e)
        return None
    except requests.exceptions.Timeout as e:
        print("Timeout Error", e)
        return None
    except requests.exceptions.TooManyRedirects as e:
        print("Too many redirects", e)
        return None
    except requests.exceptions.RequestException as e:
        print("Request Error", e)
        return None


f = open("spanishcitynames.txt", "r")
city_list = eval(f.readline())
city_map = {}
city_to_english_map = {}
string = ''
count = 0
for city in city_list:
    string = re.sub(" +", "+", city)
    api_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    api_url += string
    api_url += '&key=AIzaSyB4CuuupKyNnkAhcaQTVp8SttkAFzKQD5o'
    response_json = get_json(api_url)
    if response_json["status"] != "OK":
        print(api_url)
        print(response_json)
        sys.exit(-1)
    loc = response_json["results"][0]["geometry"]["location"]
    lat = float(loc["lat"])
    lng = float(loc["lng"])
    city_english_name = response_json["results"][0]["formatted_address"]
    city_map[city_english_name] = [lat, lng]
    city_to_english_map[city] = city_english_name
    count += 1
    print(api_url)
    print("done", count)
    print(lat, lng)
    time.sleep(5)

the_file = "citycoordinates.txt"
f = open(the_file, "w")
f.write(str(city_map))
f.close()

the_file = "spanishtoenglish.txt"
f = open(the_file, "w")
f.write(str(city_to_english_map))
f.close()

