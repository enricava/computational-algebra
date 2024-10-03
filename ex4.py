# 4.4

def partition(X):  # divide X en 4 submatrices
    n = len(X)
    a, b, c, d = ([] for i in range(4))
    for i in range(0, n//2):
        a.append(X[i][:n//2])
        b.append(X[i][n//2:])
        c.append(X[i+n//2][:n//2])
        d.append(X[i+n//2][n//2:])
    return a, b, c, d


def op(X, Y, o=0):  # default o = 0: suma, else resta
    n = len(X)
    r = [[0 for x in range(0, n)] for x in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            if o == 0:
                r[i][j] = X[i][j] + Y[i][j]
            else:
                r[i][j] = X[i][j] - Y[i][j]
    return r


def pack(A, B, C, D):  # junta submatrices en matriz
    res = []
    for i in range(len(A)):
        l = A[i] + B[i]
        res.append(l)
    for i in range(len(A)):
        l = C[i] + D[i]
        res.append(l)
    return res


def mult_strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0]*B[0][0]]]
    if n % 2 != 0:
        A = [x + [0] for x in A]
        B = [x + [0] for x in B]
        A.append([0 for x in range(0, n+1)])
        B.append([0 for x in range(0, n+1)])

    A11, A12, A21, A22 = partition(A)
    B11, B12, B21, B22 = partition(B)

    M1 = mult_strassen(op(A11, A22), op(B11, B22))
    M2 = mult_strassen(op(A21, A22), B11)
    M3 = mult_strassen(A11, op(B12, B22, 1))
    M4 = mult_strassen(A22, op(B21, B11, 1))
    M5 = mult_strassen(op(A11, A12), B22)
    M6 = mult_strassen(op(A21, A11, 1), op(B11, B12))
    M7 = mult_strassen(op(A12, A22, 1), op(B21, B22))

    C11 = op(M1, op(M4, op(M7, M5, 1)))
    C12 = op(M3, M5)
    C21 = op(M2, M4)
    C22 = op(M1, op(M3, op(M6, M2, 1)))

    C = pack(C11, C12, C21, C22)

    if n % 2 != 0:
        del C[n]
        for i in range(n):
            del C[i][n]
    return C
