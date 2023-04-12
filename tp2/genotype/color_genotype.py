import math

import numpy as np


class ColorGenotype:
    def __init__(self, color_palette, color_proportion, goal):
        super().__init__()
        # palette colors' r,g,b 's value
        self.color_palette = color_palette
        # color proportion
        self.color_proportion = color_proportion
        self.goal = goal

    def get_fitness(self):
        goal = self.goal
        red, green, blue = self.get_total()
        p1 = np.array([red, green, blue])
        p2 = np.array([goal.red, goal.green, goal.blue])
        max_distance = math.sqrt(3*pow(255, 2))
        return max_distance - np.linalg.norm(p1 - p2)

    def __str__(self) -> str:
        proportion_str = ""
        for proportion in self.color_proportion:
            proportion_str += str(proportion) + " , "

        rgb_str = ""
        for component in self.get_total():
            rgb_str += str(component) + " , "

        return 'rgb: ' + rgb_str + 'proportions: ' + proportion_str

    def get_total(self):
        red = 0
        green = 0
        blue = 0
        for i in range(len(self.color_palette)):
            red += self.color_palette[i].red * self.color_proportion[i]
            green += self.color_palette[i].green * self.color_proportion[i]
            blue += self.color_palette[i].blue * self.color_proportion[i]
        return red, green, blue

