import matplotlib.pyplot as plt
import numpy as np


def plot_heat_map(data, k):
    plt.clf()
    fig, ax = plt.subplots(figsize=(8, 8))
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
            plt.text(j, i, country_matrix[i, j], ha='center', va='center', color='black')
    plt.colorbar()
    plt.savefig('heatmap' + str(k) + '.png', dpi=300)


def plot_heat_map_with_names(data, k):
    plt.clf()
    fig, ax = plt.subplots(figsize=(8, 8))
    country_matrix = np.zeros((k, k), dtype=int)
    plt.figure(figsize=(20, 12))
    for key, countries in data.items():
        row, col = key
        plt.text(col, row, '\n'.join(countries), ha='center', va='center', color='black')
        country_matrix[row, col] = len(countries)

    plt.imshow(country_matrix, cmap='YlOrRd')
    plt.xticks(range(k), range(k))
    plt.yticks(range(k), range(k))

    plt.xlabel('Columna')
    plt.ylabel('Fila')
    plt.colorbar()
    plt.savefig('heatmapNames' + str(k) + '.png', dpi=300)


def plot_avg_distance(matriz, k):
    plt.clf()
    fig, ax = plt.subplots(figsize=(8, 8))

    max_col = k - 1
    max_row = k - 1
    plt.imshow(matriz, cmap='gray', interpolation='nearest')
    plt.xticks(range(max_col + 1), range(max_col + 1))
    plt.yticks(range(max_row + 1), range(max_row + 1))
    plt.colorbar()
    plt.savefig('avgDistance' + str(k) + '.png', dpi=300)


def plot_avg_elements_distance_per_k(elements, distances, elements_std, distances_std):
    plt.clf()
    k = range(3, 10)
    width = 0.35  # Width of each bar

    fig, ax = plt.subplots()
    rects1 = ax.bar(k, elements, width, label='Elementos por Celda', yerr=elements_std)
    rects2 = ax.bar([x + width for x in k], distances, width, label='Distancia promedio', yerr=distances_std)
    # rects3 = ax.bar([x + width * 2 for x in k], groups_cant, width, label='Grupos')

    ax.set_xlabel('K')
    ax.set_ylabel('Value')
    ax.set_title('Average Elements and Distances per K')
    ax.set_xticks([x + width / 2 for x in k])
    ax.set_xticklabels(k)
    ax.legend()

    plt.savefig('avgElementsDistancesPerK.png')


def plot_groups_per_k(groups_cant):
    plt.clf()
    k = range(3, 10)
    width = 0.35  # Width of each bar

    fig, ax = plt.subplots()
    rects1 = ax.bar(k, groups_cant, width, label='Grupos')

    ax.set_xlabel('K')
    ax.set_ylabel('Value')
    ax.set_title('Groups per K')
    ax.set_xticks([x + width / 2 for x in k])
    ax.set_xticklabels(k)
    ax.legend()

    plt.savefig('groupsPerK.png')
