import numpy as np
from PIL import Image


def map_zeros(data):
    for i in range(len(data)):
        data[i] = np.where(data[i] == 0, -1, data[i])


def map_minus_one(data):
    for i in range(len(data)):
        data[i] = np.where(data[i] == -1, 0, data[i])
        data[i] = np.where(data[i] == 1, 255, data[i])


def plot_array(array, filename, png_size):
    map_minus_one(array)
    matrix = np.reshape(array, (png_size, png_size))
    matrix = matrix.astype(np.uint8)
    image = Image.fromarray(matrix)
    image.save(filename)


def load_number_image(png_filename):
    image = Image.open(png_filename)
    array = np.array(image)
    binary_array = (array[:, :, 0] < 128).astype(int)
    return binary_array


def initialize_points(noise, characters):
    parsing_png_points = []
    for character in characters:
        name = get_image_path(character, 5, noise, 0)
        image_matrix = load_number_image(name)
        parsing_png_points.append(np.ravel(image_matrix))
    return parsing_png_points


def get_image_path(num, noise, noisy, i):
    if not noisy:
        return f'./images/noise_{noise}/{num}_character.png'
    else:
        return f'./images/noise_{noise}/' + str(num) + '_character_with_error_' + str(i) + '.png'
