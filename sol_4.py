
def is_pal(n: int):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

m = 1
for i in range(1, 1000):
    for j in range(i, 1000):
        prod = i*j
        if is_pal(prod) and prod > m:
            m = prod
            print(m)

print(m)
