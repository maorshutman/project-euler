
def is_perfect_square(x):
    lo = 1
    hi = x+1
    while True:
        sq = (lo + hi) // 2
        diff = sq**2 - x
        if abs(lo - hi) == 1:
            return False, diff, sq
        if diff == 0:
            return True, 0, sq
        if diff > 0:
            hi = sq
        else:
            lo = sq


# https://en.wikipedia.org/wiki/Pell%27s_equation#Solutions
# Pell's eq x^2  = 1 + n * y^2
# For n = 8, the fundamental solution is y = 1 , x = 3.

y1 = 1
x1 = 3
x = x1
y = y1

for i in range(20):
    tmpx = x
    x = x1 * x + 8 * y1 * y
    y = x1 * y + y1 *  tmpx
    assert is_perfect_square(8*y**2 + 1)[0]

    red = y
    blue = 0.5 + red + 0.5 * is_perfect_square(8*red**2 + 1)[2]

    if red + blue >= 1e12:
        print(x, y)
        print( is_perfect_square(8 * y**2 + 1))
        break
