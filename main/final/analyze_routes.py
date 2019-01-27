for i in range(3):
    routes = []
    f = open("route" + str(i + 1), "r")
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
    f = open("ordered_route_" + str(i + 1) + ".txt", "w")
    for route in routes:
        for j, loc in enumerate(route):
            if loc in cargo:
                cargo_index = j
        new_route = []
        for p in range(cargo_index, len(route)):
            new_route.append(route[p])
        for k in range(cargo_index):
            new_route.append(route[k])
        f.write(str(new_route) + "\n")
    f.close()
