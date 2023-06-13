import numpy as np

from tp3.multilayer.multilayerperceptron import activation_methods_dictionary


class PreTrainedPerceptron:
    def __init__(self, weights, activation_method_by_layer, latent_layer):
        self.weights = weights
        self.activation_method_by_layer = []
        for am in activation_method_by_layer:
            self.activation_method_by_layer.append(activation_methods_dictionary[am][0])
        self.latent_layer = latent_layer

    def get_weights(self):
        return self.weights

    def get_result(self, points):
        partial_output = points
        for method, weight in zip(self.activation_method_by_layer, self.weights):
            partial_output = method(np.dot(weight, partial_output))
        binary_array = np.zeros_like(partial_output, dtype=int)
        binary_array[partial_output >= 0.5] = 1
        return binary_array

    def get_latent_result(self, points):
        partial_output = points
        for method, weight in \
                zip(self.activation_method_by_layer[:self.latent_layer - 1], self.weights[:self.latent_layer - 1]):
            partial_output = method(np.dot(weight, partial_output))
        return partial_output

    # receives a point, and multiply back from the latent space to the initial space
    def generate_from_latent_space(self, point):
        partial_output = point
        for method, weight in \
                zip(self.activation_method_by_layer[self.latent_layer - 1:], self.weights[self.latent_layer - 1:]):
            partial_output = method(np.dot(weight, partial_output))
        binary_array = np.zeros_like(partial_output, dtype=int)
        binary_array[partial_output >= 0.5] = 1
        return binary_array
