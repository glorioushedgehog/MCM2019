import math
import re
import queue


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


def reachable_population(pop_dict, loc_dict, city_name, drone_name):
    reachable = 0
    reach = {
        "A": 23333.33,
        "B": 52666.67,
        "C": 37333.33,
        "D": 18000.00,
        "E": 15000.00,
        "F": 31600.00,
        "G": 17066.7
    }
    drone_reach = reach[drone_name]
    if no_recharge:
        drone_reach /= 2
    for loc in loc_dict.keys():
        if get_dist(loc_dict[loc], loc_dict[city_name]) <= drone_reach:
            reachable += pop_dict[loc]
    return reachable


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


def range_check(p1, p2, drn, drop_loc):
    if drop_loc[0] == 'Hima' or drop_loc[0] == 'Fajardo' or drop_loc[0] == 'Children':
        payload_weight = 3
    else:
        payload_weight = 2
    d = get_dist(p1, p2)
    flight_time = drn[1] * drn[2] / (drn[2] + payload_weight)
    drn_range = drn[0] * 1000 * flight_time * 60 / 3600
    vel = drn[0] * 1000 / 3600
    time = d / vel
    if d >= drn_range:
        return False, time
    else:
        return True, time


# drones, defined as [velocity (km/h), flight time (min), weight]
a = [40, 35, 15]
b = [79, 40, 15]
c = [64, 35, 15]
d = [60, 18, 15]
e = [60, 15, 15]
f = [79, 24, 15]
g = [64, 16, 15]
distance_factor = 1.2
no_recharge = True

dronedict = {tuple(a): 'a', tuple(b): 'b', tuple(c): 'c', tuple(d): 'd',
             tuple(e): 'e', tuple(f): 'f', tuple(g): 'g'}

## initialize

# drop locations ['name',[lat,long]] in degrees
alpha = ['Hima', [18.218304, -66.031394]]  #
beta = ['Fajardo', [18.3321123, -65.6501216]]  #
gamma = ['Santurce', [18.444245, -66.0689876]]
delta = ['Children', [18.3965712, -66.1632729]]  #
epsilon = ['Arecibo', [18.4672197, -66.7313808]]

# payload
med1, med2, med3 = 2, 2, 3  ## pounds

ff = open("spanishpopulations.txt", "r")
city_pop = eval(ff.readline())
ff.close()
ff = open("spanishcitycoordinates.txt", "r")
city_map = eval(ff.readline())
ff.close()

ranking = queue.PriorityQueue()

for drone in "ABCDEFG":
    for cargo in "123":
        if cargo == "1":
            drops = [epsilon]
        elif cargo == "2":
            drops = [alpha, gamma, delta]
        else:
            drops = [beta]
        drone_map = {
            "A": a,
            "B": b,
            "C": c,
            "D": d,
            "E": e,
            "F": f,
            "G": g
        }
        drone_data = drone_map[drone]
        good_cities = []
        for city in city_map.keys():
            bad_city = False
            for drop in drops:
                if not range_check(city_map[city], drop[1], drone_data, drop)[0]:
                    bad_city = True
                    break
            if not bad_city:
                good_cities.append(city)

        # score based on recon value
        for city in good_cities:
            score = reachable_population(city_pop, city_map, city, drone)
            ranking.put((score, cargo + drone + " at " + city))

while not ranking.empty():
    print(ranking.get())
