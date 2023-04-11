from abc import ABC, abstractmethod

from tp2.genotype.rgb_color_representation import RgbColor


class GenericSelectionMethod(ABC):

    def __init__(self, size, goal: RgbColor):
        self.new_generation_size = size
        self.goal = goal

    @abstractmethod
    def select(self, population):
        pass
