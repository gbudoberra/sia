import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../archivo1.csv')

# Define color palette for mutations
mutation_colors = {
    'mutation_limited_multigen': 'tab:blue',
    'mutation_uniform_gen': 'tab:orange',
    'complete_mutation': 'tab:green',
}

# Get unique selection methods
selection_methods = df['metodo_seleccion'].unique()

# Initialize figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

x_labels = []
for i, method in enumerate(selection_methods):
    filtered_df = df[df['metodo_seleccion'] == method]

    mutation_methods = filtered_df['metodo_mutacion'].unique()
    group_width = len(mutation_methods) * 0.8 / len(selection_methods)
    for j, mutation_method in enumerate(mutation_methods):
        x_labels.append(method)

# Set y-axis label
ax.set_ylabel('Avg Iteration number', fontsize=14, fontweight='bold')

# Plot bars for each mutation combination
for i, method in enumerate(selection_methods):
    filtered_df = df[df['metodo_seleccion'] == method]
    mutation_methods = filtered_df['metodo_mutacion'].unique()
    group_width = len(mutation_methods) * 0.3 / len(selection_methods)
    for j, mutation_method in enumerate(mutation_methods):
        mutation_df = filtered_df[filtered_df['metodo_mutacion'] == mutation_method]
        x = i + j * group_width + group_width/2
        y = mutation_df['cantidad_iteraciones_promedio']
        yerr = mutation_df['cantidad_iteraciones_desvio']
        color = mutation_colors[mutation_method]
        ax.bar(x, y, yerr=yerr, capsize=4, color=color, width=group_width)


# Set legend for mutation methods
mutation_patches = []
for mutation_method, color in mutation_colors.items():
    mutation_patches.append(plt.bar(0, 0, color=color, label=mutation_method))
ax.legend(handles=mutation_patches, loc='upper right', fontsize=12)

# Set x-axis ticks and labels
ax.set_xticks([i + 0.4 for i in range(len(selection_methods))])
ax.set_xticklabels(selection_methods, fontsize=12)

# Set title
ax.set_title('Avg Amount of Iterations by Selection Method and Mutation Combination', fontsize=16, fontweight='bold')
y_min, y_max = ax.get_ylim()
ax.set_ylim([0, y_max + 0.2 * (y_max - y_min)])

# Show plot
plt.show()
