import matplotlib.pyplot as plt
import numpy as np

from tp5.font import get_font_as_xis, draw_flattened_char, labels
from tp5.perceptrons.Perceptron import Perceptron
from tp5.perceptrons.VariacionalSimpleSampling import VariacionalSimpleSampling
from tp5.perceptrons.VariationalPerceptron import transform_to_binary
from tp5.update_methods.Adam import Adam
from tp5.utils.JsonReader import JsonReader
from tp5.utils.file_utils import write_weights_to_file
from tp5.variational_main import activation_decoder, activation_derivative_decoder, activation_derivative, activation


def add_noise(matrix):
    noise = np.random.random(matrix.shape)
    mask = noise < 0
    noisy_matrix = np.where(mask, 1 - matrix, matrix)
    return noisy_matrix


if __name__ == '__main__':
    config = JsonReader()
    expected = get_font_as_xis()

    # for i, array in enumerate(expected):
    #     for j, e in enumerate(array):
    #         if e == 0:
    #             expected[i][j] = -1

    data_set = expected
    result_set = expected

    encoder_architecture = [35, 20, 10, 2]
    m_encoder = Perceptron(encoder_architecture, len(data_set), activation, activation_derivative,
                           Adam(config.learning_rate, encoder_architecture))
    s_encoder = Perceptron(encoder_architecture, len(data_set), activation, activation_derivative,
                           Adam(config.learning_rate, encoder_architecture))

    decoder_architecture = encoder_architecture[::-1]
    decoder = Perceptron(decoder_architecture, len(data_set), activation_decoder, activation_derivative_decoder,
                         Adam(config.learning_rate, decoder_architecture))

    variational = VariacionalSimpleSampling(m_encoder, s_encoder, decoder, data_set, len(data_set), result_set)

    variational.train()
    write_weights_to_file(m_encoder.weights, './variational_weights/W_m_encoder')
    write_weights_to_file(s_encoder.weights, './variational_weights/W_s_encoder')
    write_weights_to_file(decoder.weights, './variational_weights/W_decoder')

    # latent_space = []
    #
    # for i, data in enumerate(expected):
    #     print(i)
    #     result = variational.feed_forward(add_noise(data))
    #     draw_flattened_char(transform_to_binary(result), i)
    #     zs = []
    #     for _ in range(1000):
    #         zs.append(variational.get_z(add_noise(data)))
    #     latent_space.append(zs)
    #
    # cmap = plt.cm.get_cmap('rainbow')
    # for i, data in enumerate(latent_space):
    #     plt.scatter([z[0] for z in data], [z[1] for z in data], label=labels[i], color=cmap(i / len(latent_space)))
    # plt.legend()
    # plt.show()
    # plt.clf()

    variational.plot_errors()
