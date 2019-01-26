f = open("drone_packing_options_2.txt", "r")
packings = set()
for line in f:
    counts = map(int, line.strip().split())
    packings.add(tuple(counts))
print(list(packings))
print(len(packings))
f = open("unique_packings_2.txt", "w")
f.write(str(list(packings)))
