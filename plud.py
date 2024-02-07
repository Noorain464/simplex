def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def matrix_transpose(matrix):
    m = len(matrix)
    p = len(matrix[0])
    return [[matrix[j][i] for j in range(m)] for i in range(p)]

def multiply(A,B):
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in matrix_transpose(B)] for row_a in A]

def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]


def pldu(M):
    n = len(M)
    # Permutation matrix
    P = identity_matrix(n)

    # Lower triangular matrix
    L = [[0] * n for _ in range(n)]

    # Upper Triangular matrix
    U = [row[:] for row in M]

    for k in range(n-1):
        
        pivot_index = max(range(k, n), key=lambda i: abs(U[i][k]))
        if pivot_index != k:
            
            swap_rows(U, k, pivot_index)
            swap_rows(P, k, pivot_index)
            if k > 0:
                swap_rows(L, k, pivot_index)

        for i in range(k+1, n):
            factor = U[i][k] / U[k][k]
            U[i] = [U[i][j] - factor * U[k][j] for j in range(n)]
            L[i][k] = factor

    
    for i in range(n):
        L[i][i] = 1

    # Diagonal matrix
    D = [[U[i][i] for i in range(n)]]

   
    for i in range(n):
        U[i][i] = 1

    return P, L, D, U

def verify_pldu(matrix):
    P, L, D, U = pldu(matrix)
    PL = multiply(P, L)
    PLD = multiply(PL, D)
    PLDU = multiply(PLD, U)
    multiplied_matrix = PLDU

    if multiplied_matrix == matrix:
        print("PLDU equals the original matrix.")
    else:
        print("PLDU not equal to the original matrix.")
matrix = [[2, 1, 3], [4, 2, 6], [7, 8, 9]]
verify_pldu(matrix)