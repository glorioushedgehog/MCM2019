# height: 14
# count: 594
#
# height: 8
# count: 828
#
# height: 12
# count: 759


def error(n1, n2, n3):
    target = [1, 0, 1]
    t_sum = sum(target)
    guess_sum = n1 * 594 + n2 * 828 + n3 * 759
    t = []
    for num in target:
        t.append(float(num) / t_sum)
    guess = [n1 * 594, n2 * 828, n3 * 759]
    g = []
    for num in guess:
        g.append(float(num) / guess_sum)
    err = 0
    for p in range(3):
        err += abs(t[p] - g[p])
    return err


best = 1000000
best_1 = 0
best_2 = 0
best_3 = 0
for i in range(12):
    for j in range(12):
        for k in range(12):
            if i + j + k == 0:
                continue
            height = i * 14 + j * 8 + k * 12
            if height > (92 - 0):
                continue
            e = error(i, j, k)
            if e < best:
                best = e
                best_1 = i
                best_2 = j
                best_3 = k
print("error:", e)
print(best_1, "layers of MED1", best_1 * 594, "total")
print(best_2, "layers of MED2", best_2 * 828, "total")
print(best_3, "layers of MED3", best_3 * 759, "total")
total_height = best_1 * 14 + best_2 * 8 + best_3 * 12
print("total height:", total_height, "free:", 92 - total_height)
