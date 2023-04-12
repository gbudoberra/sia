import csv
import statistics
import threading

from tp2.configurations.jsonReader import JSONReader
from tp2.genetics.generic_genetic import GenericGenetic
from tp2.methods.deterministic_tournament_genetic import DeterministicTournamentGenetic
from tp2.methods.elite_genetic import EliteGenetic
from tp2.methods.roulette_genetic import RouletteGenetic
from tp2.methods.probabilistic_tournament import ProbabilisticTournamentGenetic
from tp2.mutation.mutation import mutation_limited_multigen, mutation_uniform_gen, complete_mutation

times = 10
mutation_methods = [
    {
        'call': mutation_limited_multigen,
        'name': 'mutation_limited_multigen'
    },
    {
        'call': mutation_uniform_gen,
        'name': 'mutation_uniform_gen'
    },
    {
        'call': complete_mutation,
        'name': 'complete_mutation'
    }
]


def analyze_method(inner_analyze_method):
    data = []
    for mutation_method in mutation_methods:
        results = []
        generation = []
        genetic = None
        for i in range(times):
            genetic = GenericGenetic(
                [genotype for genotype in config.initial_population],
                config.population_size,
                config.k_generated_sons,
                inner_analyze_method['parent_selector'],
                inner_analyze_method['new_generation_selector'],
                mutation_method['call'],
                config.mutation_probability,
                config.mutation_delta,
                config.solution_epsilon,
                config.goal_color
            )
            population = genetic.generate_new_population()
            results.append(max(population, key=lambda x: x.get_fitness()).get_fitness())
            generation.append(genetic.counter)
        data.append([inner_analyze_method['name'], mutation_method['name'], statistics.mean(generation),
                     statistics.stdev(generation), statistics.mean(results), statistics.stdev(results)])
    inner_analyze_method['data'] = data


if __name__ == '__main__':
    config = JSONReader("./configurations/config.json", "./configurations/colors.json")

    methods = [
        {
            'parent_selector': DeterministicTournamentGenetic(
                config.k_generated_sons, config.deterministic_tournament_participant_number, config.goal_color
            ).select,
            'new_generation_selector': DeterministicTournamentGenetic(
                config.population_size, config.deterministic_tournament_participant_number, config.goal_color
            ).select,
            'name': 'deterministic_tournament',
            'data': []
        },
        {
            'parent_selector': EliteGenetic(
                config.k_generated_sons, config.goal_color
            ).select,
            'new_generation_selector': EliteGenetic(
                config.population_size, config.goal_color
            ).select,
            'name': 'elite',
            'data': []
        },
        {
            'parent_selector': ProbabilisticTournamentGenetic(
                config.k_generated_sons, config.probabilistic_tournament_threshold, config.goal_color
            ).select,
            'new_generation_selector': ProbabilisticTournamentGenetic(
                config.population_size, config.probabilistic_tournament_threshold, config.goal_color
            ).select,
            'name': 'probabilistic_tournament',
            'data': []
        },
        {
            'parent_selector': RouletteGenetic(
                config.k_generated_sons, config.goal_color
            ).select,
            'new_generation_selector': RouletteGenetic(
                config.population_size, config.goal_color
            ).select,
            'name': 'roulette',
            'data': []
        }
    ]
    headers = ["metodo_seleccion", "metodo_mutacion", "cantidad_iteraciones_promedio", "cantidad_iteraciones_desvio",
               "aptitud_max_promedio","aptitud_max_desvio"]

    threads = []
    for method in methods:
        thread = threading.Thread(target=analyze_method, args=[method])
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    with open("archivo.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(headers)
        for method in methods:
            for method_result in method["data"]:
                writer.writerow(method_result)
