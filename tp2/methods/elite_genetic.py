import functools

from tp2.genotype.color_genotype import ColorGenotype
from tp2.methods.generic_selection_method import GenericSelectionMethod


def sort_by_fitness(genotype, goal: ColorGenotype):
    return genotype.get_fitness(goal)


def calculate_individual_times(size, index):
    # we are using constant population size, so the formula is 1 - i/n
    return round(1 - index / size)


class EliteGenetic(GenericSelectionMethod):

    def __init__(self, size, goal: ColorGenotype):
        super().__init__(size, goal)

    def select(self, population):
        genotype_and_fitness = []

        # Crea una nueva función con el argumento adicional definido
        sort_by_fitness_with_goal = functools.partial(sort_by_fitness, self.goal)

        for genotype in population:
            genotype_and_fitness.append(genotype)
        sorted_population = \
            sorted(genotype_and_fitness, key=sort_by_fitness_with_goal, reverse=True)[:self.new_generation_size]

        survivors = []
        for i in range(len(sorted_population)):
            n_times = calculate_individual_times(len(population), i)
            if n_times == 0:
                break
            for j in range(n_times):
                survivors.append(sorted_population[i])
        return survivors
