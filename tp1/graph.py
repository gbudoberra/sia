import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('output.csv', delimiter=';')
search_methods = ['A*', 'bfs', 'dfs', 'greedy']
method_groups = df.groupby(['method', 'dimension'])

# Loop over each dimension
for dim, dim_data in method_groups:
    # Create a figure and axis object for the plot
    fig, ax = plt.subplots()
    fig_cost, ax_cost = plt.subplots()
    for method in search_methods:
        try:
            method_data = method_groups.get_group((method, dim))
        except KeyError:
            # Method not available for this dimension
            continue

        times = method_data['time']
        cost = method_data['cost']

        mean_time = times.mean()
        std_time = times.std()

        mean_cost = cost.mean()
        std_cost = cost.std()

        ax.errorbar(method, mean_time, yerr=std_time, marker='o', label=method)
        ax_cost.errorbar(method, mean_cost, yerr=std_cost, marker='o', label=method)

    ax.set_xlabel('Search method')
    ax.set_ylabel('Time')
    ax.set_title(f'Comparison of search methods for dimension {dim}')
    ax.legend()

    ax_cost.set_xlabel('Search method')
    ax_cost.set_ylabel('Cost')
    ax_cost.set_title(f'Comparison of search methods for dimension {dim}')
    ax_cost.legend()

    fig.savefig(f"Graphs/time_{dim}.png")
    plt.close(fig)

    fig_cost.savefig(f"Graphs/cost_{dim}.png")
    plt.close(fig_cost)


