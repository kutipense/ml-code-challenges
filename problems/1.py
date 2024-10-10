def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:
    if not a or len(a[0]) != len(b):
        return -1

    c = [sum(j * k for j, k in zip(i, b)) for i in a]

    return c
