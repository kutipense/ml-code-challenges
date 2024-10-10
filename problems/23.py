import math


def softmax(scores: list[float]) -> list[float]:
    exps = [math.exp(score) for score in scores]
    s_exps = sum(exps)
    probabilities = [round(e / s_exps, 4) for e in exps]
    return probabilities
