from abc import ABC, abstractmethod

from tp2.genotype.color_genotype import ColorGenotype


class GenericSelectionMethod(ABC):

    def __init__(self, size, goal: ColorGenotype):
        self.new_generation_size = size
        self.goal = goal

    @abstractmethod
    def select(self, population):
        pass
