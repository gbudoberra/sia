import matplotlib.pyplot as plt
import pandas as pd

mutation_probability_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
files = []


if __name__ == '__main__':
    # Leer los archivos CSV y almacenarlos en una lista
    for value in mutation_probability_values:
        files.append(pd.read_csv('../alter_mutation_prob_' + str(value) + '.csv'))

    # Crear la primera figura
    fig1, ax1 = plt.subplots()

    # Ciclar por los archivos y plotear las curvas en la primera figura con puntos
    for i, file in enumerate(files):
        ax1.errorbar(file['mutation_probability'], file['aptitud_max_promedio'],
                     yerr=file['aptitud_max_desvio'], marker='o')

    # Configurar las etiquetas y el título de la primera figura
    ax1.set_xlabel('Probabilidad de mutación')
    ax1.set_ylabel('Aptitud máxima promedio')

    # Establecer límite en el eje y de 0 al máximo valor
    ax1.set_ylim(0, 500)

    # Crear la segunda figura
    fig2, ax2 = plt.subplots()

    # Ciclar por los archivos y plotear las curvas en la segunda figura con puntos
    for i, file in enumerate(files):
        ax2.errorbar(file['mutation_probability'], file['cantidad_iteraciones_promedio'],
                     yerr=file['cantidad_iteraciones_desvio'], marker='o')  # Agregar el marker 'o' para puntos

    # Configurar las etiquetas y el título de la segunda figura
    ax2.set_xlabel('Probabilidad de mutación')
    ax2.set_ylabel('Iteraciones promedio')

    # Establecer límite en el eje y de 0 al máximo valor
    ax2.set_ylim(-10, 2000)

    # Mostrar las figuras
    plt.show()
