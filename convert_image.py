from PIL import Image

def convert_to_jpeg(old_path: str):
    image = Image.open(old_path)

    rgb_image = image.convert("RGB")

    new_path = old_path[:-3] + "jpg"

    rgb_image.save(new_path)

    return new_path

