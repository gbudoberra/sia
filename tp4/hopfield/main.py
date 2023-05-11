from utils import initialize_points
from config import Config
from tp4.imageGenerator import generate_character_list
from hopfield import Hopfield
from tp4.hopfield.utils import map_zeros

if __name__ == '__main__':
    config = Config()
    generate_character_list(config.characters, config.noises)

    points = initialize_points(False, config.characters)
    points_with_error = initialize_points(True, config.characters)
    map_zeros(points)
    map_zeros(points_with_error)

    hopfield_net = Hopfield(points, 1000)

    for point, character in zip(points, config.characters):
        filename = f'./images/results/{character}_character'
        hopfield_net.get_pattern(point, filename)
    print("finished")

