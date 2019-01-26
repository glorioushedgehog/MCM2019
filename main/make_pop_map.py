import re


def reachable_population():
    pass


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


city_pop = get_city_map()
print(len(city_pop.keys()))
f = open("spanishcitycoordinates.txt", "r")
city_map = eval(f.readline())
f.close()
print(len(city_map.keys()))

for city in city_pop.keys():
    if city not in city_map:
        print(city)

for city in city_map.keys():
    if city not in city_pop:
        print(city)
pop_map = {}
for city in city_map.keys():
    pop_map[city] = city_pop[city]

f = open("spanishpopulations.txt", "w")
f.write(str(pop_map))
f.close()
