import math
from collections import Counter


def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_arith_series_rec(seq, target_length, ints, i):
	if len(seq) == target_length:
		print(seq)
		return

	if (i == len(ints)):
		return
	
	# Keep i'th int.
	if ((len(seq) >= 2) and (seq[-1] - seq[-2] == ints[i] - seq[-1])) or (len(seq) < 2):		
		find_arith_series_rec(seq + [ints[i]], target_length, ints, i+1)

	# Skip i'th int.
	for k in range(i+1, len(ints)):		
		find_arith_series_rec(seq, target_length, ints, k)


def find_arith_series(ints, length=3):
	if len(ints) < length:
		return None
	ints = sorted(ints)
	
	find_arith_series_rec([], length, ints, 0)


def main():

	four_dig_primes = []
	for i in range(1000, 9999):
		if is_prime(i):
			four_dig_primes.append(i)

	sets = {}
	for p in four_dig_primes:
		digits = tuple(sorted([int(c) for c in str(p)]))
		if digits in sets:
			sets[digits].append(p)
		else:
			sets[digits] = [p]

	for digit_set in list(sets.keys()):
		find_arith_series(sets[digit_set])


if __name__ == "__main__":
	main()
