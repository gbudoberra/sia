import itertools
import random

import matplotlib.pyplot as plt
import numpy as np

from harcoded_main import noise_with_p
from tp4.hopfield.hopfield import Hopfield
from tp4.hopfield.utils import plot_array

letter_array = [
    # A
    [1, 1, 1, 1, 1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, 1,
     1, -1, -1, -1, 1,
     1, -1, -1, -1, 1],

    # B
    [1, 1, 1, 1, -1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, -1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, -1],

    # C
    [1, 1, 1, 1, 1,
     1, -1, -1, -1, -1,
     1, -1, -1, -1, -1,
     1, -1, -1, -1, -1,
     1, 1, 1, 1, 1],

    # D
    [1, 1, 1, 1, -1,
     1, -1, -1, 1, 1,
     1, -1, -1, -1, 1,
     1, -1, -1, 1, 1,
     1, 1, 1, 1, -1],

    # E
    [1, 1, 1, 1, 1,
     1, -1, -1, -1, -1,
     1, 1, 1, 1, 1,
     1, -1, -1, -1, -1,
     1, 1, 1, 1, 1],

    # F
    [1, 1, 1, 1, 1,
     1, -1, -1, -1, -1,
     1, 1, 1, 1, 1,
     1, -1, -1, -1, -1,
     1, -1, -1, -1, -1],

    # G
    [1, 1, 1, 1, 1,
     1, -1, -1, -1, -1,
     1, -1, 1, 1, 1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, 1],

    # H
    [1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, 1,
     1, -1, -1, -1, 1,
     1, -1, -1, -1, 1],

    # I
    [-1, 1, 1, 1, -1,
     -1, -1, 1, -1, -1,
     -1, -1, 1, -1, -1,
     -1, -1, 1, -1, -1,
     -1, 1, 1, 1, -1],

    # J
    [-1, -1, -1, -1, 1,
     -1, -1, -1, -1, 1,
     -1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, -1],

    # K
    [1, -1, -1, -1, 1,
     1, -1, -1, 1, -1,
     1, 1, 1, -1, -1,
     1, -1, -1, 1, -1,
     1, -1, -1, -1, 1],

    # L
    [1, -1, -1, -1, -1,
     1, -1, -1, -1, -1,
     1, -1, -1, -1, -1,
     1, -1, -1, -1, -1,
     1, 1, 1, 1, 1],

    # M
    [1, -1, -1, -1, 1,
     1, 1, -1, 1, 1,
     1, -1, 1, -1, 1,
     1, -1, -1, -1, 1,
     1, -1, -1, -1, 1],

    # N
    [1, -1, -1, -1, 1,
     1, 1, -1, -1, 1,
     1, -1, 1, -1, 1,
     1, -1, -1, 1, 1,
     1, -1, -1, -1, 1],

    # O
    [1, 1, 1, 1, 1,
     1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, 1],

    # P
    [1, 1, 1, 1, -1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, -1,
     1, -1, -1, -1, -1,
     1, -1, -1, -1, -1],

    # Q
    [1, 1, 1, 1, 1,
     1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     1, -1, 1, -1, 1,
     1, 1, 1, 1, 1],

    # R
    [1, 1, 1, 1, -1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, -1,
     1, -1, -1, 1, -1,
     1, -1, -1, -1, 1],

    # S
    [1, 1, 1, 1, 1,
     1, -1, -1, -1, -1,
     1, 1, 1, 1, 1,
     -1, -1, -1, -1, 1,
     1, 1, 1, 1, 1],

    # T
    [1, 1, 1, 1, 1,
     -1, -1, 1, -1, -1,
     -1, -1, 1, -1, -1,
     -1, -1, 1, -1, -1,
     -1, -1, 1, -1, -1],

    # U
    [1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, 1],

    # V
    [1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     -1, 1, -1, 1, -1,
     -1, -1, 1, -1, -1],

    # W
    [1, -1, -1, -1, 1,
     1, -1, -1, -1, 1,
     1, -1, 1, -1, 1,
     1, 1, -1, 1, 1,
     1, -1, -1, -1, 1],

    # X
    [1, -1, -1, -1, 1,
     -1, 1, -1, 1, -1,
     -1, -1, 1, -1, -1,
     -1, 1, -1, 1, -1,
     1, -1, -1, -1, 1],

    # Y
    [1, -1, -1, -1, 1,
     -1, 1, -1, 1, -1,
     -1, -1, 1, -1, -1,
     -1, -1, 1, -1, -1,
     -1, -1, 1, -1, -1],

    # Z
    [1, 1, 1, 1, 1,
     -1, -1, -1, 1, -1,
     -1, -1, 1, -1, -1,
     -1, 1, -1, -1, -1,
     1, 1, 1, 1, 1]
]


def get_subarray(array, indices):
    return [array[i] for i in indices]


def plot_energy(filename, energies):
    for noise, energy in zip(energies.keys(), energies.values()):
        plt.plot(energy, label=f'noise={noise}')
    plt.xlabel('Iteración')
    plt.ylabel('Energía')
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.clf()


def test_noises(indexes, name, images_path):
    initial_letter = letter_array[indexes[random.randint(0, len(indexes) - 1)]]
    array = get_subarray(letter_array, indexes)
    plot_array(initial_letter.copy(), f"{images_path}{name}_initial.png", 5)
    hopfield = Hopfield(array, 1000)

    energies = {}

    for noise in [0.1, 0.2, 0.3, 0.4]:
        modified_initial = noise_with_p(initial_letter, noise)
        hopfield.get_pattern(modified_initial, images_path + f'{name}_{noise}', 5)
        energies[noise] = hopfield.energy

    plot_energy(images_path + f'{name}_energy.png', energies)


if __name__ == '__main__':
    file = f'./images/patterns/letter_'
    for i, letter in zip(range(len(letter_array)), letter_array):
        plot_array(letter.copy(), file + str(i) + ".png", 5)

    groups = itertools.combinations(range(len(letter_array)), r=4)
    avg_dot_product = []
    max_dot_product = []
    for g in groups:
        group = np.array([letter_array[i].copy() for i in g])
        orto_matrix = group.dot(group.T)
        np.fill_diagonal(orto_matrix, 0)
        row, _ = orto_matrix.shape
        avg_dot_product.append((np.abs(orto_matrix).sum() / (orto_matrix.size - row), g))
        max_v = np.abs(orto_matrix).max()
        max_dot_product.append(((max_v, np.count_nonzero(np.abs(orto_matrix) == max_v) / 2), g))

    sorted_results = sorted(avg_dot_product)
    path = f'./images/results/'

    worst = sorted_results[-1][1]
    best = sorted_results[0][1]
    for b in best:
        plot_array(letter_array[b].copy(), f"letter_{b}_best.png", 5)
    for w in worst:
        plot_array(letter_array[w].copy(), f"letter_{w}_worst.png", 5)

    test_noises(best, 'best', path)
    test_noises(worst, 'worst', path)
