import numpy as np

from tp3.multilayer.multilayerperceptron import sigmoid, sigmoid_deriv
from tp5.font import get_font_as_xis
from tp5.perceptrons.Perceptron import Perceptron
from tp5.perceptrons.VariationalPerceptron import VariationalPerceptron
from tp5.utils.JsonReader import JsonReader


def activation(preactivation):
    return np.vectorize(sigmoid)(preactivation)


def activation_derivative(preactivation):
    return np.vectorize(sigmoid_deriv)(preactivation)


if __name__ == '__main__':
    config = JsonReader()
    data_set = get_font_as_xis()
    result_set = data_set

    sample_size = 10

    m_encoder = Perceptron([35, 10, 2], len(data_set), activation, activation_derivative, config.learning_rate)
    s_encoder = Perceptron([35, 10, 2], len(data_set), activation, activation_derivative, config.learning_rate)

    decoder = Perceptron([2, 10, 35], len(data_set), activation, activation_derivative, config.learning_rate)

    variational = VariationalPerceptron(m_encoder, s_encoder, decoder, data_set, len(data_set))

    variational.train()
