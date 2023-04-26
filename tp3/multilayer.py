import numpy as np


# based
# on https://openlearninglibrary.mit.edu/assets/courseware/v1/9c36c444e5df10eef7ce4d052e4a2ed1/asset-v1:MITx+6.036+1T2019+type@asset+block/notes_chapter_Neural_Networks.pdf
class Multilayer:

    activation_methods = {
        "relu": [lambda x: np.maximum(0, x), lambda x: 1 if x > 0 else 0],
        "sigmoid": [lambda x: 1 / (1 + np.exp(-x)), lambda x: (1 / (1 + np.exp(-x))) * (1 - (1 / (1 + np.exp(-x))))],
        "id": [lambda x: x, lambda x: 1],
        "tanh": [lambda x: np.tanh(x), lambda x: 1 - np.square(np.tanh(x))],
        "step": [lambda x: np.sign(x), lambda x: 0],
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
        self.derivative_action_by_layer = []
        self.weights_by_layer = []
        self.pre_activation_by_layer = []

        for index in range(self.layer_number - 1):
            self.weights_by_layer.append(np.zeros(
                (perceptron_by_layer[index + 1], perceptron_by_layer[index])))
            zero_matrix = np.zeros((perceptron_by_layer[index], self.point_number))
            self.output_by_layer.append(zero_matrix.copy())
            self.derivative_action_by_layer.append(zero_matrix.copy())
            self.pre_activation_by_layer.append(zero_matrix.copy())

    def error(self):
        error = (self.output_by_layer[self.layer_number - 1] - self.results_matrix) ** 2
        cumulative_error = np.sum(error)
        return (1 / 2) * cumulative_error

    def has_converged(self):
        return self.error() < self.epsilon

    def batch_iteration(self):
        while not self.has_converged():
            base = self.input_matrix
            for index in range(self.layer_number - 1):
                self.pre_activation_by_layer[index] = np.dot(self.weights_by_layer[index], base)
                self.output_by_layer[index] = self.activation_method(self.pre_activation_by_layer[index])
                self.derivative_action_by_layer[index] = self.activation_derivative(self.pre_activation_by_layer[index])
                base = self.output_by_layer[index]
            self.update_weights()

    def update_weights(self):
        for current_point in range(self.point_number):
            current_layer = self.layer_number - 1
            multiplier = self.learning_rate * (self.results_matrix.T[current_point] - self.output_by_layer[current_layer - 1].T[current_point])
            layer_weight_delta = multiplier * self.output_by_layer[current_layer - 1].T[current_point]
            layer_weight_delta *= self.derivative_action_by_layer[current_layer - 1].T[current_point]
            self.weights_by_layer[current_layer - 1] += layer_weight_delta
            while current_layer > 1:
                layer_weight_delta = layer_weight_delta * self.weights_by_layer[current_layer - 1] * self.derivative_action_by_layer[current_layer - 1].T[current_point]
                current_layer -= 1
                self.weights_by_layer[current_layer] = layer_weight_delta
        print("finished")

