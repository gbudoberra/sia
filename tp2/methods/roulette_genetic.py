from random import random

from tp2.genotype.rgb_color_representation import RgbColor
from tp2.methods.generic_selection_method import GenericSelectionMethod


class RouletteGenetic(GenericSelectionMethod):
    def __init__(self, size, goal: RgbColor):
        super().__init__(size, goal)

    def select(self, population):
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
            for i in range(1, len(cumulative_fitness)):
                genotype, genotype_cumulative_fitness = cumulative_fitness[i]
                if random_number <= genotype_cumulative_fitness:
                    new_generation.append(genotype)
                    current_new_generation_size += 1
                    break
        return new_generation
