from abc import ABC, abstractmethod

from tp2.color_crossover.rgb_crossover import uniform_crossover


class GenericGenetic(ABC):

    def __init__(self, population, size, generated_son, mutation_probability, delta,
                 parent_selection, new_generation_selection):
        self.population = population
        self.generated_son = generated_son  # k = generated_son in each iteration
        self.population_size = size  # N = population size
        self.mutation_probability = mutation_probability
        self.delta = delta
        self.parents_selection = parent_selection
        self.new_generation_selection = new_generation_selection

    def _mutate_sons(self, sons):
        mutated_sons = []
        for son in sons:
            mutated_sons.append(self._mutate_each_son(son))
        return mutated_sons

    def _generate_new_population(self):
        while not self.acceptable_solution():
            # select generated_son parents to create generated_son sons
            parents = self.select_parents_from_population(self.generated_son)
            # create the sons
            sons = crossover(parents)
            # mutate the sons
            mutated_sons = self._mutate_sons(sons)
            # add to the new population the sons and the existent genotypes
            new_population = self.population.copy()
            new_population.extend(mutated_sons)
            # truncate the new_population
            self.population = self.select_to_create_new_population(new_population)

    def acceptable_solution(self):
        return len(self.population) == self.population_size  #temp

    def select_parents_from_population(self, population):
        return self.parents_selection.select(self.population)

    def select_to_create_new_population(self, population):
        return self.new_generation_selection.select(self.population)

    @abstractmethod
    def _mutate_each_son(self, son):
        pass


def crossover(selection):
    i = 0
    sons = []
    while i < len(selection) - 1:
        (first_son, second_son) = uniform_crossover(selection[i], selection[i + 1])
        i = i + 2
        sons.append(first_son)
        sons.append(second_son)
    return sons
