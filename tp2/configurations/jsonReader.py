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
    def __init__(self, json_config_path, json_colors_path):
        with open(json_config_path, "r") as f:
            config = json.load(f)

        with open(json_colors_path, "r") as f:
            colors = json.load(f)

        # Goal color
        goal_color_data = colors['goal_color']
        self.goal_color = RgbColor(
            goal_color_data['r'], goal_color_data['g'], goal_color_data['b']
        )

        # Populations information
        self.palette = [RgbColor(color['r'], color['g'], color['b']) for color in colors["color_palette"]]
        self.initial_population = \
            create_first_generation(self.palette, self.goal_color, config['population_size'])
        self.population_size = config["population_size"]
        self.k_generated_sons = config["k_generated_sons"]
        self.solution_epsilon = config["solution_epsilon"]

        self.deterministic_tournament_participant_number = config["deterministic_tournament_participant_number"]
        self.probabilistic_tournament_threshold = config["probabilistic_tournament_threshold"]

        # Parent selector
        self.parent_selector = get_selector(
            config["parent_selector"],
            self.deterministic_tournament_participant_number,
            self.probabilistic_tournament_threshold,
            self.k_generated_sons, self.goal_color
        )

        self.new_generation_selector = get_selector(
            config["new_generation_selector"],
            self.deterministic_tournament_participant_number,
            self.probabilistic_tournament_threshold,
            self.population_size, self.goal_color
        )


        self.mutation_function = get_mutation_function(config["mutation_function"])

        self.mutation_delta = config["mutation_delta"]  # deprecated
        self.mutation_probability = config["mutation_probability"]


def create_first_generation(palette, goal: RgbColor, population_size):
    population = []
    for i in range(population_size):
        random_proportion = [random.random() for i in range(len(palette))]
        random_proportion = [x / sum(random_proportion) for x in random_proportion]
        individual = ColorGenotype(
            palette,
            random_proportion,
            goal
        )
        population.append(individual)
    return population


def get_selector(selector, deterministic_tournament_participant_number, probabilistic_tournament_threshold, size, goal):
    if selector == 'DeterministicTournamentGenetic':
        return DeterministicTournamentGenetic(
            size, deterministic_tournament_participant_number, goal
        ).select
    if selector == 'EliteGenetic':
        return EliteGenetic(size, goal).select
    if selector == 'ProbabilisticTournamentGenetic':
        return ProbabilisticTournamentGenetic(size, probabilistic_tournament_threshold, goal).select
    if selector == 'RouletteGenetic':
        return RouletteGenetic(size, goal).select
    return None


def get_mutation_function(function):
    cases = {
        "mutation_limited_multigen": mutation_limited_multigen,
        "mutation_uniform_gen": mutation_uniform_gen,
        "complete_mutation": complete_mutation
    }
    return cases.get(function)
