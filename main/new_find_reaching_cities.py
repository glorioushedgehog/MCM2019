import math


class Drop:
    def __init__(self, name, lat, lng, bay1weights, bay2weights):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.bay1weights = bay1weights
        self.bay2weights = bay2weights


def get_weights1(needs):
    pass


def get_weights2(needs):
    pass


def get_dist(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    r = 6371e3  # metres
    l1 = math.radians(lat1)
    l2 = math.radians(lat2)
    t1 = math.radians(lat2 - lat1)
    t2 = math.radians(lon2 - lon1)

    a = math.sin(t1 / 2) * math.sin(t1 / 2) + math.cos(l1) * math.cos(l2) * math.sin(t2 / 2) * math.sin(t2 / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    d = r * c
    return d


drops = [Drop("Carribean", 18.33211, -65.6501, get_weights1([1, 0, 1]), get_weights2([1, 0, 1])),
         Drop("HIMA", 18.2183, -66.0314, get_weights1([2, 0, 1]), get_weights2([2, 0, 1])),
         Drop("Santurce", 18.44425, -66.069, get_weights1([1, 1, 0]), get_weights2([1, 1, 0])),
         Drop("Children's", 18.39657, -66.1633, get_weights1([2, 1, 2]), get_weights2([2, 1, 2])),
         Drop("Arecibo", 18.46722, -66.7314, get_weights1([1, 0, 0]), get_weights2([1, 0, 0]))]
f = open("spanishcitycoordinates.txt", "r")
city_map = eval(f.readline())
city_drops_reached = {}
for city in city_map.keys():
    city_drops_reached[city] = []
f.close()
max_reach = 26333.3333
for drop in drops:
    reaching = []
    for city in city_map.keys():
        if get_dist(city_map[city], [drop.lat, drop.lng]) < max_reach:
            reaching.append(city)
            city_drops_reached[city].append(drop.name)
    print(drop.name, "is reached by", len(reaching), ":", reaching)
for city in city_drops_reached.keys():
    if len(city_drops_reached[city]) > 2:
        print(city, len(city_drops_reached[city]))
