import numpy as np


class Multilayer:

    activation_methods = {
        "step": [lambda x: np.sign(x)],
        "id": [lambda x: x]
    }

    # perceptron_by_layer provides the number of Perceptron in each layer from bottom
    def __init__(self, perceptron_by_layer, point_set, activation_method, expected_set, epsilon):
        self.layer_number = len(perceptron_by_layer)
        self.expected_matrix = np.array([point for point in expected_set])
        point_matrix = np.array([np.insert(point, 0, -1) for point in point_set])
        point_matrix = np.transpose(point_matrix)
        self.output_by_layer = [point_matrix]
        self.layer_weight_matrix_array = []
        self.without_activation_by_layer = []
        for index in range(len(perceptron_by_layer) - 1):
            self.layer_weight_matrix_array.append(
                (np.zeros(perceptron_by_layer[index + 1], perceptron_by_layer[index])))
            self.output_by_layer.append(np.zeros((
                perceptron_by_layer[index + 1], len(point_set))))
            self.without_activation_by_layer.append(np.zeros(
                (perceptron_by_layer[index + 1], len(point_set))))
        self.activation_method = np.vectorize(self.activation_methods[activation_method])
        self.epsilon = epsilon

    def error(self):
        transposed_result = np.transpose(self.output_by_layer[self.layer_number])
        cumulative_error = 0
        for index in range(len(transposed_result)):
            cumulative_error += pow(transposed_result[index] - self.expected_matrix[index], 2)
        return (1/2)*cumulative_error

    def has_converged(self):
        return self.error() < self.epsilon

    def batch_iteration(self):
        for index in range(len(self.layer_weight_matrix_array)):
            result = np.dot(self.layer_weight_matrix_array[index], self.output_by_layer[index - 1])
            self.without_activation_by_layer[index] = result
            self.output_by_layer[index] = self.activation_method(result)


