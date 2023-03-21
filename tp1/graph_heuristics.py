import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

h1 = 'heuristic_grid_remaining_colors'
h2 = 'heuristic_border_colors'
h3 = 'heuristic_cells_pending_per_color_remaining'
heuristics = [h1, h2, h3]


def graph_util(data, x_label, y_label, title):
    fig3, ax3 = plt.subplots()
    for i, heuristic in enumerate(heuristics):
        means = [data[j][heuristic] for j in range(len(dims))]
        x_pos = np.arange(len(dims)) + i * width - width
        ax3.bar(x_pos, means, width, color=colors[i], label=labels[i])

    ax3.set_ylabel(y_label)
    ax3.set_xlabel(x_label)
    ax3.set_title(title)
    ax3.set_xticks(np.arange(len(dims)))
    ax3.set_xticklabels(dims)
    ax3.legend()
    plt.show()



if __name__ == '__main__':
    times = []
    times_err = []
    n_border = []
    n_nodes = []
    costs = []
    dims = [5, 6, 7, 8, 9, 10]
    for i in dims:

        dim = i

        df = pd.read_csv('heuristic_output_' + str(dim) + '.csv', delimiter=';')
        methods_data = df.groupby('method')

        times.append({})
        times_err.append({})
        n_border.append({})
        n_nodes.append({})
        costs.append({})

        for method, data in methods_data:
            time_series = data['time']
            times[-1][method] = time_series.mean()
            times_err[-1][method] = time_series.std()

            cost_series = data['cost']
            costs[-1][method] = cost_series.iloc[0]

            border_series = data['boundary_set_size']
            n_border[-1][method] = border_series.iloc[0]

            nodes_series = data['exploded_nodes']
            n_nodes[-1][method] = nodes_series.iloc[0]

    fig1, ax1 = plt.subplots()
    width = 0.2
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    labels = ['Grid Remaining Colors', 'Border Colors', 'Cells Pending Per Color Remaining']

    for i, heuristic in enumerate(heuristics):
        means = [times[j][heuristic] for j in range(len(dims))]
        errors = [times_err[j][heuristic] for j in range(len(dims))]
        x_pos = np.arange(len(dims)) + i * width - width
        ax1.bar(x_pos, means, width, yerr=errors, color=colors[i], label=labels[i])

    ax1.set_ylabel('Tiempo (s)')
    ax1.set_xlabel('Dimensión de la matriz')
    ax1.set_title('Tiempo vs Dimension por heurística')
    ax1.set_xticks(np.arange(len(dims)))
    ax1.set_xticklabels(dims)
    ax1.legend()
    plt.show()
    plt.clf()

    graph_util(costs, 'Dimensión', 'Costo (pasos)', 'Costo vs Dimensión por cada heurística')
    graph_util(n_nodes, 'Dimensión', 'Nodos generados', 'Nodos generados vs Dimensión por cada heurística')
    graph_util(n_border, 'Dimensión', 'Nodos frontera finales', 'Nodos frontera vs Dimensión por cada heurística')
