f = open("english_city_names.txt", "r")
names = eval(f.readline())
f.close()

for i in range(len(names)):
    if names[i] == "Arecibo, Puerto Rico":  # areicibo
        print("Arecibo:", i)
    if names[i] == "8 Calle 6, Caguas, 00725, Puerto Rico":  # hima
        print("HIMA:", i)
    if names[i] == "Fajardo, Puerto Rico":  # carribean
        print("carribean:", i)
    if names[i] == "Viejo San Juan, San Juan, 00901, Puerto Rico":  # santurce
        print("santurce:", i)
    if names[i] == "Bayamon, Puerto Rico":  # childrens
        print("childrens:", i)

# Arecibo: 10
# childrens: 22
# carribean: 81
# HIMA: 137
# carribean: 140
# santurce: 224

drops = [10, 22, 81, 137, 140, 224]

# as in citycoordinates.txt:
# "18�11'11. 66�04'38., 8 Calle 6, Caguas, 00725, Puerto Rico"
# "Bayam�n, Puerto Rico"

# Animas comunidad, Arecibo Municipio
# Los Panes comunidad, Caguas Municipio
# Luis M. Cintron comunidad, Fajardo Municipio
# San Juan zona urbana, San Juan Municipio
# Bayamon zona urbana, Bayamon Municipio
