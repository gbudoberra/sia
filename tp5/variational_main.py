import matplotlib.pyplot as plt
import numpy as np

from tp3.multilayer.multilayerperceptron import sigmoid, sigmoid_deriv
from tp5.font import get_font_as_xis, draw_flattened_char
from tp5.perceptrons.Perceptron import Perceptron
from tp5.perceptrons.VariationalPerceptron import VariationalPerceptron
from tp5.update_methods.GradientDescendent import GradientDescendent
from tp5.utils.JsonReader import JsonReader
from tp5.utils.file_utils import write_weights_to_file


def activation(preactivation):
    return np.vectorize(sigmoid)(preactivation)


def activation_derivative(preactivation):
    return np.vectorize(sigmoid_deriv)(preactivation)


def plot_latent_space_from_dataset(variational, data_set):
    plt.clf()
    latent_space = []
    for x in data_set:
        result = []
        for _ in range(100):
            result.append(variational.get_distribution(x))
        latent_space.append(result)
    for i, space in enumerate(latent_space):
        plt.scatter(
            [z[0] for z in space],
            [z[1] for z in space],
            label=str(i)
        )
    plt.legend()
    plt.show()
    plt.clf()


if __name__ == '__main__':
    config = JsonReader()
    data_set = get_font_as_xis()
    result_set = data_set

    encoder_architecture = [35, 10, 5, 2]
    m_encoder = Perceptron(encoder_architecture, len(data_set), activation, activation_derivative,
                           GradientDescendent(config.learning_rate))
    s_encoder = Perceptron(encoder_architecture, len(data_set), activation, activation_derivative,
                           GradientDescendent(config.learning_rate))

    decoder_architecture = encoder_architecture[::-1]
    decoder = Perceptron(decoder_architecture, len(data_set), activation, activation_derivative,
                         GradientDescendent(config.learning_rate))

    variational = VariationalPerceptron(m_encoder, s_encoder, decoder, data_set, len(data_set))

    variational.train()
    write_weights_to_file(m_encoder.weights, './variational_weights/W_m_encoder')
    write_weights_to_file(s_encoder.weights, './variational_weights/W_s_encoder')
    write_weights_to_file(decoder.weights, './variational_weights/W_decoder')

    image = data_set[0]
    draw_flattened_char(image, 0)

    z = variational.get_distribution(data_set[0])
    generated = variational.generate_from(z)
    draw_flattened_char(generated, 0)

    plot_latent_space_from_dataset(variational, data_set)
