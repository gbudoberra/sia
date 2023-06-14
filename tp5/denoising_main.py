import random

from tp5.font import get_font_as_xis, draw_flattened_char
from tp5.perceptrons.AutoencoderPerceptron import AutoencoderPerceptron
from tp5.utils.JsonReader import JsonReader
from tp5.utils.file_utils import write_weights_to_file
from tp5.denoising_main_pre_trained import get_noisy_image

weights_file = "weights_6.txt"
latent_layer = 5

if __name__ == '__main__':
    config = JsonReader()
    data_set = get_font_as_xis()

    std = 0.1

    # add some noise to the dataset.
    noisy_data_set = []
    noiseless_data_set = []

    noisy_per_image = 6

    for i in range(noisy_per_image * len(data_set)):
        index, noisy_image = get_noisy_image(data_set, std)
        noisy_data_set.append(noisy_image)
        noiseless_data_set.append(data_set[index])

    pre_trained = AutoencoderPerceptron(
        [35, 10, 10, 10, 35],
        noisy_data_set,
        config.activation_method,
        noiseless_data_set,
        len(noisy_data_set),
        config.learning_rate,
        config.update_method,
        10000
    )

    pre_trained.train()

    write_weights_to_file(pre_trained.get_weights(), "denoising_weights")
