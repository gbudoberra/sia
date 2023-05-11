import os

import numpy as np
from PIL import Image
from PIL import ImageDraw, ImageFont


def save_number_image(number, filename, noise):
    save_character_image(str(number), filename, noise)


def save_character_image(character, filename, noise):
    font_size = 36
    font = ImageFont.truetype('DejaVuSans.ttf', font_size)
    image = Image.new('RGB', (50, 50), color='white')
    draw = ImageDraw.Draw(image)
    text_bbox = draw.textbbox((0, 0), str(character), font=font)
    x = (image.width - text_bbox[2]) // 2
    y = (image.height - text_bbox[3]) // 2
    draw.text((x, y), str(character), font=font, fill='black')
    if noise > 0:
        add_noise_to_image(image, noise, filename)
    image.save(filename + ".png")


def add_noise_to_image(img, noise_level, filename):
    img_array = np.array(img)
    for i in range(1):
        random_matrix = np.random.rand(*img_array.shape)
        noise_matrix = np.where(random_matrix < 0.5, np.random.normal(0, noise_level, img_array.shape), 0)
        img_array_ruidosa = np.clip(img_array + noise_matrix, 0, 255)
        img_ruidosa = Image.fromarray(np.uint8(img_array_ruidosa))
        img_ruidosa.save(f"{filename}_with_error_{i}.png")


def generate_character_list(characters, noises):
    for noise in noises:
        for char in characters:
            filename = f'images/noise_{noise}/{char}_character'
            save_character_image(char, os.path.join(filename), noise)
            print(f'Generating: {os.path.abspath(filename)}')
