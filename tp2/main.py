import matplotlib.pyplot as plt
from tp2.configurations.jsonReader import JSONReader
from tp2.genetics.generic_genetic import GenericGenetic

if __name__ == '__main__':

    config = JSONReader("./configurations/model.json", "./configurations/model_colors.json")

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
    goal_color_rgb = [config.goal_color.red / 255,  config.goal_color.green / 255,  config.goal_color.blue / 255]
    plt.bar(range(1), goal_color_rgb, color=goal_color_rgb)
    plt.show()

    population = genetic.generate_new_population()

    print('Best candidate:')
    best = max(population, key=lambda x: x.get_fitness())
    best_rgb = [prop/255 for prop in best.get_total()]
    print(str(best))

    # plt.bar(range(1), best_rgb, color=best_rgb)
    # plt.show()
    # plt.clf()
    rgb = [prop/255 for prop in best.get_total()]
    plt.bar(range(1), rgb, color=rgb)
    plt.show()

    print('Final population:')
    for genotype in population:
        print(genotype)
