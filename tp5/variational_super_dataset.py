import numpy as np
from keras.datasets import mnist

from tp5.perceptrons.Perceptron import Perceptron
from tp5.perceptrons.VariationalPerceptron import VariationalPerceptron
from tp5.update_methods.GradientDescendent import GradientDescendent
from tp5.utils.file_utils import write_weights_to_file
from tp5.variational_main import plot_latent_space_from_dataset, activation, activation_derivative

if __name__ == '__main__':
    learning_rate = 0.1

    (train_X, train_y), (test_X, test_y) = mnist.load_data()
    data_set = []

    for x in train_X[:2000]:
        data_set.append(np.reshape(x, -1))

    for data in data_set:
        for i in range(len(data)):
            if data[i] > 0:
                data[i] = 1
            else:
                data[i] = 0

    encoder_architecture = [784, 20, 5, 2]
    m_encoder = Perceptron(encoder_architecture, len(data_set), activation, activation_derivative,
                           GradientDescendent(learning_rate))
    s_encoder = Perceptron(encoder_architecture, len(data_set), activation, activation_derivative,
                           GradientDescendent(learning_rate))

    decoder_architecture = encoder_architecture[::-1]
    decoder = Perceptron(decoder_architecture, len(data_set), activation, activation_derivative,
                         GradientDescendent(learning_rate))

    variational = VariationalPerceptron(m_encoder, s_encoder, decoder, data_set, len(data_set))
    variational.train()

    write_weights_to_file(m_encoder.weights, './variational_weights/W_m_encoder')
    write_weights_to_file(s_encoder.weights, './variational_weights/W_s_encoder')
    write_weights_to_file(decoder.weights, './variational_weights/W_decoder')

    plot_latent_space_from_dataset(variational, data_set[:6])
