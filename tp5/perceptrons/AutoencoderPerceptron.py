import numpy as np

from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron
from tp5.perceptrons.result_functions import get_latent_result, generate_from_latent_space, get_result


class AutoencoderPerceptron(MultiLayerPerceptron):

    def __init__(self, perceptron_by_layer, data_set, activation_methods, result_set, epsilon, learning_rate,
                 update_method="gradient_descent", iteration_limit=10000):
        super().__init__(perceptron_by_layer, data_set, activation_methods, result_set, epsilon, learning_rate,
                         update_method)
        self.iteration_limit = iteration_limit
        for i in range(len(perceptron_by_layer)):
            if perceptron_by_layer[i] == 2:
                self.latent_layer = i

    def error(self):
        matrix = self.output_by_layer[-1]
        binary_matrix = np.zeros(matrix.shape, dtype=int)
        binary_matrix[matrix >= 0.5] = 1
        return np.sum(np.square(binary_matrix - self.results_matrix))

    def get_result(self, points):
        return get_result(points, self.activation_method_by_layer, self.weights_by_layer)

    def has_converged(self):
        error = self.error()
        if self.epochs % 10 == 0:
            print(f'{self.epochs} {error}')
        return self.epochs > self.iteration_limit or error < self.epsilon

    def get_latent_result(self, points):
        return get_latent_result(points, self.activation_method_by_layer, self.weights_by_layer, self.latent_layer)

    # receives a point, and multiply back from the latent space to the initial space
    def generate_from_latent_space(self, points):
        return generate_from_latent_space(points, self.activation_method_by_layer, self.weights_by_layer,
                                          self.latent_layer)
