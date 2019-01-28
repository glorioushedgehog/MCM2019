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


drone_reach_og = 52666.67 / 2
drone_weight = 11
# zone 1
start = [18.4377534, -66.5551326]
print("Arecibo")
drop = [18.4672197, -66.7313808]  # Arecibo
d = get_dist(start, drop)
added_weight = 2
drone_reach = drone_reach_og * drone_weight / (drone_weight + added_weight)
print("time:", 2*60 * (d / 1000) / 79)
if d > drone_reach:
    print("cannot reach")
else:
    print("reach")

# zone 2
start = [18.3612954, -66.1102957]
print("HIMA")
drop = [18.218304, -66.031394]  # HIMA
d = get_dist(start, drop)
added_weight = 4
drone_reach = drone_reach_og * drone_weight / (drone_weight + added_weight)
print("time:", 2*60 * (d / 1000) / 79)
if d > drone_reach:
    print("cannot reach")
else:
    print("reach")

print("Santurce")
drop = [18.444245, -66.0689876]  # Santurce
d = get_dist(start, drop)
added_weight = 2
drone_reach = drone_reach_og * drone_weight / (drone_weight + added_weight)
print("time:", 2*60 * (d / 1000) / 79)
if d > drone_reach:
    print("cannot reach")
else:
    print("reach")

print("Children")
drop = [18.3965712, -66.1632729]  # Children
d = get_dist(start, drop)
added_weight = 6
drone_reach = drone_reach_og * drone_weight / (drone_weight + added_weight)
print("time:", 2*60 * (d / 1000) / 79)
if d > drone_reach:
    print("cannot reach")
else:
    print("reach")

# zone 3
start = [18.3786196, -65.83933379999999]
print("Carribean (Fajardo)")
drop = [18.3321123, -65.6501216]  # Carribean (Fajardo)
d = get_dist(start, drop)
added_weight = 3
drone_reach = drone_reach_og * drone_weight / (drone_weight + added_weight)
print("time:", 2*60 * (d / 1000) / 79)
if d > drone_reach:
    print("cannot reach")
else:
    print("reach")
