from random import random

from tp2.genotype.color_genotype import ColorGenotype


def uniform_crossover(dad: ColorGenotype, mom: ColorGenotype):
    dad_proportion = dad.color_proportion
    mom_proportion = mom.color_proportion
    first_son_proportion = []
    second_son_proportion = []
    for i in range(len(dad_proportion)):
        random_num = random()
        first_son_proportion.append(dad_proportion[i] if random_num <= 0.5 else mom_proportion[i])
        second_son_proportion.append(mom_proportion[i] if random_num < 0.5 else dad_proportion[i])
    return ColorGenotype(dad.color_palette, first_son_proportion, dad.goal), ColorGenotype(dad.color_palette,
                                                                                           second_son_proportion,
                                                                                           dad.goal)
