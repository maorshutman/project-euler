# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


def get_digit_hist(n: int):
    hist = [0]*10
    for c in str(n):
        hist[int(c)] += 1
    return hist


def has_prop(n):
    for i in range(2, 7):
        if hist != get_digit_hist(i * n):
            return False
    return True


for n in range(1, 100000000):
    hist = get_digit_hist(n)
    if has_prop(n):
        print(n)
        break
