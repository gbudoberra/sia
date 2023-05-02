import os

import numpy as np
from PIL import Image
from PIL import ImageDraw, ImageFont


def save_number_image(number, filename, noise):
    font_size = 36
    font = ImageFont.truetype('DejaVuSans.ttf', font_size)
    image = Image.new('RGB', (50, 50), color='white')
    draw = ImageDraw.Draw(image)
    text_bbox = draw.textbbox((0, 0), str(number), font=font)
    x = (image.width - text_bbox[2]) // 2
    y = (image.height - text_bbox[3]) // 2
    draw.text((x, y), str(number), font=font, fill='black')
    add_noise_to_image(image, noise, filename)
    image.save(filename + ".png")


def add_noise_to_image(img, noise_level, filename):
    img_array = np.array(img)
    for i in range(100):
        random_matrix = np.random.rand(*img_array.shape)
        noise_matrix = np.where(random_matrix < 0.5, np.random.normal(0, noise_level, img_array.shape), 0)
        img_array_ruidosa = np.clip(img_array + noise_matrix, 0, 255)
        img_ruidosa = Image.fromarray(np.uint8(img_array_ruidosa))
        img_ruidosa.save(f"{filename}_with_error_{i}.png")


if __name__ == '__main__':
    for noise in [70, 160, 255]:
        for i in range(10):
            filename = f'images/noise_{noise}/{i}_digit'
            save_number_image(i, os.path.join(filename), noise)
            print(f'Generating: {os.path.abspath(filename)}')
