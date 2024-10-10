import numpy as np


def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    aTa = A.T @ A
    U = np.eye(2)
    V = np.eye(2)

    while True:
        a00, a01, a10, a11 = aTa.flatten().tolist()

        if np.isclose(a01, 0) and np.isclose(a10, 0):
            break

        if abs(a01) > abs(a10):
            th = 0.5 * np.arctan2(2 * a01, a00 - a11)
        else:
            th = 0.5 * np.arctan2(2 * a10, a11 - a00)

        J = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
        aTa = J.T @ aTa @ J
        U = U @ J
        V = V @ J.T

    S = np.diag(aTa) ** 0.5

    return U, S, V
