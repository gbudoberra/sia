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


def plot_avg_distance(matriz, k):
    max_col = k - 1
    max_row = k - 1
    plt.imshow(matriz, cmap='gray', interpolation='nearest')
    plt.xticks(range(max_col + 1), range(max_col + 1))
    plt.yticks(range(max_row + 1), range(max_row + 1))
    plt.colorbar()
    plt.show()


def plot_assigned_categories(category_map):
    categories = set(category_map.values())
    colormap = plt.cm.get_cmap('tab20', len(categories))

    category_colors = {}
    for i, category in enumerate(categories):
        category_colors[category] = colormap(i)

    x = [category[1] for category in category_map.values()]
    y = [category[0] for category in category_map.values()]

    for i, pais in enumerate(category_map.keys()):
        category = category_map[pais]
        plt.scatter(x[i], y[i], color=category_colors[category])
        plt.text(x[i], y[i], pais, fontsize=8, ha='center', va='center')

    plt.xlim(-1, max(x) + 1)
    plt.ylim(-1, max(y) + 1)

    plt.xlabel('Col')
    plt.ylabel('Row')
    legend_labels = [str(category) for category in categories]
    legend_handles = [plt.Line2D([], [], marker='o', markersize=8, color=category_colors[category], linestyle='')
                      for category in categories]
    plt.legend(legend_handles, legend_labels, loc='lower right')

    plt.show()
