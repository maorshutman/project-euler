
def compute_sqrt(x: int, digits: 10):
    a = 1
    while True:
        if a**2 < x:
            a += 1
        else:
            a -= 1
            break

    m = a * 10
    for i in range(digits):
        for _ in range(10):
            len_b = len(str(m)) - len(str(a))
            if m**2 > x * 10**(2*len_b):
                break
            m += 1

        m -= 1
        m *= 10

    return m


sum = 0
for i in range(2, 100):
    if i not in [4, 9, 16, 25, 36, 49, 64, 81]:
        digits = str(compute_sqrt(i, digits=99))
        for j in range(100):
            sum += int(digits[j])

        print(i, digits, ".", i**0.5)

print(sum)
