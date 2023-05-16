import numpy as np
from utils import get_distance


class Neuron:
    def __init__(self, dim):
        self.weights = np.random.normal(0, 0.5, size=dim)

    @classmethod
    def init_with_initial_value(cls, point):
        neuron = cls(len(point))
        neuron.weights = point
        return neuron

    def evaluate_point(self, point):
        return get_distance(self.weights, point)

    def update_weights(self, learning_rate, training_point):
        delta_vector = (np.ones(len(self.weights)) * learning_rate) * (training_point - self.weights)
        self.weights += delta_vector

