import random as rnd
# los gcd vistos en clase llegan al limite de recursion para 1000 cifras
from math import gcd

# implementacion del metodo de Jacobi O(loga logn) del campus (Javier)
# esta implementacion es casi identica a la de johndcook.com


def jacobi(a, n):
    r = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 == 3 or n % 8 == 5:
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    if n == 1:
        return r
    else:
        return 0

# iteracion unica del algoritmo de solovay strassen


def solovay_strassen(n):
    a = rnd.randint(1, n-1)
    if gcd(a, n) != 1 or pow(a, (n-1)//2, n) != jacobi(a, n) % n:
        # si gcd(a,n) != 1 termina directamente porque el 'or' deja de comprobar
        return False
    else:
        return True


def test_solovay_strassen(n, k):
    for i in range(k):
        if not solovay_strassen(n):  # si algun test falla, terminar
            return False
    return True


def generar_candidato(n):
    if n == 1:
        return rnd.choice([1, 2, 3, 5, 7, 9])

    candidato = rnd.randint(1, 9)
    for i in range(n-2):
        candidato = candidato * 10 + rnd.randint(0, 9)

    candidato = candidato * 10 + rnd.choice([1, 3, 7, 9])
    return candidato


def generar_primo(n, k):
    cnt = 0
    found = False
    candidato = generar_candidato(n)
    while not found:
        cnt += 1
        if test_solovay_strassen(candidato, k):  # aplicamos k tests al candidato
            found = True
        else:
            # avanzamos de 2 en 2 para evitar numeros pares
            candidato = generar_candidato(n)

    return (candidato, cnt)


def generar_histograma():
    import matplotlib.pyplot as plt
    from tqdm import tqdm  # libreria muy interesante para hacer barras de carga en bucles
    resultados = []
    simulaciones = 500  # 500 simulaciones 13 minutos
    # for con barra de carga, si no tienes la libreria simplemente elimina 'tqdm(.)'
    for i in tqdm(range(simulaciones)):
        resultados += [generar_primo(300, 200)[1]]

    plt.xlabel('Valor de cnt')
    plt.ylabel('Repeticiones')
    plt.hist(resultados, bins=50)
    plt.savefig('histograma.png')  # plt.plot no me funciona en linux
