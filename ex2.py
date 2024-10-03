# 2.4

MAX = 100

v = [1 for x in range(0, MAX)]
vi = [True for x in range(0, MAX)]

# Paso inicial
v[1] += v[0]
v[0] = 0
vi[0] = False
vi[1] = False
i = 1
count = 1

while not all(vi):
    k = (i+1) % MAX
    aux = v[i]
    v[i] = 0
    while aux != 0:
        v[k] += 1
        aux -= 1
        vi[k] = (v[k] == 1)
        k = (k+1) % MAX
    vi[i] = (v[i] == 1)
    i = (k-1) % MAX
    count += 1

print(count)
