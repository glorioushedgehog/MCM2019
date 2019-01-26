import re


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


f = open("spanishcitynames.txt", "r")
spanish_names = eval(f.readline())

print(len(spanish_names))

f = open("spanishtoenglish.txt", "r")
name_map = eval(f.readline())
print(len(name_map.keys()))

english_names = []
for name in spanish_names:
    english_names.append(name_map[name])
print(english_names)
f = open("english_city_names.txt", "w")
f.write(str(english_names))
f.close()
population_map = get_city_map()
english_pop_map = {}
for spanish_name in population_map.keys():
    if spanish_name not in name_map:
        print("didn't find", spanish_name)
    english = name_map[spanish_name]
    english_pop_map[english] = population_map[spanish_name]
print(english_pop_map)
f = open("english_pop_map.txt", "w")
f.write(str(english_pop_map))
f.close()
