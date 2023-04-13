import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../archivo.csv')

selection_methods = df['metodo_seleccion'].unique()

colors = {
    'mutation_limited_multigen': 'tab:blue',
    'mutation_uniform_gen': 'tab:orange',
    'complete_mutation': 'tab:green',
}

for method in selection_methods:
    filtered_df = df[df['metodo_seleccion'] == method]
    ax = filtered_df.plot(kind='bar', x='metodo_mutacion', y='aptitud_max_promedio', yerr='aptitud_max_desvio',
                          capsize=4,  color=[colors[m] for m in filtered_df['metodo_mutacion']], figsize=(10, 6))
    ax.set_xlabel('Mutation Method', fontsize=14, fontweight='bold')
    ax.set_ylabel('Max Fitness score', fontsize=14, fontweight='bold')

    ax.set_title(f'Max Fitness Score by Selection Method ({method})')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.get_legend().remove()
    plt.show()