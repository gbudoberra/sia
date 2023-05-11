import numpy as np


class Neuron:
    def __init__(self, dim):
        self.weights = np.random.normal(0, 0.5, size=dim)

    @classmethod
    def init_with_initial_value(cls, point):
        neuron = cls(len(point))
        neuron.weights = point
        return neuron

    def evaluate_point(self, point):
        return np.linalg.norm(self.weights - point)

    def update_weights(self, delta):
        delta_vector = np.ones(len(self.weights)) * delta
        self.weights += delta_vector

