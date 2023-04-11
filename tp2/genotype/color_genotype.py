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
        red = 0
        green = 0
        blue = 0
        for i in range(len(self.color_palette)):
            red += self.color_palette[i].red * self.color_proportion[i]
            green += self.color_palette[i].green * self.color_proportion[i]
            blue += self.color_palette[i].blue * self.color_proportion[i]

        p1 = np.array([red, green, blue])
        p2 = np.array([goal.red, goal.green, goal.blue])
        return -1 * np.linalg.norm(p1 - p2)

    def __str__(self) -> str:
        proportion_str = ""
        for proportion in self.color_proportion:
            proportion_str += str(proportion) + " , "
        return '(' + proportion_str + ')'
