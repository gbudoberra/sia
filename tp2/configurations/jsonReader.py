import json
import random

from tp2.genotype.color_genotype import ColorGenotype
from tp2.methods.deterministic_tournament_genetic import DeterministicTournamentGenetic
from tp2.methods.elite_genetic import EliteGenetic
from tp2.methods.probabilistic_tournament import ProbabilisticTournamentGenetic
from tp2.methods.roulette_genetic import RouletteGenetic
from tp2.mutation.mutation import mutation_limited_multigen, mutation_uniform_gen, complete_mutation
from tp2.genotype.rgb_color_representation import RgbColor


class JSONReader:
    def __init__(self, json_file_path):
        with open(json_file_path, "r") as f:
            properties_dict = json.load(f)

        # Populations information
        self.palette = [RgbColor(color['r'], color['g'], color['b']) for color in properties_dict["color_palette"]]
        self.initial_population = create_first_generation(self.palette, properties_dict)
        self.population_size = properties_dict["population_size"]
        self.k_generated_sons = properties_dict["k_generated_sons"]
        self.solution_epsilon = properties_dict["solution_epsilon"]

        # Goal color
        goal_color_data = properties_dict['goal_color']
        self.goal_color = RgbColor(
            goal_color_data['r'], goal_color_data['g'], goal_color_data['b']
        )

        # Parent selector
        self.parent_selector = get_selector(
            properties_dict["parent_selector"], properties_dict, self.k_generated_sons * 2, self.goal_color
        )

        self.new_generation_selector = get_selector(
            properties_dict["new_generation_selector"], properties_dict, self.population_size, self.goal_color
        )

        self.mutation_function = get_mutation_function(properties_dict["mutation_function"])

        self.mutation_delta = properties_dict["mutation_delta"]
        self.mutation_probability = properties_dict["mutation_probability"]


def create_first_generation(palette, properties_dict):
    population = []
    goal_color = properties_dict['goal_color']
    goal_color = RgbColor(goal_color["r"], goal_color["g"], goal_color["b"])
    for i in range(properties_dict['population_size']):
        random_proportion = [random.random() for i in range(len(palette))]
        random_proportion = [x / sum(random_proportion) for x in random_proportion]
        individual = ColorGenotype(
            palette,
            random_proportion,
            goal_color
        )
        population.append(individual)
    return population


def get_selector(selector, properties_dict, size, goal):
    if selector == 'DeterministicTournamentGenetic':
        return DeterministicTournamentGenetic(
            size, properties_dict["deterministic_tournament_participant_number"], goal
        ).select
    if selector == 'EliteGenetic':
        return EliteGenetic(size, goal).select
    if selector == 'ProbabilisticTournamentGenetic':
        return ProbabilisticTournamentGenetic(size, properties_dict["probabilistic_tournament_threshold"], goal).select
    if selector == 'RouletteGenetic':
        return RouletteGenetic(size, goal).select


def get_mutation_function(function):
    cases = {
        "mutation_limited_multigen": mutation_limited_multigen,
        "mutation_uniform_gen": mutation_uniform_gen,
        "complete_mutation": complete_mutation
    }
    return cases[function]
