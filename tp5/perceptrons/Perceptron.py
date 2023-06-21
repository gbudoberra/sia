import numpy as np

from tp3.multilayer.utils import initialize_weights, initialize_outputs
from tp5.update_methods.UpdateMethod import UpdateMethod


class Perceptron:

    def __init__(self, architecture, data_dim, activation_methods, activation_derivatives, update_method: UpdateMethod):
        self.update = update_method
        self.architecture = architecture
        self.activation_method = activation_methods
        self.activation_derivative = activation_derivatives
        self.weights = initialize_weights(architecture)
        self.outputs = initialize_outputs(architecture, data_dim)
        self.derivatives = initialize_outputs(architecture, data_dim)

    def feed(self, x):
        for i, weights in enumerate(self.weights):
            preactivation = np.matmul(weights, x)
            self.derivatives[i] = self.activation_derivative(preactivation)
            x = self.outputs[i] = self.activation_method(preactivation)
        return x

    def back_propagation_multiple(self, dloss, current_point, expected):
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
            self.weights[layer] += self.update.get_delta(last_gradient, layer)

        # weights_transposed = self.weights[0].T
        # return np.matmul(weights_transposed, multipliers[0])
        return multipliers[0]

    def back_propagation(self, dloss, expected):
        multipliers = []
        current_layer = len(self.weights) - 1
        # base = np.matmul(np.diag(self.derivatives[current_layer]), dloss)
        base = dloss * self.derivatives[current_layer]
        multipliers.append(base)
        current_layer -= 1
        while current_layer >= 0:
            diagonal = np.diag(self.derivatives[current_layer])
            weights_transposed = self.weights[current_layer + 1].T
            base = np.matmul(np.matmul(diagonal, weights_transposed), base)
            multipliers.append(base)
            current_layer -= 1
        multipliers = multipliers[::-1]

        for layer in reversed(range(len(self.weights))):
            if layer == 0:
                base = np.array(expected)
            else:
                base = self.outputs[layer - 1]
            last_gradient = np.transpose(np.outer(base, multipliers[layer]))
            self.weights[layer] += self.update.get_delta(last_gradient, layer)

        # weights_transposed = self.weights[0].T
        # return np.matmul(weights_transposed, multipliers[0])
        return multipliers[0]


# I + W1 -> O2 -> O2 + W2 -> X'
# d(||X-X'||)/dX'
# O3 = h( W2 * O2 )
# dloss/dW2 = dloss/dO2 * dO2/dW1 = dloss/dO2 * h'( W1 * O1 ) * O1 = gradiente de W1
# ...s/dO3 * dO3/dW2 = dloss/dO3 * h'( W2 * O2 ) * O2 = gradiente de W2
# # dloss/dO2 = dloss/dO3 * dO3/dO2 = dloss/dO3 * h'( W2 * O2 ) * W2
# # dloss/dO2
# # dloss/dW1 = dlos

# dloss/dO2 =  dloss/dx' * dx'/dO2 = dloss/dx' * h'(preac) * W1
#

# I + W1 -> O2 -> O2 + W2 -> m
# d(MSE + KL)/dm
# m = h( W2 * O2 )
# dloss/dW2 = dloss/dm * dO3/dW2 = dloss/dm * h'( W2 * O2 ) * O2 = gradiente de W2
# dloss/dO2 = dloss/dm * dO3/dO2 = dloss/dm * h'( W2 * O2 ) * W2
# dloss/dO2
# dloss/dW1 = dloss/dO2 * dO2/dW1 = dloss/dO2 * h'( W1 * O1 ) * O1 = gradiente de W1
