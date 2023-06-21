import matplotlib.pyplot as plt
import numpy as np

from tp3.multilayer.multilayerperceptron import sigmoid, sigmoid_deriv, activation_methods_dictionary
from tp5.font import get_font_as_xis, draw_flattened_char
from tp5.perceptrons.Perceptron import Perceptron
from tp5.perceptrons.VariationalPerceptron import VariationalPerceptron
from tp5.update_methods.Adam import Adam
from tp5.utils.JsonReader import JsonReader
from tp5.utils.file_utils import write_weights_to_file


def activation(preactivation):
    return np.vectorize(sigmoid)(preactivation)
    # return np.vectorize(activation_methods_dictionary["id"][0])(preactivation)


def activation_derivative(preactivation):
    return np.vectorize(sigmoid_deriv)(preactivation)
    # return np.vectorize(activation_methods_dictionary["id"][1])(preactivation)


def activation_decoder(preactivation):
    return np.vectorize(sigmoid)(preactivation)


def activation_derivative_decoder(preactivation):
    return np.vectorize(sigmoid_deriv)(preactivation)


def plot_latent_space_from_dataset(variational, data_set):
    plt.clf()
    latent_space = []
    for x in data_set:
        result = []
        for _ in range(1000):
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


def plot(error):
    plt.plot(range(len(error)), error)
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    config = JsonReader()
    data_set = get_font_as_xis()

    encoder_architecture = [35, 10, 2]
    m_encoder = Perceptron(encoder_architecture, len(data_set), activation_decoder, activation_derivative_decoder,
                           Adam(config.learning_rate, encoder_architecture))
    s_encoder = Perceptron(encoder_architecture, len(data_set), activation_decoder, activation_derivative_decoder,
                           Adam(config.learning_rate, encoder_architecture))

    decoder_architecture = encoder_architecture[::-1]
    decoder = Perceptron(decoder_architecture, len(data_set), activation_decoder, activation_derivative_decoder,
                         Adam(config.learning_rate, decoder_architecture))

    variational = VariationalPerceptron(m_encoder, s_encoder, decoder, data_set, 100)

    variational.train()
    write_weights_to_file(m_encoder.weights, './variational_weights/W_m_encoder')
    write_weights_to_file(s_encoder.weights, './variational_weights/W_s_encoder')
    write_weights_to_file(decoder.weights, './variational_weights/W_decoder')

    for i in range(len(data_set)):
        image = data_set[i]
        print(i)
        z = (variational.get_distribution(data_set[i]))
        generated = variational.generate_from(z)
        draw_flattened_char(generated, i)

    plot_latent_space_from_dataset(variational, data_set)
    # plot(variational.mses)
    # plot(variational.kls)
