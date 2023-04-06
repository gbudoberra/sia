from generic_genetic import GenericGenetic
from random import randint
import random


class ProbabilisticTournamentGenetic(GenericGenetic):
    def __init__(self, population, size, participant_number, threshold):
        super().__init__(population, size)
        self.participant_number = participant_number
        self.threshold = threshold

    def _crossover(self):
        pass

    def _mutate_population(self):
        pass

    def _select_parents(self):
        current_new_generation_size = 0
        new_generation = []
        for i in range(self.new_generation_size):
            # agarra 2 elementos de la poblacion al azar
            ind1, ind2 = random.sample(self.population, k=2)
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

    def _generate_new_population(self):
        pass

    def acceptable_solution(self):
        pass
