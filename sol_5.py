import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


N = 20
primes = [2, 3, 5, 7, 11, 13, 17, 19]

counter = {p: 0 for p in primes}
for i in range(2, N):
    if is_prime(i):
        counter[i] += 1
    else:
        fs = factors(i)
        hist = {p: 0 for p in primes}
        for f in fs:
            hist[f] += 1
        for p in primes:
            if hist[p] > counter[p]:
                counter[p] = hist[p]

sum = 1
for p, count in counter.items():
    sum *= p**count

print(sum)
