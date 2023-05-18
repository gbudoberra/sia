import matplotlib.pyplot as plt
import numpy as np


def plot_heat_map(data, k):
    country_matrix = np.zeros((k, k), dtype=int)
    for key, countries in data.items():
        row, col = key
        country_matrix[row, col] = len(countries)

    plt.imshow(country_matrix, cmap='YlOrRd')
    plt.xticks(range(k), range(k))
    plt.yticks(range(k), range(k))

    plt.xlabel('Columna')
    plt.ylabel('Fila')
    for i in range(k):
        for j in range(k):
            plt.text(j, i, country_matrix[i, j], ha='center', va='center', color='black', fontsize=8)
    plt.colorbar()
    plt.show()
    plt.clf()


def plot_heat_map_with_names(data, k):
    country_matrix = np.zeros((k, k), dtype=int)
    plt.figure(figsize=(20, 12))
    for key, countries in data.items():
        row, col = key
        plt.text(col, row, '\n'.join(countries), ha='center', va='center', color='black', fontsize=12)
        country_matrix[row, col] = len(countries)

    plt.imshow(country_matrix, cmap='YlOrRd')
    plt.xticks(range(k), range(k))
    plt.yticks(range(k), range(k))

    plt.xlabel('Columna')
    plt.ylabel('Fila')
    plt.colorbar()
    plt.show()


def plot_avg_distance(matriz, k):
    max_col = k - 1
    max_row = k - 1
    plt.imshow(matriz, cmap='gray', interpolation='nearest')
    plt.xticks(range(max_col + 1), range(max_col + 1))
    plt.yticks(range(max_row + 1), range(max_row + 1))
    plt.colorbar()
    plt.show()


