class Location:

    def req_string(self):
        num_med_1 = str(self.reqs[0])
        num_med_2 = str(self.reqs[1])
        num_med_3 = str(self.reqs[2])
        return num_med_1 + " MED1, " + num_med_2 + " MED2, " + num_med_3 + " MED3"

    def __init__(self, name, lat, lon, reqs):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.reqs = reqs

    def __str__(self):
        return self.name + \
               " at " \
               + str(self.lat) + \
               ", " + str(self.lon) + \
               " which needs " + \
               self.req_string()

locations = []
locations.append(Location("Caribbean Medical Center, Jajardo",
                          18.33,
                          -65.65,
                          [1, 0, 1]))

locations.append(Location("Hospital HIMA, San Pablo",
                          18.22,
                          -66.03,
                          [2, 0, 1]))

locations.append(Location("Hospital Pavia Santurce, San Juan",
                          18.44,
                          -66.07,
                          [1, 1, 0]))

locations.append(Location("Puerto Rico Children's Hospital, Bayamon ",
                          18.40,
                          -66.16,
                          [2, 1, 2]))

locations.append(Location("Hospital Pavia Arecibo, Arecibo",
                          18.47,
                          -66.73,
                          [1, 0, 0]))

for loc in locations:
    print(loc)

