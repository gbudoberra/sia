import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('output.csv', delimiter=';')
search_methods = ['A*','dfs', 'greedy']
method_groups = df.groupby(['method', 'dimension'])
colors = ['r', 'g', 'b', 'y', 'm', 'c']
data = {}
data_errors = {}

for dim, dim_data in method_groups:
    for method in search_methods:
        if dim[0] == method:
            if data.get(dim[1]) is None:
                data[dim[1]] = {}
            data[dim[1]][method] = dim_data['time'].mean()
            if data_errors.get(dim[1]) is None:
                data_errors[dim[1]] = {}
            data_errors[dim[1]][method] = dim_data['time'].std()


#Define the colors for the methods
colors = ['r', 'g', 'b', 'm']

# Convert the data into arrays
x = np.arange(start=5, stop=12)  # X values
width = 0.2  # Width of each bar

# Plot the bars
fig, ax = plt.subplots()
for i, (dim, values) in enumerate(data.items()):
    for j, (method, time) in enumerate(values.items()):
        ax.bar(x[i] + j * width, time, width, yerr=data_errors[dim][method], alpha=0.7, color=colors[j])

# Add labels, legend, etc.
ax.set_xticks(x)
ax.set_yscale("log")
ax.set_title('Methods mean time vs Dimension')
ax.set_xticklabels(x)
ax.set_ylabel('Mean time(s)')
ax.legend(search_methods)

plt.show()
# loop over the keys in the data dictionary
# for dim in data.keys():
#     methods = list(data[dim].keys())
#     values = list(data[dim].values())
#     errors = list(data_errors[dim].values())
#
#     # create a bar chart showing the values and errors for all the search methods in the current dimension
#     fig, ax = plt.subplots()
#     ax.bar(methods, values, yerr=errors, capsize=5, color=colors[:len(methods)])
#     ax.set_xlabel('Search Method')
#     ax.set_ylabel('Mean Time(s)')
#     ax.set_title(f'{dim} - Mean Time and Standard Deviation for Search Methods')
#     fig.savefig(f"Graphs/time_{dim}.png")
#     plt.close(fig)







