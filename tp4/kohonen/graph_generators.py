import numpy as np
import matplotlib.pyplot as plt


def plot_heat_map(data):
    max_row = max(data.keys(), key=lambda x: x[0])[0]
    max_col = max(data.keys(), key=lambda x: x[1])[1]
    country_matrix = np.zeros((max_row + 1, max_col + 1), dtype=int)
    for key, countries in data.items():
        row, col = key
        country_matrix[row, col] = len(countries)

    plt.imshow(country_matrix, cmap='YlOrRd')
    plt.xticks(range(max_col + 1), range(max_col + 1))
    plt.yticks(range(max_row + 1), range(max_row + 1))

    plt.xlabel('Columna')
    plt.ylabel('Fila')
    for i in range(max_row + 1):
        for j in range(max_col + 1):
            plt.text(j, i, country_matrix[i, j], ha='center', va='center', color='black', fontsize=8)
    plt.colorbar()
    plt.show()


def plot_avg_distance(matriz):
    plt.imshow(matriz, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.show()
