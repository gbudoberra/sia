from generic_genetic import GenericGenetic
from random import random

from tp2.generic_selection_method import GenericSelectionMethod


class RouletteGenetic(GenericSelectionMethod):
    def __init__(self, size):
        super().__init__(size)

    def _select_parents(self, population):
        fitness_sum = sum([genotype.get_fitness() for genotype in population])
        fitness_relative = [(genotype, genotype.get_fitness() / fitness_sum) for genotype in population]
        fitness_relative_order = sorted(fitness_relative, key=lambda x: x[1])
        cumulative_fitness = [(None, 0)]
        current_index = 0
        while current_index < len(fitness_relative_order):
            cumulative_fitness.append((fitness_relative_order[current_index][0],
                                       cumulative_fitness[current_index][1] + fitness_relative_order[current_index][1]))
            current_index += 1
        new_generation = []
        current_new_generation_size = 0
        while current_new_generation_size < self.new_generation_size:
            random_number = random()
            i = 1
            prev = None
            q, suma = cumulative_fitness[i]
            while suma <= random_number:
                q, suma = cumulative_fitness[i]
                prev = cumulative_fitness[i - 1][0]
                i += 1
            new_generation.append(prev)
            current_new_generation_size += 1
            # for genotype, relative in cumulative_fitness:
            #     if random_number <= relative <= random_number:
            #         new_generation.append(genotype)
            # current_new_generation_size += 1
        return new_generation
