import numpy as np


# this class is not used as a multilayer with one layer is equivalent.
class Oja:

    def __init__(self, point_set, learning_rate, epochs, target):
        if not point_set:
            raise ValueError("Invalid point provided")
        self.weights = np.random.uniform(0, 1, len(point_set[0]))
        self.point_matrix = np.array([point for point in point_set])
        self.learning_rate = learning_rate
        self.current_weights_output = np.zeros(len(self.point_matrix))
        self.current_iterations = 0
        self.prev_weights = None
        self.epochs = epochs
        self.error = []
        self.target = target

    def update_weight(self, point, output_value):
        self.prev_weights = np.copy(self.weights)
        self.weights = self.weights + self.learning_rate * output_value * (point - output_value * self.weights)

    def iterate(self):
        for i in range(self.epochs):
            self.error.append(np.sqrt(np.linalg.norm(self.weights - self.target)))
            for point in self.point_matrix:
                point_array = np.array(point)
                output = np.inner(point_array, self.weights)
                self.update_weight(point_array, output)

    def get_y1(self):
        result = []
        for point in self.point_matrix:
            result.append(np.inner(point, self.weights))
        return result
