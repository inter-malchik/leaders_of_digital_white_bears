from PIL import Image
import os

def convert_to_jpeg(old_path: str):
    image = Image.open(old_path)

    rgb_image = image.convert("RGB")

    new_path = old_path[:-3] + "jpg"

    rgb_image.save(new_path)

    os.remove(old_path)

    return new_path