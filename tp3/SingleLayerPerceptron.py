import numpy as np


class SingleLayerPerceptron:
    def __init__(self, point_set, learning_rate, expected_results):
        if len(point_set) == 0:
            RuntimeError("Invalid point set provided")
        self.weights = [0 for _ in range(len(point_set[0])+1)]
        self.vector_set = []
        for point in point_set:
            coordinates = [1]
            for x_i in point:
                coordinates.append(x_i)
            self.vector_set.append(np.array(coordinates))
        self.learning_rate = learning_rate
        self.expected_results = expected_results
        self.old_weights = []
        self.current_iterations = 0

    def compute_vector_output(self, index):
        point = np.array([self.vector_set[index][i] for i in range(1, len(self.vector_set[index]))])
        weights = np.array([self.weights[i] for i in range(1, len(self.weights))])
        if (np.dot(point, weights) - self.weights[0]) >= 0:
            return 1
        else:
            return -1

    def has_converged(self):
        if self.current_iterations > 10000:
            return True
        wrong = 0
        for i in range(len(self.vector_set)):
            if self.compute_vector_output(i) != self.expected_results[i]:
                wrong += 1
        return wrong == 0

    def iteration(self):
        for current_vector in range(len(self.vector_set)):
            vector_output = self.compute_vector_output(current_vector)
            vector_expected = self.expected_results[current_vector]
            if vector_expected != vector_output:
                self.update_weight(current_vector, vector_output, vector_expected)

    def update_weight(self, i, output, expected):
        self.old_weights.append(self.weights)
        new_weights = self.weights + (self.learning_rate * (expected - output) * self.vector_set[i])
        self.weights = new_weights

    def get_solution(self):
        while not self.has_converged():
            self.iteration()
            self.current_iterations += 1
