def k_means_clustering(
    points: list[tuple[float, float]],
    k: int,
    initial_centroids: list[tuple[float, float]],
    max_iterations: int,
) -> list[tuple[float, float]]:
    p_dim = len(points[0])
    sqr_dist = lambda p0, p1: sum((i - j) ** 2 for i, j in zip(p0, p1))
    sum_p = lambda p0, p1: tuple(i + j for i, j in zip(p0, p1))
    div_p = lambda p0, k: tuple(round(i / k, 4) for i in p0)

    centroids = initial_centroids

    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]
        for p in points:
            dist = float("inf")
            index = -1
            for i, centroid in enumerate(centroids):
                _dist = sqr_dist(p, centroid)
                if _dist < dist:
                    dist = _dist
                    index = i
            clusters[index].append(p)

        for index, cluster in enumerate(clusters):
            p_sum = [0] * p_dim
            for p in cluster:
                p_sum = sum_p(p_sum, p)
            p_avg = div_p(p_sum, len(cluster))
            centroids[index] = p_avg

    final_centroids = centroids

    return final_centroids
