import numpy as np

from tp3.multilayer.utils import create_mean_and_std_matrix
from tp5.update_methods.UpdateMethod import UpdateMethod

b1 = 0.9
b2 = 0.95  # 0.999
e = 1e-8


def _update_mean(gradient, mean, iteration):
    return (b1 * mean + (1 - b1) * gradient) / (1 - (b1 ** iteration))


def _update_std(gradient, std, iteration):
    return (b2 * std + (1 - b2) * np.square(gradient)) / (1 - (b2 ** iteration))


class Adam(UpdateMethod):

    def __init__(self, learning_rate, architecture):
        self.learning_rate = learning_rate
        self.adam_iterations = np.zeros(len(architecture))
        self.mean, self.std = create_mean_and_std_matrix(architecture)

    def get_delta(self, gradient, layer):
        self.adam_iterations[layer] += 1
        self.mean[layer] = _update_mean(gradient, self.mean[layer], self.adam_iterations[layer])
        self.std[layer] = _update_std(gradient, self.std[layer], self.adam_iterations[layer])
        return -1 * self.learning_rate * (np.divide(self.mean[layer], (np.sqrt(self.std[layer] + e))))
