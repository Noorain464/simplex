def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def matrix_transpose(matrix):
    m = len(matrix)
    p = len(matrix[0])
    return [[matrix[j][i] for j in range(m)] for i in range(p)]

def multiply(A, B):
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in matrix_transpose(B)] for row_a in A]

def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]

def extend_matrix(matrix, target_size):
    n_rows = len(matrix)
    n_cols = len(matrix[0]) if matrix else 0
    if n_rows < target_size:
        matrix.extend([[0] * n_cols for _ in range(target_size - n_rows)])
    elif n_cols < target_size:
        for row in matrix:
            row.extend([0] * (target_size - n_cols))
    return matrix

def find_pivot_index(matrix, k):
    max_index = k
    max_value = abs(matrix[k][k])
    for i in range(k + 1, len(matrix)):
        if abs(matrix[i][k]) > max_value:
            max_value = abs(matrix[i][k])
            max_index = i
    return max_index

def pldu(M):

    n_rows = len(M)
    n_cols = len(M[0]) if M else 0

    
    if n_rows != n_cols:
        n = max(n_rows, n_cols)
        M = extend_matrix(M, n)

    # Permutation matrix
    n = len(M)
    P = identity_matrix(n)

    # Lower triangular matrix
    L = [[0] * n for _ in range(n)]

    # Upper Triangular matrix
    U = [row[:] for row in M]

    for k in range(n - 1):
        pivot_index = find_pivot_index(U, k)
        pivot_value = U[pivot_index][k]

        if pivot_value == 0:
            print("Zero pivot.")
            return None, None, None, None  

        if pivot_index != k:
            swap_rows(U, k, pivot_index)
            swap_rows(P, k, pivot_index)
            if k > 0:
                swap_rows(L, k, pivot_index)

        for i in range(k + 1, n):
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
    if P is None:
        print("No PLDU decomposition.")
        return
    
    PL = multiply(P, L)
    PLD = multiply(PL, D)
    PLDU = multiply(PLD, U)
    
    if PLDU == matrix:
        print("PLDU equals the original matrix.")
    else:
        print("PLDU does not equal the original matrix.")

matrix = [[0, 0, 2], [2, 1, 2], [1, 2, 1]]
verify_pldu(matrix)
