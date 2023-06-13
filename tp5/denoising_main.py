import random

from tp5.font import get_font_as_xis, draw_flattened_char
from tp5.perceptrons.AutoencoderPerceptron import AutoencoderPerceptron
from tp5.utils.JsonReader import JsonReader
from tp5.utils.file_utils import write_weights_to_file
from tp5.denoising_main_pre_trained import get_noisy_image

weights_file = "weights_2.txt"
latent_layer = 5

if __name__ == '__main__':
    config = JsonReader()
    data_set = get_font_as_xis()

    noise_rate = 0.01

    # add some noise to the dataset.
    noisy_data_set = []
    noiseless_data_set = []

    for i in range(2 * len(data_set)):
        index, noisy_image = get_noisy_image(data_set, noise_rate)
        noisy_data_set.append(noisy_image)
        noiseless_data_set.append(data_set[index])

    pre_trained = AutoencoderPerceptron(
        [35, 10, 2, 10, 35],
        noisy_data_set,
        config.activation_method,
        noiseless_data_set,
        2 * len(noisy_data_set),
        config.learning_rate,
        config.update_method,
        20000
    )

    pre_trained.train()

    write_weights_to_file(pre_trained.get_weights(), "denoising_weights")
