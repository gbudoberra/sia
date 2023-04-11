import functools
from typing import Callable, List

from tp2.color_crossover.rgb_crossover import uniform_crossover
from tp2.genotype.color_genotype import ColorGenotype
from tp2.genotype.rgb_color_representation import RgbColor


class GenericGenetic:

    def __init__(self,
                 population, size, k_generated_sons,
                 parents_selector: Callable[[List[ColorGenotype]], List[ColorGenotype]],
                 new_generation_selector: Callable[[List[ColorGenotype]], List[ColorGenotype]],
                 mutation_function: Callable[[float, ColorGenotype, int], ColorGenotype],
                 mutation_probability: float,
                 mutation_delta: int,
                 solution_epsilon,
                 goal
                 ):

        # Population information
        self.population = population
        self.k_generated_sons = k_generated_sons  # k = generated_son in each iteration
        self.population_size = size  # N = population size
        self.goal = goal

        # Selector functions
        self.parents_selector = parents_selector
        self.new_generation_selector = new_generation_selector

        # Mutation information
        self.mutation_function = mutation_function
        self.mutation_probability = mutation_probability
        self.delta = mutation_delta
        self.counter = 0
        self.solution_epsilon = solution_epsilon

    def _mutate_sons(self, sons):
        mutated_sons = []
        for son in sons:
            mutated_sons.append(self.mutation_function(self.mutation_probability, son, self.delta))
        return mutated_sons

    def generate_new_population(self):
        while not self.acceptable_solution():
            # select generated_son parents to create generated_son sons
            parents = self.parents_selector(self.population)
            # create the sons
            sons = crossover(parents)
            # mutate the sons
            mutated_sons = self._mutate_sons(sons)
            # add to the new population the sons and the existent genotypes
            new_population = self.population.copy()
            new_population.extend(mutated_sons)
            # truncate the new_population
            self.population = self.new_generation_selector(new_population)
            self.counter = self.counter + 1
        return self.population

    def acceptable_solution(self):
        sorted_population = sorted(self.population, key=sort_by_fitness, reverse=True)
        best_genotype = sorted_population[0]
        print(best_genotype.get_fitness())
        return -1*best_genotype.get_fitness() < self.solution_epsilon


def sort_by_fitness(genotype):
    return genotype.get_fitness()


def crossover(selection):
    i = 0
    sons = []
    while i < len(selection) - 1:
        (first_son, second_son) = uniform_crossover(selection[i], selection[i + 1])
        i = i + 2
        sons.append(first_son)
        sons.append(second_son)
    return sons
