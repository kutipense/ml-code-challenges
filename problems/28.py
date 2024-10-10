import numpy as np


def svd_2x2(A: np.ndarray) -> tuple:
    # solve det(A - Iλ) = 0 for eigens
    # [a b] -> [a-λ b]
    # [c d] -> [c d-λ]
    # det(A) = (a-λ * d-λ) - b*c
    # 		   = λ**2 -(a+d)*λ + a*d-b*c

    aaT = A @ A.T
    a, b, c, d = aaT.flatten().tolist()
    e_vals = np.roots([1, -(a + d), (a * d - b * c)])
    s = np.diag(e_vals) ** 0.5

    # (A - Iλ)x = 0 for eigen vecs
    # [a-λ b] [x0] -> x0*(a-λ) + x1*b = 0
    # [c d-λ] [x1] -> x0*c + x1*(d-λ) = 0

    u = np.zeros((2, 2))
    for i, e_val in enumerate(e_vals):
        u[:, i] = -aaT[0, 1] / (aaT[0, 0] - e_val), 1

    u = u / np.linalg.norm(u, axis=0)

    # vT = s⁻¹ @ u⁻¹ @ A
    vT = np.linalg.inv(s) @ u.T @ A

    return (u, s.diagonal(), vT)
