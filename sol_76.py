
cache = {
    (1,1): 1,
    (2,1): 1,
    (2,2): 1,
}

def compute_n_max_k(n, k, cache):
    snk = 0
    for i in range(1, min(k, n-k)+1):
        snk += cache[(n-k, i)]
    cache[(n, k)] = snk


N = 100

for n in range(3, N + 1):
    for i in range(1, n):
        compute_n_max_k(n, i, cache)
    cache[n, n] = 1

tot = 0
for k in range(1, N):
    tot += cache[(N, k)]

print(tot)
