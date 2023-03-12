from .catching import attempt_catch
from .pokemon import StatusEffect
import statistics


def catch_with_pokeballs(pokeball_list, pokemon_names, factory):
    result_map = {}
    for j in range(100):
        for pokeball in pokeball_list:
            for pokemon_name in pokemon_names:
                attempt_catch_by_pokeball = []
                pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
                for i in range(1000):
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

    return average_and_mean


def get_avg_std_for_pokemon(pokemon, pokeball):
    attempts = []
    for i in range(1000):
        value = 1 if attempt_catch(pokemon, pokeball)[0] else 0
        attempts.append(value)
    return sum(attempts)/len(attempts), statistics.stdev(attempts)/(len(attempts)**0.5)
