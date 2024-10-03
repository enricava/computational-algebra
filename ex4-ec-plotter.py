# 4.4 Gráfica de tiempos
# Incluyo dos gráficas, una para n <= 125 y otra para potencias de 2 hasta n = 512

import random as rnd
import matplotlib.pyplot as plt
import time
import gc
m = __import__("ex4")

numdims = []
tiempos = []
tnormal = []

max = 512
n = 1

while n <= max:
    gc.collect()  # para resolver pequeños spikes en la grafica - garbage collector
    A = [[rnd.randint(0, 9) for x in range(0, n)] for x in range(0, n)]
    B = [[rnd.randint(0, 9) for x in range(0, n)] for x in range(0, n)]
    ini = time.time()
    C = m.mult_strassen(A, B)
    fin = time.time()
    numdims += [n]
    t = fin-ini
    tiempos += [t]
    print("n =", n, "tiempo =", t, "[seg]")
    # n += 1
    n *= 2

plt.plot(numdims, tiempos, "b-")
plt.grid(b=True, which='major', axis='both',
         color='r', linestyle='--', linewidth=0.5)
plt.xlabel('n')
plt.ylabel('tiempo [seg]')
# plt.savefig("mult_strassen.png")
plt.show()
plt.clf()
