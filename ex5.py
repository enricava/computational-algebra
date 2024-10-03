# gcd binario extraido de las notas
def gcd_binario(x, y):    # (x,y) != (0,0)
    x = abs(x)
    y = abs(y)
    xespar = x % 2 == 0
    yespar = y % 2 == 0
    if x == 0:           # caso base: gcd(0,y)=y
        m = y
    elif y == 0:         # caso base: gcd(x,0)=x
        m = x
    elif xespar and yespar:
        m = 2 * gcd_binario(x//2, y//2)
    elif xespar:
        m = gcd_binario(x//2, y)
    elif yespar:
        m = gcd_binario(x, y//2)
    elif x > y:
        m = gcd_binario(y, x-y)
    else:
        m = gcd_binario(x, y-x)
    return m


def esCarmichael(N):
    for a in range(2, N):
        if gcd_binario(a, N) == 1 and pow(a, N-1, N) != 1:
            return False
    return True


# probaremos suficientes numeros compuestos para obtener 10 Carmichael numbers
# si buscamos mas numeros, tendriamos que crear una funcion extender_criba
n = 30000
p = [1]*n  # criba de Eratostenes
for i in range(2, n):
    if p[i]:
        for m in range(i + i, n, i):
            p[m] = 0
c = 0
x = 2
v = []
while c < 10:
    if p[x] == 0 and esCarmichael(x):
        v += [x]
        c += 1
    x += 1
print(v)
