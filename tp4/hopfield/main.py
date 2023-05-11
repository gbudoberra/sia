import matplotlib.pyplot as plt

from utils import initialize_points
from config import Config
import numpy as np
from PIL import Image
from tp4.imageGenerator import generate_character_list
from hopfield import Hopfield


def map_zeros(data):
    for i in range(len(data)):
        data[i] = np.where(data[i] == 0, -1, data[i])


def map_minus_one(data):
    for i in range(len(data)):
        data[i] = np.where(data[i] == -1, 0, data[i])
        data[i] = np.where(data[i] == 1, 255, data[i])


if __name__ == '__main__':
    config = Config()
    # generate_character_list(config.characters, config.noises)

    points = initialize_points(False, config.characters)
    points_with_error = initialize_points(True, config.characters)
    map_zeros(points)
    map_zeros(points_with_error)

    hopfield_net = Hopfield(points, 1000)
    result = []
    for point in points_with_error:
        result.append(hopfield_net.get_pattern(point))

    matrices = []
    for c, r in zip(config.characters, result):
        map_minus_one(r)
        matrix = np.reshape(r, (50, 50))
        matrices.append(matrix)
        image = Image.fromarray(matrix)
        image.show()
