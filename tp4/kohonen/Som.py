import random

from neuron import Neuron
import numpy as np
from utils import get_distance


class Som:
    def __init__(self, map_dim, point_set, iteration_limit, update_radius, update_learning_rate):
        self.k = map_dim
        self.iterations = 0

        self.point_set = point_set
        self.iteration_limit = iteration_limit * (self.k ** 2)

        self._initialize_neuron_matrix(map_dim)

        self._varying_learning_rate = update_learning_rate
        self._varying_radius = update_radius
        self.radius = map_dim if self._varying_radius else 1
        self.learning_rate = 1 if self._varying_learning_rate else 0.1

    def _initialize_neuron_matrix(self, map_dim):
        self.neurons = []
        for i in range(map_dim):
            neuron_row = []
            for j in range(map_dim):
                neuron_row.append(
                    Neuron.init_with_initial_value(self.point_set[random.randint(0, len(self.point_set) - 1)]))
            self.neurons.append(neuron_row)

    def _train_iteration(self, training_point):
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

    def _update_neurons(self, minimum_distance, minimum_row, minimum_col, training_point):
        adjacent_cells = self._get_adjacent_cells(minimum_row, minimum_col)
        for adj_row, adj_col in adjacent_cells:
            if self.k > adj_row >= 0 and self.k > adj_col >= 0:
                self.neurons[adj_row][adj_col].update_weights(self.learning_rate, training_point)

    def train(self):
        while self.iterations < self.iteration_limit:
            training_point = self.point_set[random.randint(0, len(self.point_set) - 1)]
            train_iteration = self._train_iteration(training_point)
            self._update_neurons(train_iteration['minimum_distance'], train_iteration['minimum_row'],
                                 train_iteration['minimum_col'], training_point)
            self._update_radius()
            self._update_learning_rate()
            print(self.iterations)
            self.iterations += 1

    def get_row_and_column(self, point):
        minimum = self._get_minimum_distance(point)
        return minimum['minimum_row'], minimum['minimum_col']

    def _update_radius(self):
        if self._varying_radius and self.radius > 1:
            self.radius -= 1

    def _update_learning_rate(self):
        # ensuring learning_rate < 1 as iterations starts in 0.
        if self._varying_learning_rate:
            self.learning_rate = (self.learning_rate / (self.iterations + 2))

    def _get_adjacent_cells(self, row, col):
        radius = self.radius
        adjacent_cells = []
        for current_row in range(row - radius, row + radius + 1):
            for current_col in range(col - radius, col + radius + 1):
                distance = np.sqrt((current_row - row) ** 2 + (current_col - col) ** 2)
                if 0 < distance <= radius:
                    adjacent_cells.append((current_row, current_col))
        return adjacent_cells

    def compute_avg_distance(self, row, col):
        adjacent_cells = self._get_adjacent_cells(row, col)
        adjacent_diff = []
        for adj_row, adj_col in adjacent_cells:
            if self.k > adj_row >= 0 and self.k > adj_col >= 0:
                adjacent_diff.append(
                    get_distance(self.neurons[adj_row][adj_col].weights, self.neurons[row][col].weights))
        return np.mean(adjacent_diff)

    def get_avg_distance(self):
        result_matrix = []
        for row in range(self.k):
            result_row = []
            for col in range(self.k):
                result_row.append(self.compute_avg_distance(row, col))
            result_matrix.append(result_row)
        return result_matrix
