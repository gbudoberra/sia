import csv
import statistics
import threading

from tp2.configurations.jsonReader import JSONReader
from tp2.genetics.generic_genetic import GenericGenetic

times = 10
headers = ["mutation_probability", "cantidad_iteraciones_promedio", "cantidad_iteraciones_desvio",
           "aptitud_max_promedio", "aptitud_max_desvio"]


def analyze(mutation_probability):
    data = []
    results = []
    generation = []
    genetic = None
    for i in range(times):
        genetic = GenericGenetic(
            [genotype for genotype in config.initial_population],
            config.population_size,
            config.k_generated_sons,
            config.parent_selector,
            config.new_generation_selector,
            config.mutation_function,
            mutation_probability,
            config.mutation_delta,
            config.solution_epsilon,
            config.goal_color
        )
        population = genetic.generate_new_population()
        results.append(max(population, key=lambda x: x.get_fitness()).get_fitness())
        generation.append(genetic.counter)
    data.append([mutation_probability, statistics.mean(generation),
                 statistics.stdev(generation), statistics.mean(results), statistics.stdev(results)])
    with open("alter_mutation_prob_" + str(mutation_probability) + ".csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(headers)
        for result in data:
            writer.writerow(result)
    return


if __name__ == '__main__':
    config = JSONReader("./configurations/config.json", "./configurations/colors.json")

    threads = []
    for value in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
        thread = threading.Thread(target=analyze, args=[value])
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
