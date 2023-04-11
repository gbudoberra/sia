from tp2.configurations.jsonReader import JSONReader
from tp2.genetics.generic_genetic import GenericGenetic

if __name__ == '__main__':

    config = JSONReader("./configurations/model.json")

    genetic = GenericGenetic(
        config.initial_population,
        config.population_size,
        config.k_generated_sons,
        config.parent_selector,
        config.new_generation_selector,
        config.mutation_function,
        config.mutation_probability,
        config.mutation_delta,
        config.solution_epsilon,
        config.goal_color
    )

    population = genetic.generate_new_population()

    print('Best candidate:')
    print(max(population, key=lambda x: x.get_fitness()))

    print('Final population:')
    for genotype in population:
        print(genotype)
