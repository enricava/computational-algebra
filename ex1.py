# 1.5

#
#   Voy a hacer el ejercicio de forma no eficiente y de forma eficiente
#   y comparar el tiempo usado
#

import math
import time

t0 = time.time()

# a) Forma no eficiente pero directa de implementar :
# n := constante de Champernowne construida con los primeros l enteros

n = '.'
l = 1000000
for i in range(1, l+1):
    n += str(i)


i = 1
x = 1
while i < 1000000:
    x *= int(n[i])
    i *= 10

print('Resultado metodo no eficiente:', x)  # solucion
t1 = time.time()

# b) Forma mas eficiente, generando solo los numeros que aportan la cifra
# buscada

# Los digitos que buscamos son 1, 10, 100..
#   Creo un vector con digitos buscados para simplificar
x = 1
d = []
for j in range(0, 7):
    d += [10**j]

i = 1
t = 9
c = 9
v = [9]
while t < 1000000:
    i += 1
    c = c*10
    t = (c * i) + t
    v += [t]  # vector con posiciones de los digitos

x = 1 * 1  # estas las conocemos ya del enunciado
k = 0
for i in range(2, 7):
    while (v[k+1] < d[i]):
        k += 1

    # t es el numero que contiene el digito que buscamos
    #   se calcula contando, desde el ultimo bloque v[k] cuantos digitos nos
    #   quedan sabiendo que el primer numero del bloque es 10**(k+1)
    t = math.floor((d[i] - v[k])/i) + 10**(k+1)

    # s indica posicion del digito: 0 ultima, 1 primera, 2 segunda..
    s = (d[i] - v[k]) % i
    if (s == 0):
        f = t % 10
    else:
        f = int(str(t)[s-1])
    x *= f

print('Resultado metodo eficiente:', x)  # solucion

t2 = time.time()
print('Tiempo usado metodo no eficiente:', t1-t0, 'segundos')
print('Tiempo usado metodo eficiente:', t2-t1, 'segundos')
