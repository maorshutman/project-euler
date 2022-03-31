# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


n = 600851475143

primes = []
for i in range(2, 100000):
    if is_prime(i):
        primes.append(i)
    if len(primes) == 1000:
        break

lpf = 1
for p in primes:
    if n%p==0:
        lpf = p
        n /= p
    print(n)
    if n == 1:
        print("DONE")
        break

print(lpf)