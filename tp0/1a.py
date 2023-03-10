from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import json
import matplotlib.pyplot as plt

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
            for i in range(100):
                value = 1 if attempt_catch(pokemon, pokeball)[0] else 0
                attempt_catch_by_pokeball.append(value)
            if pokeball not in result_map:
                result_map[pokeball] = []
            result_map[pokeball].append((sum(attempt_catch_by_pokeball)/len(attempt_catch_by_pokeball)))

    result_avg_map = {}
    for pokeball in result_map.keys():
        result_avg_map[pokeball] = sum(result_map[pokeball])/len(result_map[pokeball])

    data = result_avg_map
    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.xticks(range(len(data)), list(data.keys()))
    plt.xlabel('Tipo de bola')
    plt.ylabel('Probabilidad de captura')
    plt.title('Probabilidades de captura por tipo de bola')
    plt.show()