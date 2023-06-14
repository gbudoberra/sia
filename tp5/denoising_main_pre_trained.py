import random

import matplotlib.pyplot as plt
import numpy as np

from tp5.font import get_font_as_xis
from tp5.perceptrons.PreTrainedPerceptron import PreTrainedPerceptron
from tp5.utils.JsonReader import JsonReader
from tp5.utils.file_utils import read_weights_from_file


def get_noisy_image(data, noise_rate):
    index = random.randint(0, len(data) - 1)
    noisy_image = data[index].copy()
    for j in range(len(noisy_image)):
        if random.random() < noise_rate:
            noisy_image[j] = 1 - noisy_image[j]
    return index, noisy_image


def get_gaussian_noisy_image(data, std):
    index = random.randint(0, len(data) - 1)
    noisy_image = data[index].copy()
    noisy_image = noisy_image.astype(np.float64)
    noisy_image += np.random.normal(0, std, len(noisy_image))  # add noise
    return index, noisy_image


def get_gaussian_noisy_image_by_index(index, data, std):
    noisy_image = data[index].copy()
    noisy_image = noisy_image.astype(np.float64)
    noisy_image += np.random.normal(0, std, (7, 5))  # add noise
    return index, noisy_image


def get_closer_image(data, output):
    distance = []
    for image in data:
        distance.append(np.linalg.norm(image - output))
    return distance.index(min(distance))


weights_file = "denoising_weights_5.txt"
latent_layer = 3

if __name__ == '__main__':
    config = JsonReader()
    data_set = get_font_as_xis()
    result_set = data_set

    pre_trained = PreTrainedPerceptron(
        read_weights_from_file(len(["sigmoid", "sigmoid", "sigmoid", "sigmoid", "sigmoid"]), weights_file),
        ["sigmoid", "sigmoid", "sigmoid", "sigmoid", "sigmoid"],
        latent_layer
    )

    counter = 0
    image_total = 1000
    for i in range(image_total):
        index, noisy_image = get_noisy_image(data_set, 0.1)
        nn_result = pre_trained.get_result(noisy_image)
        result_index = get_closer_image(data_set, nn_result)
        if result_index == index:
            counter += 1

    labels = ['Aciertos', 'No aciertos']
    sizes = [counter, image_total - counter]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.show()
