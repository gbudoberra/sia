import numpy as np


# based
# on https://openlearninglibrary.mit.edu/assets/courseware/v1/9c36c444e5df10eef7ce4d052e4a2ed1/asset-v1:MITx+6.036+1T2019+type@asset+block/notes_chapter_Neural_Networks.pdf
class Multilayer:

    activation_methods = {
        "relu": [lambda x: np.maximum(0, x), lambda x: 1 if x > 0 else 0],
        "sigmoid": [lambda x: 1 / (1 + np.exp(-x)), lambda x: (1 / (1 + np.exp(-x))) * (1 - (1 / (1 + np.exp(-x))))],
        "id": [lambda x: x, lambda x: 1],
        "tanh": [lambda x: np.tanh(x), lambda x: 1 - np.square(np.tanh(x))],
        "step": [lambda x: 1 if x >= 0 else -1, lambda x: 1],
    }

    def __init__(self, perceptron_by_layer, data_set, activation_method, result_set, epsilon, learning_rate):

        self.point_number = len(data_set)
        self.layer_number = len(perceptron_by_layer)

        self.results_matrix = np.transpose(np.array([point for point in result_set]))
        self.input_matrix = np.transpose(np.array([np.insert(point, 0, -1) for point in data_set]))
        self.activation_method = np.vectorize(self.activation_methods[activation_method][0])
        self.activation_derivative = np.vectorize(self.activation_methods[activation_method][1])
        self.epsilon = epsilon
        self.learning_rate = learning_rate

        self.output_by_layer = []
        self.differentiated_preactivate_by_layer = []
        self.weights_by_layer = []
        self.pre_activation_by_layer = []

        for index in range(self.layer_number - 1):
            self.weights_by_layer.append(np.zeros(
                (perceptron_by_layer[index + 1], perceptron_by_layer[index])))
            zero_matrix = np.zeros((perceptron_by_layer[index + 1], self.point_number))
            self.output_by_layer.append(zero_matrix.copy())
            self.differentiated_preactivate_by_layer.append(zero_matrix.copy())
            self.pre_activation_by_layer.append(zero_matrix.copy())

    def error(self):
        error = (self.output_by_layer[-1] - self.results_matrix) ** 2
        cumulative_error = np.sum(error)
        return (1 / 2) * cumulative_error

    def has_converged(self):
        return self.error() < self.epsilon

    def batch_iteration(self):
        while not self.has_converged():
            last_output = self.input_matrix
            for index in range(self.layer_number - 1):
                self.pre_activation_by_layer[index] = np.matmul(self.weights_by_layer[index], last_output)
                self.output_by_layer[index] = self.activation_method(self.pre_activation_by_layer[index])
                self.differentiated_preactivate_by_layer[index] = self.activation_derivative(self.pre_activation_by_layer[index])
                last_output = self.output_by_layer[index]
            self.update_weights()

    def update_weights(self):
        for current_point in range(self.point_number):
            multipliers = self._compute_multipliers(current_point)
            base = np.array(self.input_matrix[:, current_point])
            for layer in range(len(self.weights_by_layer)):
                if layer > 0:
                    base = self.output_by_layer[layer - 1][:, current_point]
                self.weights_by_layer[layer] += -1 * self.learning_rate * np.transpose(np.outer(base, multipliers[layer]))

    def _compute_multipliers(self, index):
        multipliers = []
        current_layer = len(self.weights_by_layer) - 1
        base = np.matmul(np.diag(self.differentiated_preactivate_by_layer[current_layer][:, index]), (self.output_by_layer[-1][:, index]) - self.results_matrix[:, index])
        multipliers.append(base)
        current_layer -= 1
        while current_layer >= 0:
            base = np.matmul(np.matmul(np.diag(self.differentiated_preactivate_by_layer[current_layer][:, index]), self.weights_by_layer[current_layer + 1]), base)
            multipliers.append(base)
            current_layer -= 1
        return multipliers[::-1]
