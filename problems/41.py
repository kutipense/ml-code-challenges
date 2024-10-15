import numpy as np


def simple_conv2d(
    input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int
):
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    output_height = int((input_height + 2 * padding - kernel_height) / stride) + 1
    output_width = int((input_width + 2 * padding - kernel_width) / stride) + 1
    output_matrix = np.zeros((output_height, output_width))

    k = 0
    for h in range(-padding, input_height - kernel_height + 1 + padding, stride):
        t = 0
        for w in range(-padding, input_width - kernel_width + 1 + padding, stride):
            for i in range(kernel_height):
                for j in range(kernel_width):
                    if h + i < 0 or w + j < 0:
                        continue
                    if h + i >= input_height or w + j >= input_width:
                        continue
                    output_matrix[k][t] += input_matrix[h + i][w + j] * kernel[i][j]
            t += 1
        k += 1

    return output_matrix
