import PIL
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math


def add_meta(path_to_image, image_path_orig='', date_submission='', date_photo_made=''):
    image = Image.open(path_to_image)

    im_x, im_y = image.size

    if im_y > im_x:
        image.rotate(90, PIL.Image.NEAREST, expand=1)
        image.save(path_to_image)
        im_x, im_y = im_y, im_x

    image_bottom = PIL.Image.new("RGB", (im_x, 500), (0, 0, 0))

    I1 = ImageDraw.Draw(image_bottom)
    myFont = ImageFont.truetype('Arial.ttf', 100)

    infodata = []

    if image_path_orig:
        infodata.append((f"ПУТЬ К ИЗОБРАЖЕНИЮ:", image_path_orig))

    if date_photo_made:
        infodata.append((f"ДАТА АЭРОФОТОСЪЕМКИ:", date_photo_made))

    if date_submission:
        infodata.append((f"ДАТА ОБРАБОТКИ:", date_submission))

    padding = 100 // (len(infodata) - 1) if (len(infodata)) > 1 else 100/2

    for i in range(len(infodata)):
        I1.text((padding, i * 100 + padding * (i + 1)), infodata[i][0], font=myFont, fill=(255, 255, 255))
        I1.text((im_x //2 - padding, i * 100 + padding * (i + 1)), infodata[i][1], font=myFont, fill=(255, 255, 255))

    #image_bottom.show()

    dst = Image.new('RGB', (im_x, im_y + 500))
    dst.paste(image, (0, 0))
    dst.paste(image_bottom, (0, im_y))

    dst.save(f"meta{path_to_image}.jpg")
