# (115472.0, '1B at Imbery comunidad, Barceloneta Municipio', [18.4377534, -66.5551326])
# (1073156.0, '2B at Guaynabo zona urbana, Guaynabo Municipio', [18.3612954, -66.1102957])
# (280491.0, '3B at Rio Grande zona urbana, Rio Grande Municipio', [18.3786196, -65.83933379999999])
import numpy as np
import itertools


def convex_hull_graham(points):
    '''
    Returns points on convex hull in CCW order according to Graham's scan algorithm.
    By Tom Switzer <thomas.switzer@gmail.com>.
    '''
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = []
    for x in points:
        l = _keep_left(l, x)
    u = []
    for x in reversed(points):
        u = _keep_left(u, x)
    # l = reduce(_keep_left, points, [])
    # u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l


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


def reachable_cities(cargo_cords):
    reachable = []
    for a_city in city_map.keys():
        dist = distance_factor * get_dist(cargo_cords, city_map[a_city])
        if dist < drone_reach:
            reachable.append(a_city)
    return reachable


def list_equals(l1, l2):
    if len(l1) != len(l2):
        return False
    for index in range(len(l1)):
        if l1[index] != l2[index]:
            return False
    return True


def reduce_cities():
    temp_map = {}
    global city_map
    unique_cities = set(city_map.keys())
    old_cities = list(city_map.keys())
    for ii in range(len(old_cities) - 1):
        for jj in range(ii + 1, len(old_cities)):
            if list_equals(city_map[old_cities[ii]], city_map[old_cities[jj]]):
                if old_cities[ii] in unique_cities and old_cities[jj] in unique_cities:
                    unique_cities.remove(old_cities[ii])
            else:
                a_distance = distance_factor * get_dist(city_map[old_cities[ii]], city_map[old_cities[jj]])
                if a_distance < min_distance:
                    if old_cities[ii] in unique_cities and old_cities[jj] in unique_cities:
                        unique_cities.remove(old_cities[ii])
    for city in unique_cities:
        temp_map[city] = city_map[city]
    city_map = temp_map


def get_route_length(start_coords, route_cities):
    total = distance_factor * get_dist(start_coords, city_map[route_cities[0]])
    for iii in range(len(route_cities) - 1):
        total += distance_factor * get_dist(city_map[route_cities[iii]], city_map[route_cities[iii + 1]])
    total += distance_factor * get_dist(start_coords, city_map[route_cities[-1]])
    return total


def trip_length(start_city, candidates):
    min_dist = 10000000000
    for perm in itertools.permutations(candidates):
        a_trip_length = get_route_length(start_city, perm)
        if a_trip_length < min_dist:
            min_dist = a_trip_length
    return min_dist


min_distance = 500
distance_factor = 1.414
drone_reach = 52666.67 / 2
ff = open("spanishpopulations.txt", "r")
city_pop = eval(ff.readline())
ff.close()
ff = open("spanishcitycoordinates.txt", "r")
city_map = eval(ff.readline())
ff.close()
reduce_cities()
cargo = [[18.4377534, -66.5551326], [18.3612954, -66.1102957], [18.3786196, -65.83933379999999]]
unique_options = set()


def get_routes(start, cities):
    route_list = []
    while cities:
        first_city = cities.pop()
        current_route = [first_city]
        while True:
            current_route_length = 10000000
            best_new_city = ''
            for an_city in cities:
                current_route.append(an_city)
                candidate_length = trip_length(start, current_route)
                if candidate_length > drone_reach * 2:
                    current_route = current_route[:-1]
                    continue
                if candidate_length < current_route_length:
                    best_new_city = an_city
            if best_new_city == '':
                break
            current_route.append(best_new_city)
            cities.remove(best_new_city)
        route_list.append(current_route)
    return route_list


def get_coords(places):
    lis = []
    for place in places:
        lis.append(city_map[place])
    return lis


def new_get_route_length(route_cities):
    total = distance_factor * get_dist(route_cities[0], route_cities[-1])
    for iii in range(len(route_cities) - 1):
        total += distance_factor * get_dist(route_cities[iii], route_cities[iii + 1])
    return total


def new_get_routes(start, city_locs):
    candidate_route = [start, city_locs.pop()]
    while start in candidate_route and new_get_route_length(candidate_route) < (drone_reach*2):
        last = city_locs.pop()
        candidate_route.append(last)
        candidate_route = convex_hull_graham(candidate_route)
    old_len = len(candidate_route)
    candidate_route.remove(last)
    if len(candidate_route) != old_len - 1:
        print("removal didn't work")
    print("route", len(candidate_route))
    candidate_route = convex_hull_graham(candidate_route + [start])
    return [candidate_route]








    route_list = []
    route = [start]
    while city_locs:
        last_success_ago = 0
        candidate = city_locs[0]
        candidate_route = convex_hull_graham(route + [candidate])
        if start in candidate_route and new_get_route_length(candidate_route) < drone_reach:
            route.append(city_locs.pop())
            last_success_ago = 0
        if last_success_ago > len(city_locs):
            route_list.append(route)
            route = [start]
        last_success_ago += 1
    return route_list


for i in range(3):
    options = reachable_cities(cargo[i])
    for o in options:
        unique_options.add(tuple(o))
    print(i + 1, len(options))
    distances = []
    for j in range(len(options)):
        for k in range(len(options)):
            if j == k:
                continue
            distance = distance_factor * get_dist(city_map[options[j]], city_map[options[k]])
            distances.append(distance)
    print(cargo[i])
    option_coords = get_coords(options)
    routes = new_get_routes(cargo[i], option_coords)
    for route in routes:
        print(route)
        print("route length:", new_get_route_length(route))


print(len(unique_options), "reachable cities total")

