from src.pokemon import PokemonFactory, StatusEffect
from src.functions import catch_with_pokeballs, get_avg_std_for_pokemon
import numpy as np
import matplotlib.pyplot as plt
import json

if __name__ == "__main__":
    input_file = "pokemon.json"
    factory = PokemonFactory(input_file)
    pokeball_list = ['pokeball', 'ultraball', 'fastball', 'heavyball']
    with open(input_file, "r") as c:
        pokemon_dictionary = dict(json.load(c))
    pokemon_names = pokemon_dictionary.keys()

    # Crear subplots
    fig1, ax1 = plt.subplots()

    deltas = {}
    for name in pokemon_names:
        # Establecer el ancho de la barra
        width = 0.15

        # Level
        level_attempts = []
        for i in range(100):
            level_attempts.append(get_avg_std_for_pokemon(factory.create(name, i, StatusEffect.NONE, 1), pokeball_list[0]))
        x = range(100)
        y = [level_attempts[i][0] for i in range(100)]
        yerr = [level_attempts[i][1] for i in range(100)]
        max_level = max(level_attempts[i][0] for i in range(100))
        min_level = min(level_attempts[i][0] for i in range(100))
        delta_level = max_level - min_level
        print("Delta Level: " + str(delta_level))

        # % HP
        hp_attempts = {}
        for i in np.linspace(0, 1, 21):
            hp_attempts[i] = (get_avg_std_for_pokemon(factory.create(name, 100, StatusEffect.NONE, i), pokeball_list[0]))
        x = np.linspace(0, 1, 21)
        y = [hp_attempts[i][0] for i in np.linspace(0, 1, 21)]
        yerr = [hp_attempts[i][1] for i in np.linspace(0, 1, 21)]
        max_hp = max(hp_attempts[i][0] for i in np.linspace(0, 1, 21))
        min_hp = min(hp_attempts[i][0] for i in np.linspace(0, 1, 21))
        delta_hp = max_hp - min_hp
        print("Delta HP: " + str(delta_hp))

        # Status
        status_attempts = {}
        for status in StatusEffect:
            status_attempts[status] = (get_avg_std_for_pokemon(factory.create(name, 100, status, 1), pokeball_list[0]))
        x = np.arange(len(StatusEffect))
        y = [status_attempts[i][0] for i in StatusEffect]
        yerr = [status_attempts[i][1] for i in StatusEffect]
        max_status = max(status_attempts[i][0] for i in StatusEffect)
        min_status = min(status_attempts[i][0] for i in StatusEffect)
        delta_status = max_status - min_status
        print("Delta Status: " + str(delta_status))

        deltas[name] = (delta_hp, delta_level, delta_status)

    # todo
    # Graph with bars> Pokemon is the X axis.
    # Each pokemon has three bars with different colors.
    # Delta value is the Y Axis
    #









