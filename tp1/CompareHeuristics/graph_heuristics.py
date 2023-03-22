import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

h1 = 'heuristic_grid_remaining_colors'
h2 = 'heuristic_border_colors'
h3 = 'heuristic_cells_pending_per_color_remaining'
heuristics = [h1, h2, h3]


def graph_util(data, err, x_label, y_label, title):
    fig3, ax3 = plt.subplots()
    for i, heuristic in enumerate(heuristics):
        means = [data[j][heuristic] for j in range(len(dims))]
        errors = [err[j][heuristic] for j in range(len(dims))]
        x_pos = np.arange(len(dims)) + i * width - width
        ax3.bar(x_pos, means, width, yerr=errors, color=colors[i], label=labels[i])

    ax3.set_ylabel(y_label)
    ax3.set_xlabel(x_label)
    ax3.set_title(title)
    ax3.set_xticks(np.arange(len(dims)))
    ax3.set_xticklabels(dims)
    if y_label != 'Costo (pasos)':
        ax3.set_yscale("log")
    ax3.legend()
    plt.savefig(title)
    plt.clf()



if __name__ == '__main__':
    n_border = []
    n_nodes = []
    costs = []
    n_border_err = []
    n_nodes_err = []
    costs_err = []
    dims = [5, 6, 7, 8, 9, 10]
    for i in dims:

        dim = i

        df = pd.read_csv('heuristic_output_' + str(dim) + '.csv', delimiter=';')
        methods_data = df.groupby('method')

        n_border_err.append({})
        n_border.append({})
        n_nodes_err.append({})
        n_nodes.append({})
        costs_err.append({})
        costs.append({})

        for method, data in methods_data:
            cost_series = data['cost']
            costs[-1][method] = cost_series.mean()
            costs_err[-1][method] = cost_series.std()

            border_series = data['boundary_set_size']
            n_border[-1][method] = border_series.mean()
            n_border_err[-1][method] = border_series.std()

            nodes_series = data['exploded_nodes']
            n_nodes[-1][method] = nodes_series.mean()
            n_nodes_err[-1][method] = nodes_series.std()

    fig1, ax1 = plt.subplots()
    width = 0.2
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    labels = ['Grid Remaining Colors', 'Border Colors', 'Cells Pending Per Color Remaining']


    graph_util(costs, costs_err, 'Dimensión', 'Costo (pasos)', 'Costo vs Dimensión por cada heurística')
    graph_util(n_nodes, n_nodes_err, 'Dimensión', 'Nodos generados', 'Nodos generados vs Dimensión por cada heurística')
    graph_util(n_border, n_border_err, 'Dimensión', 'Nodos frontera finales', 'Nodos frontera vs Dimensión por cada heurística')
