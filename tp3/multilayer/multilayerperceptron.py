import numpy as np
from tp3.multilayer.utils import initialize_network, update_layer, compute_multipliers
import pandas as pd

# based
# on https://openlearninglibrary.mit.edu/assets/courseware/v1/9c36c444e5df10eef7ce4d052e4a2ed1/asset-v1:MITx+6.036+1T2019+type@asset+block/notes_chapter_Neural_Networks.pdf
class MultiLayerPerceptron:
    activation_methods = {
        "relu": [lambda x: np.maximum(0, x), lambda x: 1 if x > 0 else 0],
        "sigmoid": [lambda x: 1 / (1 + np.exp(-x)), lambda x: (1 / (1 + np.exp(-x))) * (1 - (1 / (1 + np.exp(-x))))],
        "id": [lambda x: x, lambda x: 1],
        "tanh": [lambda x: np.tanh(x), lambda x: 1 - np.square(np.tanh(x))],
        "step": [lambda x: 1 if x >= 0 else -1, lambda x: 1],
    }

    # 4 Matrices por layer:
    #       1- OUTPUTS = [ O1, O2, ... ]
    #       2- WEIGHTS = [ W0, W1, ... ]
    #       3- Pre-activation = [ sum( Wi * Xi) para to i ]
    #       4- Pre-activation diff = [ deltas ]
    def __init__(self, perceptron_by_layer, data_set, activation_method, result_set, epsilon, learning_rate):

        self.epsilon = epsilon
        self.learning_rate = learning_rate
        self.epochs = 0

        self.point_number = len(data_set)
        self.layer_number = len(perceptron_by_layer)

        self.results_matrix = np.transpose(np.array([point for point in result_set]))
        self.input_matrix = np.transpose(np.array([np.insert(point, 0, -1) for point in data_set]))

        self.activation_method = np.vectorize(self.activation_methods[activation_method][0])
        self.activation_derivative = np.vectorize(self.activation_methods[activation_method][1])

        # Inicializa cada uno de estos vectores con matrices en 0 con sus respectivas dimensiones.
        self.weights_by_layer, self.output_by_layer, \
            self.differentiated_preactivate_by_layer, self.pre_activation_by_layer \
            = initialize_network(perceptron_by_layer, self.point_number)

    def error(self):
        error = (self.output_by_layer[-1] - self.results_matrix) ** 2
        cumulative_error = np.sum(error)
        return (1 / 2) * cumulative_error

    def has_converged(self):
        return self.epochs > 5000 or self.error() < self.epsilon

    def batch_iteration(self):
        while not self.has_converged():
            self.update_network(self.input_matrix)
            self.back_propagation()
            print(self.output_by_layer[-1])
            self.epochs += 1

    def update_network(self, input_data):
        last_output = input_data
        for index in range(self.layer_number - 1):
            self.pre_activation_by_layer[index], self.output_by_layer[index], \
                self.differentiated_preactivate_by_layer[index] = update_layer(last_output,
                                                                               self.weights_by_layer[index],
                                                                               self.activation_method,
                                                                               self.activation_derivative)
            last_output = self.output_by_layer[index]

    def back_propagation(self):
        for current_point in range(self.point_number):

            multipliers = self._compute_multipliers(current_point)
            base = np.array(self.input_matrix[:, current_point])

            for layer in range(len(self.weights_by_layer)):
                if layer > 0:
                    base = self.output_by_layer[layer - 1][:, current_point]
                self.weights_by_layer[layer] += -1 * self.learning_rate * np.transpose(
                    np.outer(base, multipliers[layer]))

    def _compute_multipliers(self, index):
        outputs_vs_expected_delta = ((self.output_by_layer[-1][:, index]) - self.results_matrix[:, index])
        return compute_multipliers(
            index,
            self.weights_by_layer,
            self.differentiated_preactivate_by_layer,
            outputs_vs_expected_delta
        )

    def get_result(self, points):
        partial_output = np.insert(points, 0, -1)
        for i in range(len(self.weights_by_layer)):
            partial_output = np.dot(self.weights_by_layer[i], partial_output)
        return self.activation_method(partial_output)



