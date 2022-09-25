import dataclasses

import PIL
from PIL import Image, ImageOps
from PIL import ImageDraw
from PIL import ImageFont
import math
import datetime as dt

from dataclasses import dataclass


@dataclass
class BoxCoords:
    centre: tuple
    min_x: int
    min_y: int
    max_x: int
    max_y: int

    @staticmethod
    def parse_from_string(s):
        data = tuple(map(int, s.split(', ')))
        return BoxCoords((data[0], data[1]), *data[2:6])


@dataclass
class PhotoData:
    markup_path: str
    image_path: str
    image_dir: str
    date_of_creation: dt.datetime
    date_of_analysis: dt.datetime = dt.datetime.now()
    bear_boxes: list = dataclasses.field(default_factory=list)

    def scan_bear_boxes(self, path_to_paramentic_file: str):
        f = open(path_to_paramentic_file, 'r')
        for line in f:
            if line and line != "\n":
                self.bear_boxes.append(BoxCoords.parse_from_string(line))
        f.close()


def get_zoom_rect(bear_boxes: list):
    _min_x = _min_y = math.inf
    _max_x = _max_y = -math.inf

    for coord_box in bear_boxes:
        _min_y = min(_min_y, coord_box.min_y)
        _min_x = min(_min_x, coord_box.min_x)
        _max_y = min(_max_y, coord_box.max_y)
        _max_x = min(_max_x, coord_box.max_x)

    return BoxCoords(((_min_x + _max_x) // 2, (_min_y + _max_y) // 2), _min_x, _max_x, _min_y, _max_y)


def add_meta(image, image_path_orig='', date_submission='', date_photo_made=''):
    im_x, im_y = image.size

    if all([x for x in {image_path_orig, date_submission, date_photo_made}]):
        bottom_cum_size = math.ceil(im_y * 0.23)
    elif any([x for x in {image_path_orig, date_submission, date_photo_made}]):
        bottom_cum_size = math.ceil(im_y * 0.20)
    else:
        bottom_cum_size = math.ceil(im_y * 0.18)

    font_size = math.ceil(im_x * 0.03)

    image_bottom = PIL.Image.new("RGB", (im_x, bottom_cum_size), (0, 0, 0))

    I1 = ImageDraw.Draw(image_bottom)
    myFont = ImageFont.truetype(r"C:\Windows\Fonts\Arial.ttf", font_size)

    infodata = []

    if image_path_orig:
        infodata.append((f"ПУТЬ К ИЗОБРАЖЕНИЮ:", image_path_orig))

    if date_photo_made:
        infodata.append((f"ДАТА АЭРОФОТОСЪЕМКИ:", date_photo_made))

    if date_submission:
        infodata.append((f"ДАТА ОБРАБОТКИ:", date_submission))

    padding = font_size // (len(infodata) - 1) if (len(infodata)) > 1 else font_size / 2

    for i in range(len(infodata)):
        I1.text((padding, i * font_size + padding * (i + 1)), infodata[i][0], font=myFont, fill=(255, 255, 255))
        I1.text((im_x // 2 - padding, i * font_size + padding * (i + 1)), str(infodata[i][1]), font=myFont,
                fill=(255, 255, 255))

    # image_bottom.show()

    dst = Image.new('RGB', (im_x, im_y + bottom_cum_size))
    dst.paste(image, (0, 0))
    dst.paste(image_bottom, (0, im_y))

    # dst.save(f"meta{path_to_image}.jpg")
    return dst


def process_image(photo_data: PhotoData):
    meta_images = []

    for i, box in enumerate(photo_data.bear_boxes):
        image = Image.open(photo_data.image_path)
        image = image.crop((box.min_x, box.min_y, box.max_x, box.max_y))
        ratio = image.size[0] / image.size[1]

        new_x = 620
        new_y = math.ceil(ratio * new_x)

        image = image.resize((new_x, new_y))
        # _image_path = f"{photo_data.image_path[:4]}{i}{photo_data.image_path[-4:]}"
        # image.save(_image_path)
        if new_y>new_x:
            image = image.rotate(90, expand=True)

        meta_images.append(add_meta(image,
                                    image_path_orig=photo_data.image_dir,
                                    date_submission=str(photo_data.date_of_creation),
                                    date_photo_made=str(photo_data.date_of_analysis)))

    return list(map(convert_to_black_pad, meta_images))


def convert_to_black_thumbnail(img):
    # 649x401
    thumbnail_size = (649, 401)

    background = Image.new('RGB', thumbnail_size, "black")
    source_image = img.convert("RGB")
    source_image.thumbnail(thumbnail_size)
    (w, h) = source_image.size
    background.paste(source_image, ((thumbnail_size[0] - w) // 2 - 5, (thumbnail_size[1] - h) // 2 - 5))
    return background


def convert_to_black_pad(img):
    return ImageOps.pad(img, (649, 401), color='black')
