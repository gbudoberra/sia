from random import random

from matplotlib import pyplot as plt

from tp5.font import get_font_as_xis, labels, draw_flattened_char, draw_flattened_char_with_title
from tp5.perceptrons.PreTrainedPerceptron import PreTrainedPerceptron
from tp5.utils.JsonReader import JsonReader
from tp5.utils.file_utils import read_weights_from_file

weights_file = "weights_2.txt"
latent_layer = 4

if __name__ == '__main__':
    config = JsonReader()
    data_set = get_font_as_xis()
    result_set = data_set

    pre_trained = PreTrainedPerceptron(
        read_weights_from_file(len(config.activation_method), weights_file),
        config.activation_method,
        latent_layer
    )

    latent_space = []
    for X in data_set:
        Y = pre_trained.get_latent_result(X)
        latent_space.append(Y)

    x = [p[0] for p in latent_space]
    y = [p[1] for p in latent_space]

    plt.scatter(x, y)

    for label, x_i, y_i in zip(labels, x, y):
        plt.annotate(label, (x_i, y_i), xytext=(5, 5), textcoords='offset points')

    plt.grid(True)
    plt.show()

    plt.scatter(x, y)

    px = [random() * max(x) for _ in range(5)]
    py = [random() * max(x) for _ in range(5)]

    plt.scatter(px, py, color='red')

    for i, x_i, y_i in zip(range(len(px)), px, py):
        plt.annotate(str(i), (x_i, y_i), xytext=(5, 5), textcoords='offset points')

    for label, x_i, y_i in zip(labels, x, y):
        plt.annotate(label, (x_i, y_i), xytext=(5, 5), textcoords='offset points')

    plt.grid(True)
    plt.show()

    for i, x_i, y_i in zip(range(len(px)), px, py):
        draw_flattened_char_with_title(pre_trained.generate_from_latent_space([x_i, y_i]), f'Character: {str(i)}')
