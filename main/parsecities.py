import re
import sys
import time

import requests


def get_city_map():
    fo = open("puertoricocities.txt", "r")
    city_map = {}
    found_city = False
    cityo = "INITIAL_CITY"
    for line in fo:
        line = line.strip()
        if line:
            x = re.findall("[0-9]", line[0])
            if x:
                if found_city:
                    line = re.sub(",", "", line)
                    num = float(line)
                    found_city = False
                    city_map[cityo] = num
            else:
                found_city = True
                cityo = line
            # print(line)
    return city_map


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


cities = get_city_map()

city_list = list(cities.keys())
city_names_file = "spanishcitynames.txt"
f = open(city_names_file, "w")
f.write(str(city_list))
f.close()
num_cities = len(city_list)
for k in range(num_cities):
    new_string = city_list[k]
    new_string = re.sub("comunidad", "", new_string)
    new_string = re.sub("zona urbana", "", new_string)
    new_string = re.sub("Municipio", "", new_string)
    city_list[k] = new_string
distance = []
for _ in range(num_cities):
    row = [-1] * num_cities
    distance.append(row)

english_city_names = []
not_found_counter = 0
call_counter = 0
num_chunks = int(num_cities / 10)
for i in range(num_chunks):
    origin_list = city_list[10 * i: 10 * (i + 1)]
    for j in range(num_chunks):
        destination_list = city_list[10 * j: 10 * (j + 1)]
        api_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins='
        origin_string = ''
        for city in city_list:
            origin_string += re.sub(" +", "+", city) + "|"
        origin_string = origin_string[:-1]
        api_url += origin_string + '&destinations='
        destination_string = ''
        for city in city_list:
            destination_string += re.sub(" +", "+", city) + "|"
        destination_string = destination_string[:-1]
        api_url += destination_string
        api_url += '&mode=driving&language=en&key=AIzaSyDb3dox_85hXQ9-C1LEa8YQBjetxlliq1Q'
        print(api_url)
        call_counter += 1
        response_json = get_json(api_url)
        if response_json["status"] != "OK":
            print(response_json)
            sys.exit(-1)
        if i == 0:
            english_cities = response_json["origin_addresses"]
            english_city_names += english_cities
        rows = response_json["rows"]
        row_index = i * 10
        col_index = j * 10
        for row in rows:
            elements = row["elements"]
            for element in elements:
                if element["status"] != "OK":
                    not_found_counter += 1
                else:
                    distance_value = element["distance"]["value"]
                    distance[row_index][col_index] = distance_value
                col_index += 1
            row_index += 1
        print("calls completed:", call_counter, "not found:", not_found_counter)
        time.sleep(2)

write_file = "distancematrix.txt"
f = open(write_file, "w")
f.write(str(distance))
f.close()

city_names_file = "citynames.txt"
f = open(city_names_file, "w")
f.write(str(english_city_names))
f.close()

