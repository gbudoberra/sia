from abc import ABC, abstractmethod


class GenericGenetic(ABC):

    def __init__(self, population, size):
        self.population = population
        self.new_generation_size = size

    @abstractmethod
    def _select_parents(self):
        pass

    @abstractmethod
    def _crossover(self):
        pass

    @abstractmethod
    def _mutate_population(self):
        pass

    @abstractmethod
    def _generate_new_population(self):
        pass

    @abstractmethod
    def acceptable_solution(self):
        pass
