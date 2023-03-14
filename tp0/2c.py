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

    deltas_status = []
    deltas_hp = []
    deltas_level = []

    for name in pokemon_names:

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
        deltas_level.append(delta_level)

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
        deltas_hp.append(delta_hp)

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
        deltas_status.append(delta_status)

    # Set the width of each bar and the gap between bars
    bar_width = 0.25
    bar_gap = 0.05

    # Create the x positions for each set of bars
    x_positions = np.arange(len(pokemon_names))

    # Plot the bars for each set of values
    plt.bar(x_positions - bar_width - bar_gap, deltas_hp, bar_width, label="Delta HP")
    plt.bar(x_positions, deltas_level, bar_width, label="Delta Level")
    plt.bar(x_positions + bar_width + bar_gap, deltas_status, bar_width, label="Delta Status")

    # Add labels and a legend
    plt.xlabel("Pokemons")
    plt.ylabel("Delta Values")
    plt.title("Comparison of the impact of each property")
    plt.xticks(x_positions, pokemon_names)
    plt.legend()

    # Display the plot
    plt.show()








