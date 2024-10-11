import numpy as np


def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    sig = lambda x: 1 / (1 + np.exp(-x))
    d_sig = lambda x: x * (1 - x)
    mse = lambda x, y: ((x - y) ** 2).sum() / x.shape[0]
    d_mse = lambda x, y: 2 * (x - y)

    updated_weights = initial_weights
    updated_bias = initial_bias
    mse_values = []
    for i in range(epochs):
        label_preds = sig(features @ updated_weights + updated_bias)
        loss = mse(label_preds, labels)
        mse_values.append(round(loss, 4))

        _dsl = d_sig(label_preds) * d_mse(label_preds, labels)
        dw = (_dsl @ features) / features.shape[0]
        db = _dsl.sum() / features.shape[0]
        print(dw, db)

        updated_weights -= learning_rate * dw
        updated_bias -= learning_rate * db

    return np.round(updated_weights, 4).tolist(), round(updated_bias, 4), mse_values
