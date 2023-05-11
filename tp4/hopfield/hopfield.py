import numpy as np


class Hopfield:

    def __init__(self, pattern_set, iteration_limit):
        self.iteration_limit = iteration_limit
        dim = len(pattern_set[0])
        pattern_set_size = 1 / len(pattern_set)
        self.weight = np.zeros((dim, dim))
        for pattern in pattern_set:
            self.weight += np.outer(pattern, pattern) / pattern_set_size
        self.weight -= np.eye(dim, dim)

    def get_pattern(self, pattern):
        before = pattern
        has_changed = True
        iteration = 0
        while has_changed and iteration < self.iteration_limit:
            current = np.sign(np.dot(self.weight, before))
            error = np.linalg.norm(current - before)
            print(str(iteration) + " : " + str(error))
            has_changed = True if error != 0 else False
            iteration += 1
            before = current
        return before

    def calculate_energy(self, pattern):
        return -1 / 2 * pattern.T * self.weight * pattern
