import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('output.csv', delimiter=';')
search_methods = ['A*','dfs', 'greedy']
method_groups = df.groupby(['method', 'dimension'])
colors = ['r', 'g', 'b', 'y', 'm', 'c']
data = {}

for dim, dim_data in method_groups:
    for method in search_methods:
        if dim[0] == method:
            if data.get(dim[1]) is None:
                data[dim[1]] = {}
            data[dim[1]][method] = dim_data['cost'].mean()

# Define the colors for the methods
colors = ['r', 'g', 'b', 'm']

# Convert the data into arrays
x = np.arange(start=5, stop=12)  # X values
width = 0.2  # Width of each bar

# Plot the bars
fig, ax = plt.subplots()
for i, (dim, values) in enumerate(data.items()):
    for j, (method, time) in enumerate(values.items()):
        ax.bar(x[i] + j * width, time, width, alpha=0.7, color=colors[j])

# Add labels, legend, etc.
ax.set_xticks(x)
ax.set_title('Methods cost vs Dimension')
ax.set_xticklabels(x)
ax.set_ylabel('Cost')
ax.legend(search_methods)

plt.show()
