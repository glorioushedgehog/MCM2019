import math


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


f = open("citycoordinates.txt", "r")
line = f.readline()
city_map = eval(line)
matrix = []
num_cities = len(city_map.keys())
city_list = list(city_map.keys())
for _ in range(num_cities):
    temp = [-1] * num_cities
    matrix.append(temp)

for i in range(num_cities):
    for j in range(num_cities):
        city1 = city_list[i]
        city2 = city_list[j]
        distance = get_dist(city_map[city1], city_map[city2])
        matrix[i][j] = distance

print(matrix[0])
f = open("crow_distance_matrix.txt", "w")
for line in matrix:
    f.write(str(line) + "\n")
f.close()
