from src.pokemon import PokemonFactory
import json
import matplotlib.pyplot as plt
import numpy as np
from src.functions import catch_with_pokeballs

if __name__ == "__main__":
    input_file = "pokemon.json"
    factory = PokemonFactory(input_file)
    pokeball_list = ['pokeball', 'ultraball', 'fastball', 'heavyball']
    with open(input_file, "r") as c:
        pokemon_dictionary = dict(json.load(c))
    pokemon_names = pokemon_dictionary.keys()

    average_and_mean = catch_with_pokeballs(pokeball_list, pokemon_names, factory)


    # Crear subplots
    fig, ax = plt.subplots()

    # Establecer el ancho de la barra
    width = 0.15

    # Crear barras de cada pokemon para cada tipo de pokeball
    for i, p in enumerate(pokemon_names):
        x = np.arange(len(pokeball_list))
        y = [average_and_mean[pokeball][p][0] for pokeball in pokeball_list]
        yerr = [average_and_mean[pokeball][p][1] for pokeball in pokeball_list]
        ax.bar(x + i * width, y, width, yerr=yerr, label=p)

    # Establecer etiquetas en los ejes y títulos
    ax.set_ylabel('Probabilidad de atrapar')
    ax.set_title('Efectividad de las pokebolas')
    ax.set_xticks(np.arange(len(pokeball_list)) + width * 2)
    ax.set_xticklabels(pokeball_list)
    ax.legend()

    plt.show()
