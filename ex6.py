import math

# Criba Eratostenes
MAX = 300
p = [1] * MAX
primos = []
for i in range(2, MAX):
    if p[i]:
        primos += [i]
        for j in range(i*i, MAX, i):
            p[j] = 0

# gcd_binario


# Pollards p-1
def pollard(n, b):
    if (n % 2 == 0):
        return 2
    a = 2
    for x in primos[:b]:
        for i in range(0, math.ceil(math.log(n, x))):
            a = pow(a, x, n)

    d = math.gcd(a-1, n)
    if 1 < d and d < n:
        return d
    return n


def factorize(n, b):
    u = pollard(n, b)
    fs = [u]
    if (n % u == 0 and u != n):
        fs += factorize(n//u, b)
    return fs


N = 1542201487980564464479858919567403438179217763219681634914787749213
b = 100
print(N, 'factorizado pollard con b =', b, ':\n\t', factorize(N, b))
