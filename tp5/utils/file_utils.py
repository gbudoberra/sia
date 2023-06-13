import os.path

import numpy as np


def write_weights_to_file(weights, file_prefix):
    i = 1
    while os.path.exists(f'{file_prefix}_{i}.txt'):
        i += 1

    with open(f'{file_prefix}_{i}.txt', 'wb') as f:
        for a in weights:
            np.save(f, np.array(a))
    print(f'Weights saved to {file_prefix}_{i}.txt')


def read_weights_from_file(layers, file_name):
    weights = []
    with open(file_name, 'rb') as f:
        for i in range(layers - 1):
            weights.append(np.load(f))
    return weights
