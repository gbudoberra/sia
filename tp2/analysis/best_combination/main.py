import csv
import statistics
import threading

from tp2.configurations.jsonReader import JSONReader
from tp2.genetics.generic_genetic import GenericGenetic
from tp2.methods.deterministic_tournament_genetic import DeterministicTournamentGenetic
from tp2.methods.elite_genetic import EliteGenetic
from tp2.methods.probabilistic_tournament import ProbabilisticTournamentGenetic
from tp2.methods.roulette_genetic import RouletteGenetic
from tp2.mutation.mutation import mutation_limited_multigen, mutation_uniform_gen, complete_mutation

times = 2
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


def analyze_method(method):
    data = []
    for mutation_method in mutation_methods:

        results = []
        for i in range(times):
            genetic = GenericGenetic(
                config.initial_population,
                config.population_size,
                config.k_generated_sons,
                method['call'],
                method['call'],
                mutation_method['call'],
                config.mutation_probability,
                config.mutation_delta,
                config.solution_epsilon,
                config.goal_color
            )
            population = genetic.generate_new_population()
            results.append(max(population, key=lambda x: x.get_fitness()).get_fitness())

        average_fitness = sum(results) / len(results)

        data.append([method['name'], mutation_method['name'], genetic.counter, average_fitness,
                     statistics.stdev(results)])
    method['data'] = data


if __name__ == '__main__':
    config = JSONReader("./configurations/config.json", "./configurations/colors.json")

    headers = ["metodo_seleccion", "metodo_mutacion", "cantidad_iteraciones", "aptitud_max_promedio",
               "aptitud_max_desvio"]
    with open("archivo.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(headers)

    methods = [
        {
            'call': DeterministicTournamentGenetic(
                config.population_size, config.deterministic_tournament_participant_number, config.goal_color
            ).select,
            'name': 'deterministic_tournament',
            'data': None
        },
        {
            'call': EliteGenetic(
                config.population_size, config.goal_color
            ).select,
            'name': 'elite',
            'data': None
        },
        {
            'call': ProbabilisticTournamentGenetic(
                config.population_size, config.probabilistic_tournament_threshold, config.goal_color
            ).select,
            'name': 'probabilistic_tournament',
            'data': None
        },
        {
            'call': RouletteGenetic(
                config.population_size, config.goal_color
            ).select,
            'name': 'roulette',
            'data': None
        }
    ]

    threads = []
    for method in methods:
        thread = threading.Thread(target=analyze_method, args=[method, ])
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for method in methods:
        writer.writerow(method['data'])
