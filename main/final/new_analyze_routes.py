import numpy as np
import queue


def get_dist(p1, p2):
    R = 6.371e6

    lat1 = p1[0]*np.pi/180
    lon1 = p1[1]*np.pi/180
    lat2 = p2[0]*np.pi/180
    lon2 = p2[1]*np.pi/180

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (np.sin(dlat/2))**2 + np.cos(lat1) * np.cos(lat2) * (np.sin(dlon/2))**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    distance = R * c
    return distance


def new_get_route_length(route_cities):
    total = distance_factor * get_dist(route_cities[0], route_cities[-1])
    for iii in range(len(route_cities) - 1):
        total += distance_factor * get_dist(route_cities[iii], route_cities[iii + 1])
    return total


distance_factor = 1.414


def get_cities(locs):
    city_list = []
    for loc in locs:
        city_list.append(cord_map[tuple(loc)])
    return city_list


def get_population(city_list):
    total = 0
    for a_city in city_list:
        total += pop_map[a_city]
    return total


for i in range(3):
    routes = []
    f = open("ordered_route_" + str(i + 1) + ".txt", "r")
    for line in f:
        routes.append(eval(line))
    f.close()
    f = open("spanishcitycoordinates.txt")
    city_map = eval(f.readline())
    f.close()
    f = open("spanishpopulations.txt")
    pop_map = eval(f.readline())
    f.close()
    cord_map = {}
    for city in city_map.keys():
        cord_map[tuple(city_map[city])] = city
    cargo = [[18.4377534, -66.5551326], [18.3612954, -66.1102957], [18.3786196, -65.83933379999999]]
    print("Zone " + str(i + 1) + " routes")
    q = queue.PriorityQueue()
    for route in routes:
        meters = new_get_route_length(route)
        minutes = (60 * meters / 1000) / 79
        cities = get_cities(route[1:])
        population = get_population(cities)
        q.put((-population, meters, minutes, cities, route[1:]))
    fly_time = 0
    times = []
    while not q.empty():
        population, meters, minutes, cities, cords = q.get()
        # print(int(-population), "population")
        # print(str(meters / 1000)[:5], "km")
        # print(str(minutes)[:5], "minutes")
        # for k in range(len(cords)):
        #     print(cities[k])
        #     print(cords[k][0], cords[k][1])

        fly_time += minutes
        times.append(minutes)
    charging_time = 50
    dropping_time = 0
    drone1_time_needed = 0
    drone2_time_needed = 0
    t = 0
    index = 0
    drone1_indicies = []
    drone2_indicies = []
    while t < 11 * 60 and index < len(times):
        if drone1_time_needed <= 0:
            drone1_indicies.append(index)
            drone1_time_needed += times[index] + charging_time + dropping_time
            index += 1
        elif drone2_time_needed <= 0:
            drone2_indicies.append(index)
            drone2_time_needed += times[index] + charging_time + dropping_time
            index += 1
        t += 1
        drone1_time_needed -= 1
        drone2_time_needed -= 1
    if index != len(times):
        print("NO")
    # print("fly time:", int(fly_time))
    # print("total time:", t)
