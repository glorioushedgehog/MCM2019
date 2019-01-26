f = open("drone_packing_options_1.txt", "r")
packings = set()
for line in f:
    counts = map(int, line.strip().split())
    packings.add(tuple(counts))
print(packings)
print(len(packings))
