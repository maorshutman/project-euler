
def count(r, c):
    tot = 0
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            tot += (r - i + 1) * (c - j + 1)
    return tot


area = 1
min_dist = 1000000000
dims = None

for r in range(1, 200):
    for c in range(r, 200):
        tot_rc = count(r, c)
        dist = abs(tot_rc - 2000000)
        if dist <=  min_dist:
            area = r*c
            min_dist = dist
            dims = (r, c)

print(area, min_dist, dims)
