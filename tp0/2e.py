from src.pokemon import PokemonFactory, StatusEffect
from src.functions import catch_with_pokeballs_level, get_avg_std_for_pokemon
import numpy as np
import matplotlib.pyplot as plt
import sys
import json


if __name__ == "__main__":
    input_file = "pokemon.json"
    factory = PokemonFactory(input_file)
    pokeball_list = ['pokeball', 'ultraball', 'fastball', 'heavyball']
    with open(input_file, "r") as c:
        pokemon_dictionary = dict(json.load(c))
    pokemon_names = pokemon_dictionary.keys()

    if len(sys.argv) <= 2:
        raise Exception("Provide pokemon name as first parameter and pokemon level as second parameter.")

    if sys.argv[1] not in pokemon_names:
        raise Exception("Provide a correct pokemon name as first parameter.")

    if not sys.argv[2].isnumeric() or not 100 >= int(sys.argv[2]) > 0:
        raise Exception("Provide a level between 1 and 100 as second parameter " + sys.argv[2])

    name = sys.argv[1]
    level = int(sys.argv[2])
    level_str = sys.argv[2]

    # Pokeballs ---------------------------------------------------------------
    pokeballs_average_and_std = catch_with_pokeballs_level(pokeball_list, [name], factory, level)

    # Crear subplots
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()

    # Establecer el ancho de la barra
    width = 0.15

    # Crear barras de cada pokemon para cada tipo de pokeball
    x = np.arange(len(pokeball_list))
    y = [pokeballs_average_and_std[pokeball][name][0] for pokeball in pokeball_list]
    yerr = [pokeballs_average_and_std[pokeball][name][1] for pokeball in pokeball_list]
    best_pokeball = pokeball_list[y.index(max(y))]
    ax1.bar(x + width * 2, y, width, yerr=yerr)

    # Establecer etiquetas en los ejes y títulos
    ax1.set_ylabel('Probabilidad de atrapar')
    ax1.set_title('Efectividad pokebolas: ' + name)
    ax1.set_xticks(np.arange(len(pokeball_list)) + width * 2)
    ax1.set_xticklabels(pokeball_list)
    fig1.savefig('graphs/2e_' + name + '_level' + level_str + '_pokeballs.png')

    # % HP
    hp_attempts = {}
    for i in np.linspace(0, 1, 21):
        hp_attempts[i] = (get_avg_std_for_pokemon(factory.create(name, level, StatusEffect.NONE, i), pokeball_list[0]))
    x = np.linspace(0, 1, 21)
    y = [hp_attempts[i][0] for i in np.linspace(0, 1, 21)]
    yerr = [hp_attempts[i][1] for i in np.linspace(0, 1, 21)]
    best_hp = x[y.index(max(y))]
    ax3.scatter(x, y)
    ax3.errorbar(x, y, yerr=yerr, linestyle='None')
    # Establecer etiquetas en los ejes y títulos
    ax3.set_ylabel('Probabilidad de atrapar')
    ax3.set_xlabel('HP %')
    ax3.set_title('Impacto del HP %: ' + name)
    fig3.savefig('graphs/2e_' + name + '_level' + level_str + '_hp.png')

    # Status
    status_attempts = {}
    for status in StatusEffect:
        status_attempts[status] = (get_avg_std_for_pokemon(factory.create(name, level, status, 1), pokeball_list[0]))
    x = np.arange(len(StatusEffect))
    y = [status_attempts[i][0] for i in StatusEffect]
    yerr = [status_attempts[i][1] for i in StatusEffect]
    best_status = [status.name for status in StatusEffect][y.index(max(y))]
    ax4.bar(x + width * 2, y, width, yerr=yerr)
    # Establecer etiquetas en los ejes y títulos
    ax4.set_ylabel('Probabilidad de atrapar')
    ax4.set_xticks(np.arange(len(StatusEffect)) + width * 2)
    ax4.set_xticklabels([status.name for status in StatusEffect])
    ax4.set_title('Impacto del status: ' + name)
    fig4.savefig('graphs/2e_' + name + '_level' + level_str + '_status.png')

    print(name + ', ' + level_str + ', ' + best_pokeball + ', ' + str(best_hp) + ', ' + best_status)