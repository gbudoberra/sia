from src.pokemon import PokemonFactory, StatusEffect
from src.functions import catch_with_pokeballs, get_avg_std_for_pokemon
import numpy as np
import matplotlib.pyplot as plt
import sys
import json

# Propiedades mutable:
#   Level --> Max hp
#
#   StatusEffect
#
#   HP %
#       Menor mejor
#   pokeball type
#       BasePokeball, Pokeball, HeavyBall, UltraBall, FastBall
# numerator = 1 + (max_hp * 3 - curr_hp * 2) * catch_rate * ball_rate * status

if __name__ == "__main__":
    input_file = "pokemon.json"
    factory = PokemonFactory(input_file)
    pokeball_list = ['pokeball', 'ultraball', 'fastball', 'heavyball']
    with open(input_file, "r") as c:
        pokemon_dictionary = dict(json.load(c))
    pokemon_names = pokemon_dictionary.keys()

    if len(sys.argv) <= 1 or sys.argv[1] not in pokemon_names:
        raise Exception("Provide a correct pokemon name as first parameter.")

    name = sys.argv[1]

    # Pokeballs ---------------------------------------------------------------
    pokeballs_average_and_std = catch_with_pokeballs(pokeball_list, [name], factory)

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
    ax1.bar(x + width * 2, y, width, yerr=yerr)

    # Establecer etiquetas en los ejes y títulos
    ax1.set_ylabel('Probabilidad de atrapar')
    ax1.set_title('Efectividad pokebolas: ' + name)
    ax1.set_xticks(np.arange(len(pokeball_list)) + width * 2)
    ax1.set_xticklabels(pokeball_list)
    fig1.savefig('graphs/2d_' + name + '_pokeballs.png')

    # Level
    level_attempts = []
    for i in range(100):
        level_attempts.append(get_avg_std_for_pokemon(factory.create(name, i, StatusEffect.NONE, 1), pokeball_list[0]))
    x = range(100)
    y = [level_attempts[i][0] for i in range(100)]
    yerr = [level_attempts[i][1] for i in range(100)]
    ax2.scatter(x, y)
    ax2.errorbar(x, y, yerr=yerr, linestyle='None')
    # Establecer etiquetas en los ejes y títulos
    ax2.set_ylabel('Probabilidad de atrapar')
    ax2.set_xlabel('Nivel')
    ax2.set_title('Impacto del nivel: ' + name)
    ax2.margins(x=0.02)
    fig2.savefig('graphs/2d_' + name + '_level.png')

    # % HP
    hp_attempts = {}
    for i in np.linspace(0, 1, 21):
        hp_attempts[i] = (get_avg_std_for_pokemon(factory.create(name, 100, StatusEffect.NONE, i), pokeball_list[0]))
    x = np.linspace(0, 1, 21)
    y = [hp_attempts[i][0] for i in np.linspace(0, 1, 21)]
    yerr = [hp_attempts[i][1] for i in np.linspace(0, 1, 21)]
    ax3.scatter(x, y)
    ax3.errorbar(x, y, yerr=yerr, linestyle='None')
    # Establecer etiquetas en los ejes y títulos
    ax3.set_ylabel('Probabilidad de atrapar')
    ax3.set_xlabel('HP %')
    ax3.set_title('Impacto del HP %: ' + name)
    fig3.savefig('graphs/2d_' + name + '_hp.png')

    # Status
    status_attempts = {}
    for status in StatusEffect:
        status_attempts[status] = (get_avg_std_for_pokemon(factory.create(name, 100, status, 1), pokeball_list[0]))
    x = np.arange(len(StatusEffect))
    y = [status_attempts[i][0] for i in StatusEffect]
    yerr = [status_attempts[i][1] for i in StatusEffect]
    ax4.bar(x + width * 2, y, width, yerr=yerr)
    # Establecer etiquetas en los ejes y títulos
    ax4.set_ylabel('Probabilidad de atrapar')
    ax4.set_xticks(np.arange(len(StatusEffect)) + width * 2)
    ax4.set_xticklabels([status.name for status in StatusEffect])
    ax4.set_title('Impacto del status: ' + name)
    fig4.savefig('graphs/2d_' + name + '_status.png')



