import math


def get_pentagonal_numbers(n):
    pent_nums = {}
    for i in range(1, n+1):
        pent_nums[i] = int(i * (3 * i - 1) / 2)
        pent_nums[-i] = int(-i * (-3 * i - 1) / 2)
    return pent_nums


def main():
    """ Use the Pentagonal Number Theorem.
    """

    g = get_pentagonal_numbers(10000)

    p = {
        0: 1,
        1: 1,    
    }

    for n in range(2, 100000):
        pn = 0
        k = 1
        
        while True:            
            if (n - g[k]) < 0:
                break
            pn += (int((-1)**(k-1))) * p[n - g[k]]

            if (n - g[-k]) < 0:
                break
            pn += (int((-1)**(-k-1))) * p[n - g[-k]]

            k += 1

        p[n] = pn
        print(f"{n} -> {pn}")

        if p[n] % 1000000 == 0:
            print(f"Found : {n}")
            break


if __name__ == "__main__":
    main()
