def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    means = [sum(i) / len(i) for i in vectors]
    _vectors = [[v - mean for v in vec] for vec, mean in zip(vectors, means)]

    cov = [[0] * len(vectors) for i in range(len(vectors))]
    for i in range(len(cov)):
        for j in range(len(cov)):
            v0, v1 = _vectors[i], _vectors[j]
            cov[i][j] = sum(p1 * p2 for p1, p2 in zip(v0, v1)) / (len(v0) - 1)

    return cov
