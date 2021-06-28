
def mod_geometric(n, b, m):
    T = 1
    e = b % m
    total = 0

    while n > 0:
        if n & 1:
            total = (e * total + T) % m
    
        T = ((e + 1) * T) % m
        e = (e * e) % m
        n >>= 1
        
    return total


def compute_s(n, m=1000000007):

    s = 0

    for k in range(1, n + 1):
        print(k)

        q = 1 - k**2

        s += (mod_geometric(n, q, m) * (q % m)) % m

    return s % m


def main():
    """ We use the following realtions between the roots of a cubic equation
    and its coefficients:
    
    a * x^3 + b * x^2 + c * x+ d = 0 
    
    q + r + p = -b/a
    qrp = -d/a
    qr + pr + qp = c/a

    Then:

    (q + r) * (p + r) * (p + q) = -rpq + (p + r + q) * (c/a) 
                                = d/a - (cb)/(a^2) 
                                = 1 - k^2

    """

    print(compute_s(1000000))


if __name__ == "__main__":
    main()
