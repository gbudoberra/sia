import numpy as np
from tp4.hopfield.utils import plot_array


class Hopfield:

    def __init__(self, pattern_set, iteration_limit):
        self.iteration_limit = iteration_limit
        neuron_number = len(pattern_set[0])
        self.weight = ((1 / neuron_number) * np.dot(np.transpose(pattern_set), pattern_set))
        for i in range(neuron_number):
            self.weight[i][i] = 0

    def get_pattern(self, pattern, filename, png_size):
        before = pattern
        has_changed = True
        iteration = 0
        while has_changed and iteration < self.iteration_limit:

            iter_filename = f'{filename}_i{iteration}.png'
            before_for_graph = [b for b in before]
            plot_array(before_for_graph, iter_filename, png_size)

            current = np.sign(np.dot(self.weight, before))
            has_changed = self._error_by_position(current, before)
            iteration += 1
            before = current
        return before

    def _error_by_position(self, current, before):
        for c, b in zip(current, before):
            if c != b:
                return True
        return False

    def calculate_energy(self, pattern):
        return -1 / 2 * pattern.T * self.weight * pattern
