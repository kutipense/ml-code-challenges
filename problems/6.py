def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

    # (a-lambda) * (d-lambda) - bc = 0
    # ad - dlambda -alambda lambda^2 -bc = 0
    # lambda^2 - (a+d)lambda + ad - bc = 0

    tr = a + d
    det = a * d - b * c

    disc_root = (tr * tr - 4 * det) ** 0.5

    root0 = (tr + disc_root) / 2
    root1 = (tr - disc_root) / 2

    eigenvalues = sorted((root0, root1))[::-1]
    return eigenvalues
