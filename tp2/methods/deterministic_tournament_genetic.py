import random

from tp2.genotype.rgb_color_representation import RgbColor
from tp2.methods.generic_selection_method import GenericSelectionMethod


class DeterministicTournamentGenetic(GenericSelectionMethod):

    def __init__(self, size, participant_number, goal: RgbColor):
        super().__init__(size, goal)
        self.participant_number = participant_number

    def select(self, population):
        current_new_generation_size = 0
        new_generation = []

        while current_new_generation_size < self.new_generation_size:
            sample_size = self.participant_number  # totally arbitrary number
            tournament_participants = random.sample(population, sample_size)
            tournament_participants_fitness = [(genotype, genotype.get_fitness()) for genotype in
                                               tournament_participants]
            sorted(tournament_participants_fitness, key=lambda x: x[1])
            new_generation.append(tournament_participants_fitness[0][0])
            current_new_generation_size += 1
        return new_generation
