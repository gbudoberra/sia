from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import json
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    input_file = "pokemon.json"
    factory = PokemonFactory(input_file)
    pokeball_list = ['pokeball', 'ultraball', 'fastball', 'heavyball']
    with open(input_file, "r") as c:
        pokemon_dictionary = dict(json.load(c))
    pokemon_names = pokemon_dictionary.keys()
    result_map = {}

    for pokeball in pokeball_list:
        attempt_catch_by_pokeball = []
        for pokemon_name in pokemon_names:
            pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
            for i in range(1000):
                value = 1 if attempt_catch(pokemon, pokeball)[0] else 0
                attempt_catch_by_pokeball.append(value)
            if pokeball not in result_map:
                result_map[pokeball] = []
            result_map[pokeball].append((pokemon_name,sum(attempt_catch_by_pokeball)/len(attempt_catch_by_pokeball)))

    print(result_map)

    data = result_map
    # Convert data to arrays
    balls = list(data.keys())
    pokemon = [i[0] for i in data[balls[0]]]
    values = np.array([[i[1] for i in data[b]] for b in balls])

    # Plot
    fig, ax = plt.subplots()
    ax.bar(pokemon, values[0], label=balls[0])
    for i in range(1, len(balls)):
        ax.bar(pokemon, values[i], bottom=np.sum(values[:i], axis=0), label=balls[i])
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()

