import random

from tp2.genotype.rgb_color_representation import RgbColor
from tp2.methods.generic_selection_method import GenericSelectionMethod


class ProbabilisticTournamentGenetic(GenericSelectionMethod):
    def __init__(self, size, threshold, goal: RgbColor):
        super().__init__(size, goal)
        self.threshold = threshold

    def select(self, population):

        new_generation = []
        for i in range(self.new_generation_size):

            # agarra 2 elementos de la poblacion al azar
            ind1, ind2 = random.sample(population, k=2)
            r = random.random()

            # si r < threshold, agrega el mejor de los 2
            if ind1.get_fitness() > ind2.get_fitness():
                if r < self.threshold:
                    new_generation.append(ind1)
                else:
                    new_generation.append(ind2)
            else:
                if r < self.threshold:
                    new_generation.append(ind2)
                else:
                    new_generation.append(ind1)

        return new_generation
