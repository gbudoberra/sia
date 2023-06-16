import numpy as np

from tp3.multilayer.utils import initialize_weights, initialize_outputs


def gradient_descendent(gradient, learning_rate):
    return -1 * learning_rate * gradient


# def adam_update(self, gradient):
#         b1 = 0.9
#         b2 = 0.95  # 0.999
#         e = 1e-8
#         self.adam_iteration += 1
#         for layer in range(len(self.weights_by_layer)):
#             self.mean[layer] = (b1 * self.mean[layer] + (1 - b1) * gradient[layer]) / (1 - (b1 ** self.adam_iteration))
#             self.std[layer] = (b2 * self.std[layer] + (1 - b2) * np.square(gradient[layer])) / (
#                     1 - (b2 ** self.adam_iteration))
#             self.weights_by_layer[layer] += -1 * self.learning_rate * (
#                 np.divide(self.mean[layer], (np.sqrt(self.std[layer] + e)))
#             )


class Perceptron:

    def __init__(self, architecture, data_dim, activation_methods, activation_derivatives, learning_rate,
                 update_method=gradient_descendent):
        self.update = update_method
        self.learning_rate = learning_rate
        self.architecture = architecture
        self.activation_method = activation_methods
        self.activation_derivative = activation_derivatives
        self.weights = initialize_weights(architecture)
        self.outputs = initialize_outputs(architecture, data_dim)
        self.input = None
        self.derivatives = initialize_outputs(architecture, data_dim)

    def feed(self, x):
        self.input = x
        for i, weights in enumerate(self.weights):
            preactivation = np.matmul(weights, x)
            self.derivatives[i] = self.activation_derivative(preactivation)
            x = self.outputs[i] = self.activation_method(preactivation)
        return x

    def back_propagation(self, dloss, current_point, expected):
        multipliers = []
        current_layer = len(self.weights) - 1
        base = np.matmul(np.diag(self.derivatives[current_layer][:, current_point]), dloss)
        multipliers.append(base)
        current_layer -= 1
        while current_layer >= 0:
            diagonal = np.diag(self.derivatives[current_layer][:, current_point])
            weights_transposed = self.weights[current_layer + 1].T
            base = np.matmul(np.matmul(diagonal, weights_transposed), base)
            multipliers.append(base)
            current_layer -= 1
        multipliers = multipliers[::-1]

        for layer in reversed(range(len(self.weights))):
            if layer == 0:
                base = np.array(expected)
            else:
                base = self.outputs[layer - 1][:, current_point]
            last_gradient = np.transpose(np.outer(base, multipliers[layer]))
            self.weights[layer] += self.update(last_gradient, self.learning_rate)

        weights_transposed = self.weights[0].T
        return np.matmul(weights_transposed, multipliers[0])

# def back_propagation(self, dloss, current_point):
#     for i, weights in enumerate(reversed(self.weights)):
#         real_i = (len(self.weights) - 1) - i
#
#         if real_i > 0:
#             dloss_dw = np.matmul(np.matmul(dloss, self.derivatives[real_i]),
#                                  self.outputs[real_i - 1].T)  # dloss/dx' * dx'/dwn = dloss/dx' * h'(preac) * I
#             # (35,32) * (35,32) * (32,10) => 35 10
#             self.outputs[real_i - 1][:, current_point]
#
#
#         else:
#             dloss_dw = np.matmul(np.matmul(dloss, self.derivatives[real_i]), self.input.T)
#         self.weights[real_i] += self.update(dloss_dw, self.learning_rate)
#
#         dloss_di = np.matmul(np.matmul(np.diag(dloss), self.weights[real_i]).T, self.derivatives[real_i])  # dloss/dx' * dx'/dI = dloss/dx' * h'(preac) * Wn => dloss/dO
#         dloss = dloss_di
#     return dloss


# I + W1 -> O2 -> O2 + W2 -> X'
# d(||X-X'||)/dX'
# O3 = h( W2 * O2 )
# dloss/dW2 = dloss/dO3 * dO3/dW2 = dloss/dO3 * h'( W2 * O2 ) * O2 = gradiente de W2
# dloss/dO2 = dloss/dO3 * dO3/dO2 = dloss/dO3 * h'( W2 * O2 ) * W2
# dloss/dO2
# dloss/dW1 = dloss/dO2 * dO2/dW1 = dloss/dO2 * h'( W1 * O1 ) * O1 = gradiente de W1
# ...

# dloss/dO2 =  dloss/dx' * dx'/dO2 = dloss/dx' * h'(preac) * W1
#

# I + W1 -> O2 -> O2 + W2 -> m
# d(MSE + KL)/dm
# m = h( W2 * O2 )
# dloss/dW2 = dloss/dm * dO3/dW2 = dloss/dm * h'( W2 * O2 ) * O2 = gradiente de W2
# dloss/dO2 = dloss/dm * dO3/dO2 = dloss/dm * h'( W2 * O2 ) * W2
# dloss/dO2
# dloss/dW1 = dloss/dO2 * dO2/dW1 = dloss/dO2 * h'( W1 * O1 ) * O1 = gradiente de W1
