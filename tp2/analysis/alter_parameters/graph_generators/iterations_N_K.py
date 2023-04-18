import matplotlib.pyplot as plt
import pandas as pd

k_values = [0.1, 0.5, 1]
k_files = []


if __name__ == '__main__':
    # Leer los archivos CSV y almacenarlos en una lista
    for value in k_values:
        k_files.append(pd.read_csv('../alter_N_K_' + str(value) + '.csv'))

    # Crear la primera figura
    fig1, ax1 = plt.subplots()

    # Ciclar por los archivos y plotear las curvas en la primera figura con puntos
    for i, file in enumerate(k_files):
        ax1.errorbar(file['N'], file['aptitud_max_promedio'], yerr=file['aptitud_max_desvio'],
                     label='k=' + str(k_values[i]), marker='o')  # Agregar el marker 'o' para puntos

    # Configurar las etiquetas y el título de la primera figura
    ax1.set_xlabel('Tamaño de la población')
    ax1.set_ylabel('Aptitud máxima promedio')
    ax1.legend()

    # Establecer límite en el eje y de 0 al máximo valor
    ax1.set_ylim(300, 500)

    # Crear la segunda figura
    fig2, ax2 = plt.subplots()

    # Ciclar por los archivos y plotear las curvas en la segunda figura con puntos
    for i, file in enumerate(k_files):
        ax2.errorbar(file['N'], file['cantidad_iteraciones_promedio'], yerr=file['cantidad_iteraciones_desvio'],
                     label='k=' + str(k_values[i]), marker='o')  # Agregar el marker 'o' para puntos

    # Configurar las etiquetas y el título de la segunda figura
    ax2.set_xlabel('Tamaño de la población')
    ax2.set_ylabel('Iteraciones promedio')
    ax2.legend()

    # Establecer límite en el eje y de 0 al máximo valor
    ax2.set_ylim(-10, 100)

    # Mostrar las figuras
    plt.show()
