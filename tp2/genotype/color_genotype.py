import numpy as np


class ColorGenotype:
    def __init__(self, red, green, blue):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue

    def get_fitness(self, goal):
        p1 = np.array([self.red, self.green, self.blue])
        p2 = np.array([goal.red, goal.green, goal.blue])
        return -1 * np.linalg.norm(p1 - p2)

    def __str__(self) -> str:
        return '(' + str(self.red) + ', ' + str(self.green) + ', ' + str(self.blue) + ')'
