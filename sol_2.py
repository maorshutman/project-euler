max_fib = 4000000
a = 1
b = 2
s = 0

while b < max_fib:
    tmp = b
    b = b + a
    a = tmp
    if b % 2 == 0:
        s += b

print(s+2)
