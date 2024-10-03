# 3.4

#
# Puedes ganar si puedes ganar para un conjunto de n-1, n-2 o n-6 piedras
# Tengo una lista con los resultados posibles al jugar con 0,1,2..6 piedras
# Cuando pruebo con 7 piedras, solo me interesan los resultados de jugar con
# 1,2,3..7 piedras
# Asi, puedo hacer programacion dinamica con una lista de tamaño 7
# O(n) en tiempo y O(1) en espacio

import time


def es_posible_ganar_con_n_piedras(n):
    t0 = time.time()
    g = [1, 0, 1, 1, 0, 1, 1]
    if 0 <= n < 6:
        print('Resultado para', n,
              'piedras  es [', bool(g[n]), '] en :', 0, 'segundos')
        return
    for i in range(7, n+1):
        g.append(not (g[1]) or not (g[5]) or not (g[6]))
        # Por qué he puesto ese "not":
        # En esencia, g nos dice si podemos ganar cuando es nuestro turno.
        #   Cuando quitamos una piedra, es el turno de nuestro adversario, así
        #   que queremos saber que su turno *no* tiene estrategia ganadora.
        del g[0]

    t1 = time.time()
    print('Resultado para', n, 'piedras  es [', bool(
        g[len(g)-1]), '] en :', t1-t0, 'segundos')


for i in range(1, 11):
    es_posible_ganar_con_n_piedras(i)

n = 10**6
es_posible_ganar_con_n_piedras(n)
