import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows, cols = np.array(A).shape
    A_T = np.zeros((cols, rows))

    for row_idx in range(len(A)):
        for col_idx in range(len(A[row_idx])):
            A_T[col_idx][row_idx] = A[row_idx][col_idx]

    return A_T
