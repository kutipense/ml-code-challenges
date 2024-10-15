def matrixmul(
    a: list[list[int | float]], b: list[list[int | float]]
) -> list[list[int | float]]:
    h0, w0 = len(a), len(a[0])
    h1, w1 = len(b), len(b[0])

    if w0 != h1:
        return -1

    c = [[0 for i in range(w1)] for j in range(h0)]

    for i in range(h0):
        for j in range(w0):
            for k in range(w1):
                c[i][k] += a[i][j] * b[j][k]

    return c
