import random

import numpy as np


def create_mean_and_std_matrix(perceptron_by_layer):
    mean = []
    for index in range(len(perceptron_by_layer) - 1):
        mean.append(np.zeros(
            (perceptron_by_layer[index + 1], perceptron_by_layer[index])))
    return mean, mean.copy()


# create an initial random weight  matrix
def create_weights_by_layer(perceptron_by_layer):
    weights_by_layer = []

    for index in range(len(perceptron_by_layer) - 1):
        random.seed(100541)
        np.random.seed(100541)
        weights = np.random.normal(0, 0.5, size=(perceptron_by_layer[index + 1], perceptron_by_layer[index]))
        weights_by_layer.append(weights)
    return weights_by_layer


def create_zero_matrices(perceptron_by_layer, point_number):
    matrix = []
    for index in range(len(perceptron_by_layer) - 1):
        zero_matrix = np.zeros((perceptron_by_layer[index + 1], point_number))
        matrix.append(zero_matrix.copy())
    return matrix


def initialize_network(perceptron_by_layer, point_number):
    weights_by_layer = create_weights_by_layer(perceptron_by_layer)
    mean, std = create_mean_and_std_matrix(perceptron_by_layer)

    zero_matrix = create_zero_matrices(perceptron_by_layer, point_number)
    output_by_layer = zero_matrix.copy()
    differentiated_preactivate_by_layer = zero_matrix.copy()
    pre_activation_by_layer = zero_matrix.copy()

    return weights_by_layer, output_by_layer, differentiated_preactivate_by_layer, pre_activation_by_layer, mean, std


def update_layer(last_output, weights, activation_method, activation_derivative):
    pre_activation_by_layer = np.matmul(weights, last_output)
    output_by_layer = activation_method(pre_activation_by_layer)
    differentiated_preactivate_by_layer = activation_derivative(pre_activation_by_layer)
    return pre_activation_by_layer, output_by_layer, differentiated_preactivate_by_layer


def compute_multipliers(index, weights_by_layer, differentiated_preactivate_by_layer, outputs_delta_to_expected):
    multipliers = []
    current_layer = len(weights_by_layer) - 1
    base = np.matmul(np.diag(differentiated_preactivate_by_layer[current_layer][:, index]),
                     outputs_delta_to_expected)
    multipliers.append(base)
    current_layer -= 1
    while current_layer >= 0:
        diagonal = np.diag(differentiated_preactivate_by_layer[current_layer][:, index])
        weights_transposed = weights_by_layer[current_layer + 1].T
        base = np.matmul(np.matmul(diagonal, weights_transposed), base)
        multipliers.append(base)
        current_layer -= 1
    return multipliers[::-1]
