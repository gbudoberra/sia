import os
from PIL import Image, ImageDraw, ImageFont

def save_number_image(number, filename):
    # Selecciona la fuente y el tamaño de letra
    font_size = 36
    font = ImageFont.truetype('DejaVuSans.ttf', font_size)

    # Crea una nueva imagen de 100x100 píxeles
    image = Image.new('RGB', (100, 100), color='white')

    # Dibuja el número en la imagen
    draw = ImageDraw.Draw(image)
    text_bbox = draw.textbbox((0, 0), str(number), font=font)
    x = (image.width - text_bbox[2]) // 2
    y = (image.height - text_bbox[3]) // 2
    draw.text((x, y), str(number), font=font, fill='black')

    # Guarda la imagen como archivo PNG
    image.save(filename)

if __name__ == '__main__':
    # Genera imágenes para los números del 0 al 9
    for i in range(10):
        filename = f'{i}.png'
        save_number_image(i, filename)
        print(f'Imagen guardada en {os.path.abspath(filename)}')
