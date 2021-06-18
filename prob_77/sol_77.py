import math


def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_primes_up_to(n):
    primes = []
    for k in range(2, n):
        if is_prime(k):
            primes.append(k)
    return primes


def count_possible_sums(
    target, 
    primes, 
    curr_sum,
    seq, 
    found_sets,
    cache
):

    seq_tup_rep = seq_to_tuple_rep(seq)

    if curr_sum == target:
        if seq_tup_rep not in found_sets:
            found_sets.add(seq_tup_rep)

        last = seq.pop()
        curr_sum -= last
        return

    for i, p in enumerate(primes):
        if target < (p + curr_sum):
            break
        else:
            # Use cached sets if exit.
            remainder = target - curr_sum
            if remainder in cache:
                for cached_set in cache[remainder]:
                    merged = merge(seq_tup_rep, cached_set)
                    found_sets.add(merged)

            else:
                count_possible_sums(
                    target, 
                    primes, 
                    curr_sum + p,
                    seq + [p],
                    found_sets,
                    cache
                )


def seq_to_tuple_rep(seq):
    seq_dict = dict()
    
    for p in seq:
        if p in seq_dict:
            seq_dict[p] += 1
        else:
            seq_dict[p] = 1

    seq_str_rep = dict_to_tuple(seq_dict)
    
    return seq_str_rep


def dict_to_tuple(d):
    keys = sorted(d.keys())
    pairs = []
    for key in keys:
        pairs.append((key, d[key]))
    return tuple(pairs)


def tuple_to_dict(pairs):
    d = {}
    for pair in pairs:
        d[pair[0]] = pair[1]
    return d


def merge(tup_1, tup_2):
    merged = []

    d_1 = tuple_to_dict(tup_1)
    d_2 = tuple_to_dict(tup_2)    
    
    d = {}

    for key in d_1.keys():
        if key in d:
            d[key] += d_1[key]
        else:
            d[key] = d_1[key]

    for key in d_2.keys():
        if key in d:
            d[key] += d_2[key]
        else:
            d[key] = d_2[key]
 
    return dict_to_tuple(d)


def main():
    """ We solve this problem using dynamic programming.
    """

    target = 75
    primes = get_primes_up_to(target)
    
    found_sets = set()
    cache = dict()

    # We represent a possible sum is the form: ((p1, n1), (p2, n2), ...), 
    # where p1, p2, .. are primes, and n1, n2, ... are the number of times 
    # each of them appears in the sum. This representation allows us to use sets
    # since they are hashable.
    
    # Initilize cache with trivial cases:
    cache = {
        2: {((2, 1),)},
        3: {((3, 1),)}, 
        4: {((2, 2),)},
    }

    for n in range(5, target + 1):
        seq = []
        found_sets = set()

        count_possible_sums(n, primes, 0, seq, found_sets, cache)

        cache[n] = set()
        for tup in found_sets:
            cache[n].add(tup)

        print(n, "->" , len(cache[n]))


if __name__ == "__main__":
    main()
