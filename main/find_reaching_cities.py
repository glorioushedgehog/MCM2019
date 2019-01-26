f = open("crow_distance_matrix.txt", "r")
distance = []
for line in f:
    distance.append(eval(line))

"Arecibo, Puerto Rico"  # areicibo
"8 Calle 6, Caguas, 00725, Puerto Rico"  # hima
"Fajardo, Puerto Rico"  # carribean
"Viejo San Juan, San Juan, 00901, Puerto Rico"  # santurce
"Bayamon, Puerto Rico"  # childrens
