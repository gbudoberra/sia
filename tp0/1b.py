from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import json
import matplotlib.pyplot as plt
import numpy as np
import statistics

if __name__ == "__main__":
    input_file = "pokemon.json"
    factory = PokemonFactory(input_file)
    pokeball_list = ['pokeball', 'ultraball', 'fastball', 'heavyball']
    with open(input_file, "r") as c:
        pokemon_dictionary = dict(json.load(c))
    pokemon_names = pokemon_dictionary.keys()
    result_map = {}

    for j in range(100):
        for pokeball in pokeball_list:
            for pokemon_name in pokemon_names:
                attempt_catch_by_pokeball = []
                for i in range(100):
                    pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
                    value = 1 if attempt_catch(pokemon, pokeball)[0] else 0
                    attempt_catch_by_pokeball.append(value)
                if pokeball not in result_map:
                    result_map[pokeball] = {}
                if pokemon_name not in result_map[pokeball]:
                    result_map[pokeball][pokemon_name] = []
                result_map[pokeball][pokemon_name].append(
                    sum(attempt_catch_by_pokeball) / len(attempt_catch_by_pokeball))

    average_and_mean = {}
    for pokemon_name in pokemon_names:
        for pokeball in pokeball_list:
            current_list = result_map[pokeball][pokemon_name]
            if pokeball not in average_and_mean:
                average_and_mean[pokeball] = {}
            average_and_mean[pokeball][pokemon_name] = (statistics.mean(current_list), statistics.stdev(current_list))


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
