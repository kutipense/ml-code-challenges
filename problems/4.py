def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    n, m = len(matrix), len(matrix[0])
    if mode == "row":
        means = [sum(row) / len(row) for row in matrix]
    else:  # elif mode=="column"
        means = [sum(matrix[j][i] for j in range(n)) / n for i in range(m)]

    return means
