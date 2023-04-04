from abc import ABC, abstractmethod


class Genotype(ABC):
    def __init__(self):
        self.status = None

    @abstractmethod
    def get_fitness(self):
        pass


