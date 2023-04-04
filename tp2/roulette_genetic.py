from generic_genetic import GenericGenetic
from random import random


class RouletteGenetic(GenericGenetic):
    def _select_parents(self):
        pass

    def _crossover(self):
        pass

    def _mutate_population(self):
        pass

    def _generate_new_population(self):
        fitness_sum = sum([genotype.get_fitness() for genotype in self.population])
        fitness_relative = [(genotype, genotype.get_fitness() / fitness_sum) for genotype in self.population]
        fitness_relative_order = sorted(fitness_relative, key=lambda x: x[1])
        cumulative_fitness = [(None, 0)]
        current_index = 0
        while current_index < len(fitness_relative_order):
            cumulative_fitness.append((fitness_relative_order[current_index][0],
                                       cumulative_fitness[current_index] + fitness_relative_order[current_index][1]))
            current_index += 1
        new_generation = []
        current_new_generation_size = 0
        while current_new_generation_size < self.new_generation_size:
            random_number = random()
            for genotype, relative in cumulative_fitness:
                if random_number <= relative <= random_number:
                    new_generation.append(genotype)
            current_new_generation_size += 1
        return new_generation

    def acceptable_solution(self):
        pass
