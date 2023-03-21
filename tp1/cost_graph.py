import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('output.csv', delimiter=';')
search_methods = ['A*','bfs','dfs', 'greedy']
method_groups = df.groupby(['method', 'dimension'])
colors = ['r', 'g', 'b', 'y', 'm', 'c']
data = {}
data_errors = {}

for dim, dim_data in method_groups:
    for method in search_methods:
        if dim[0] == method:
            if data.get(dim[1]) is None:
                data[dim[1]] = {}
            data[dim[1]][method] = dim_data['cost'].mean()
            if data_errors.get(dim[1]) is None:
                data_errors[dim[1]] = {}
            data_errors[dim[1]][method] = dim_data['cost'].std()

# loop over the keys in the data dictionary
for dim in data.keys():
    methods = list(data[dim].keys())
    values = list(data[dim].values())
    errors = list(data_errors[dim].values())

    # create a bar chart showing the values and errors for all the search methods in the current dimension
    fig, ax = plt.subplots()
    ax.bar(methods, values, yerr=errors, capsize=5, color=colors[:len(methods)])
    ax.set_xlabel('Search Method')
    ax.set_ylabel('Mean Cost')
    ax.set_title(f'{dim} - Mean Time and Standard Deviation for Search Methods')
    fig.savefig(f"Graphs/cost_{dim}.png")
    plt.close(fig)
