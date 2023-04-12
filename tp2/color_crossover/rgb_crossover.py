from random import random

from tp2.genotype.color_genotype import ColorGenotype
from tp2.mutation.mutation import normalize_proportions


def uniform_crossover(dad: ColorGenotype, mom: ColorGenotype):
    dad_proportion = dad.color_proportion.copy()
    mom_proportion = mom.color_proportion.copy()
    first_son_proportion = []
    second_son_proportion = []
    for i in range(len(dad_proportion)):
        random_num = random()
        first_son_proportion.append(dad_proportion[i] if random_num <= 0.5 else mom_proportion[i])
        second_son_proportion.append(mom_proportion[i] if random_num <= 0.5 else dad_proportion[i])
    first_son = ColorGenotype(dad.color_palette, first_son_proportion, dad.goal)
    second_son = ColorGenotype(dad.color_palette, second_son_proportion, dad.goal)
    return normalize_proportions(first_son), normalize_proportions(second_son)
