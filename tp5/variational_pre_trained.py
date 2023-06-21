import numpy as np
from matplotlib import pyplot as plt
from seaborn import heatmap

from tp5.font import get_font_as_xis, draw_flattened_char, labels
from tp5.perceptrons.PreTrainedVariational import PreTrainedVariational
from tp5.perceptrons.VariationalPerceptron import transform_to_binary
from tp5.utils.file_utils import read_weights_from_file
from tp5.variational_main import activation, activation_decoder

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt


def plot_latent_space_results(variational):
    data = None
    cols = np.arange(-1.5, 1.5, 0.25)
    rows = np.arange(-2, 0.5, 0.25)
    for row in rows:
        data_r = None
        for col in cols:
            r = transform_to_binary(variational.feed_z([row, col]))
            if data_r is None:
                data_r = r.reshape(7, -1)
            else:
                data_r = np.concatenate((data_r, r.reshape(7, -1)), axis=1)
        if data is None:
            data = data_r
        else:
            data = np.concatenate((data, data_r), axis=0)

    fig, ax = plt.subplots(figsize=(8, 8), gridspec_kw={'hspace': 0.5, 'wspace': 0.2})

    plt.xticks(np.arange(len(cols)) * 5, cols, rotation='vertical')
    plt.yticks(np.arange(len(rows)) * 7, rows)

    monocromatic_cmap = plt.get_cmap('binary')
    ax.imshow(data, cmap=monocromatic_cmap, interpolation='nearest')
    plt.tight_layout()
    plt.show()
    plt.clf()


if __name__ == '__main__':
    expected = get_font_as_xis()

    # for i, array in enumerate(expected):
    #     for j, e in enumerate(array):
    #         if e == 0:
    #             expected[i][j] = -1

    i = 1
    n_layers = 4
    decoder_weights = read_weights_from_file(n_layers, f'./variational_weights/W_decoder_kl3_{i}.txt')
    s_weights = read_weights_from_file(n_layers, f'./variational_weights/W_s_encoder_kl3_{i}.txt')
    m_weights = read_weights_from_file(n_layers, f'./variational_weights/W_m_encoder_kl3_{i}.txt')

    variational = PreTrainedVariational(m_weights, s_weights, decoder_weights, activation, activation_decoder)

    plot_latent_space_results(variational)

    # latent_space = []
    # for i, data in enumerate(expected):
    #     print(i)
    # result = variational.feed_forward(data)
    # draw_flattened_char(data, i)
    #     zs = []
    #     for _ in range(1000):
    #         zs.append(variational.get_z(data))
    #     latent_space.append(zs)
    #
    # cmap = plt.cm.get_cmap('rainbow')
    # for i, data in enumerate(latent_space):
    #     plt.scatter([z[0] for z in data], [z[1] for z in data], label=labels[i], color=cmap(i / len(latent_space)))
    # plt.legend()
    # plt.show()
    # plt.clf()
