import numpy as np


# based
# on https://openlearninglibrary.mit.edu/assets/courseware/v1/9c36c444e5df10eef7ce4d052e4a2ed1/asset-v1:MITx+6.036+1T2019+type@asset+block/notes_chapter_Neural_Networks.pdf
class Multilayer:

    activation_methods = {
        "step": [lambda x: np.sign(x)],
        "id": [lambda x: x]
    }

    def __init__(self, perceptron_by_layer, point_set, activation_method, expected_set, epsilon):
        self.layer_number = len(perceptron_by_layer)
        self.expected_matrix = np.array([point for point in expected_set])
        input_matrix = np.array([np.insert(point, 0, -1) for point in point_set])
        input_matrix = np.transpose(input_matrix)
        self.output_by_layer = [input_matrix]
        self.weights_by_layer = []
        self.pre_activation_by_layer = []
        for index in range(self.layer_number - 1):
            self.weights_by_layer.append(
                (np.zeros(perceptron_by_layer[index + 1], perceptron_by_layer[index])))
            self.output_by_layer.append(np.zeros((
                perceptron_by_layer[index + 1], len(point_set))))
            self.pre_activation_by_layer.append(np.zeros(
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
        for index in range(len(self.weights_by_layer)):
            self.pre_activation_by_layer[index] = np.dot(self.weights_by_layer[index], self.output_by_layer[index - 1])
            self.output_by_layer[index] = self.activation_method(self.pre_activation_by_layer[index])


