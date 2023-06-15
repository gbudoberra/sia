import numpy as np
from tp3.multilayer.multilayerperceptron import MultiLayerPerceptron


def reparameterization_trick(x):
    mid = len(x) / 2
    mean = x[:mid]
    std = x[mid:]
    epsilon = np.random.standard_normal()
    return mean * epsilon + std


def identity(x):
    return x


class Variational:
    def __init__(self, points, encoder_perceptron_by_layer, decoder_perceptron_by_layer, activation_method, epsilon,
                 learning_rate, last_dim):
        normal_distribution = np.random.standard_normal((len(points), len(points[0])))
        encoder_perceptron_by_layer.append(last_dim)
        self.points = points
        self.epsilon = epsilon
        self.encoder = MultiLayerPerceptron(
            encoder_perceptron_by_layer,
            points,
            activation_method,
            normal_distribution,
            epsilon,
            learning_rate
        )

        decoder_perceptron_by_layer.insert(0, last_dim / 2)
        self.decoder = MultiLayerPerceptron(
            decoder_perceptron_by_layer,
            points,
            activation_method,
            points,
            epsilon,
            learning_rate
        )

    def feed_forward(self):
        for p in self.points:
            encoder_result = self.encoder.get_result(p)
            decoder_input = reparameterization_trick(encoder_result)
            result = self.decoder.get_result(decoder_input)
            self.encoder.adam_update(self.get_gradient(result))
            self.decoder.adam_update(self.get_gradient(result))

    def get_gradient(self, result):
        return result

    def loss_function(self, x, encoder_result, decoder_result):
        mean = encoder_result[:len(encoder_result) / 2]
        std = encoder_result[len(encoder_result) / 2:]
        return -0.5 * (1 + std - np.square(mean) - np.exp(std))
