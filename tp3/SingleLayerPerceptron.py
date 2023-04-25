import numpy as np


class SingleLayerPerceptron:
    def __init__(self, point_set, learning_rate, expected_results, epsilon, activation_function):
        if not point_set:
            raise ValueError("Invalid point provided")
        self.weights = np.zeros(len(point_set[0]) + 1)
        self.point_matrix = np.array([np.insert(point, 0, 1) for point in point_set])
        self.learning_rate = learning_rate
        self.expected_results = np.array(expected_results)
        self.current_weights_output = np.zeros(len(expected_results))
        self.current_iterations = 0
        self.epsilon = epsilon
        self.activation_function = activation_function

    def has_converged(self):
        output_results = [ self.activation_function(output) for output in self.current_weights_output]
        return self.current_iterations > 1000 or \
            np.linalg.norm(output_results - self.expected_results) <= 0

    def update_weight(self, point, output_value, expected_value):
        self.weights = self.weights + \
                       (self.learning_rate * (expected_value - output_value) * point)

    def get_solution(self):
        while not self.has_converged():
            self.current_weights_output = np.dot(self.point_matrix, self.weights)
            for i in range(len(self.expected_results)):
                vector_output = self.activation_function(self.current_weights_output[i])
                if self.expected_results[i] != vector_output:
                    self.update_weight(self.point_matrix[i], vector_output, self.expected_results[i])
            self.current_iterations += 1
