import functools

from tp2.genotype.color_genotype import ColorGenotype
from tp2.genotype.rgb_color_representation import RgbColor
from tp2.methods.generic_selection_method import GenericSelectionMethod


def sort_by_fitness(genotype):
    return genotype.get_fitness()


def calculate_individual_times(size, index):
    # we are using constant population size, so the formula is 1 - i/n
    return round(1 - index / size)


class EliteGenetic(GenericSelectionMethod):

    def __init__(self, size, goal: RgbColor):
        super().__init__(size, goal)

    def select(self, population):
        sorted_collection = sorted(population, key=sort_by_fitness, reverse=True)
        return sorted_collection[:self.new_generation_size]


