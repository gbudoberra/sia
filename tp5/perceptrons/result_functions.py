import numpy as np


def get_result(points, activation_method_by_layer, weights):
    partial_output = points
    for activation_method, weight in zip(activation_method_by_layer, weights):
        partial_output = activation_method(np.dot(weight, partial_output))
    binary_array = np.zeros_like(partial_output, dtype=int)
    binary_array[partial_output >= 0.5] = 1
    return binary_array


def get_latent_result(points, activation_method_by_layer, weights, latent_layer):
    partial_output = points
    for activation_method, weight in zip(activation_method_by_layer[:latent_layer - 1], weights[:latent_layer - 1]):
        partial_output = activation_method(np.dot(weight, partial_output))
    return partial_output


# receives a point, and multiply back from the latent space to the initial space
def generate_from_latent_space(points, activation_method_by_layer, weights, latent_layer):
    partial_output = points
    for activation_method, weight in zip(activation_method_by_layer[latent_layer - 1:], weights[latent_layer - 1:]):
        partial_output = activation_method(np.dot(weight, partial_output))
    binary_array = np.zeros_like(partial_output, dtype=int)
    binary_array[partial_output >= 0.5] = 1
    return binary_array
