# (115472.0, '1B at Imbery comunidad, Barceloneta Municipio', [18.4377534, -66.5551326])
# (1073156.0, '2B at Guaynabo zona urbana, Guaynabo Municipio', [18.3612954, -66.1102957])
# (280491.0, '3B at Rio Grande zona urbana, Rio Grande Municipio', [18.3786196, -65.83933379999999])
import numpy as np


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


distance_factor = 1.414
drone_reach = 52666.67
ff = open("spanishpopulations.txt", "r")
city_pop = eval(ff.readline())
ff.close()
ff = open("spanishcitycoordinates.txt", "r")
city_map = eval(ff.readline())
ff.close()
cargo = [[18.4377534, -66.5551326], [18.3612954, -66.1102957], [18.3786196, -65.83933379999999]]
for i in range(3):
    print(i + 1, len(reachable_cities(cargo[i])))

