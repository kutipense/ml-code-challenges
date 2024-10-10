import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = np.zeros(len(b))

    a_diag_inv = 1 / np.diag(A)
    _A = A - np.diag(np.diag(A))

    for _ in range(n):
        x = a_diag_inv * (b - _A @ x)

    return x
