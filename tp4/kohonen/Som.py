import random

from neuron import Neuron
import numpy as np


class Som:
    def __init__(self, map_dim, point_set, learning_rate, iteration_limit):
        self.k = map_dim
        self._initialize_neuron_matrix(map_dim, len(point_set[0]))

        self.iterations = 0
        self.radius = 1
        self.learning_rate = 1

        self.point_set = point_set
        self.iteration_limit = iteration_limit

    def _initialize_neuron_matrix(self, map_dim, point_dim):
        self.neurons = []
        for i in range(map_dim):
            neuron_row = []
            for j in range(map_dim):
                neuron_row.append(Neuron(point_dim))
            self.neurons.append(neuron_row)

    def _train_iteration(self):
        training_point = self.point_set[random.randint(0, len(self.point_set) - 1)]
        return self._get_minimum_distance(training_point)

    def _get_minimum_distance(self, training_point):
        distance_matrix = np.zeros((self.k, self.k))
        for i in range(self.k):
            for j in range(self.k):
                distance_matrix[i][j] = self.neurons[i][j].evaluate_point(training_point)
        minimum_distance = np.unravel_index(np.argmin(distance_matrix), distance_matrix.shape)
        minimum_row = minimum_distance[0]
        minimum_col = minimum_distance[1]
        return {'minimum_distance': distance_matrix[minimum_row][minimum_col], 'minimum_row': minimum_row,
                'minimum_col': minimum_col}

    def _update_neurons(self, minimum_distance, minimum_row, minimum_col):
        offset = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for row_offset, col_offset in offset:
            if self.k > minimum_row + row_offset >= 0 and self.k > minimum_col + col_offset >= 0:
                self.neurons[minimum_row + row_offset][minimum_col + col_offset]\
                    .update_weights((self.learning_rate / (self.iterations + 1)) * minimum_distance)

    def train(self):
        while self.iterations < self.iteration_limit:
            train_iteration = self._train_iteration()
            self._update_neurons(train_iteration['minimum_distance'], train_iteration['minimum_row'],
                                 train_iteration['minimum_col'])
            self.iterations += 1

    def get_row_and_column(self, point):
        minimum = self._get_minimum_distance(point)
        return minimum['minimum_row'], minimum['minimum_col']

