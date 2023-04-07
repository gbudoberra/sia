from generic_genetic import GenericGenetic
from random import randint

from tp2.generic_selection_method import GenericSelectionMethod


class DeterministicTournamentGenetic(GenericSelectionMethod):

    def __init__(self, size, participant_number):
        super().__init__(size)
        self.participant_number = participant_number

    def _select_parents(self, population):
        current_new_generation_size = 0
        new_generation = []
        while current_new_generation_size < self.new_generation_size:
            added_genotype = 0
            enrolled_genotypes = []
            tournament_participant = []
            while added_genotype < self.participant_number:
                index = randint(0, self.new_generation_size - 1)
                if index not in enrolled_genotypes:
                    tournament_participant.append(population[index])
                    added_genotype += 1
                    enrolled_genotypes.append(index)
            tournament_participant_fitness = [(genotype, genotype.get_fitness()) for genotype in tournament_participant]
            sorted(tournament_participant_fitness, key=lambda x: x[1])
            new_generation.append(tournament_participant_fitness[self.participant_number - 1])
            added_genotype += 1
        return new_generation

