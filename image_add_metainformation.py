import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math
import datetime as dt

from dataclasses import dataclass


@dataclass
class BoxCoords:
    centre: tuple
    min_x: int
    max_x: int
    min_y: int
    max_y: int

    @staticmethod
    def parse_from_string(s):
        data = map(int, s.split(', '))
        return BoxCoords((data[0], data[1]), *data[2:6])


@dataclass
class PhotoData:
    markup_path: str
    image_path: str
    date_of_creation: dt.datetime
    date_of_analysis: dt.datetime = dt.datetime.now()
    bear_boxes: list = []

    def scan_bear_boxes(self, path_to_paramentic_file: str):
        f = open(path_to_paramentic_file, 'r')
        for line in f:
            if line and line != "\n":
                bear_boxes.append(BoxCoords.parse_from_string(line))
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
    im_x, im_y = image.size()
    
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

    padding = 100 // (len(infodata) - 1) if (len(infodata)) > 1 else 100 / 2

    for i in range(len(infodata)):
        I1.text((padding, i * 100 + padding * (i + 1)), infodata[i][0], font=myFont, fill=(255, 255, 255))
        I1.text((im_x // 2 - padding, i * 100 + padding * (i + 1)), str(infodata[i][1]), font=myFont,
                fill=(255, 255, 255))

    # image_bottom.show()

    dst = Image.new('RGB', (im_x, im_y + 500))
    dst.paste(image, (0, 0))
    dst.paste(image_bottom, (0, im_y))

    # dst.save(f"meta{path_to_image}.jpg")
    return dst


def process_image(photo_data: PhotoData):
    bear_boxes = [] #get bear boxes

    image = Image.open(photo_data.image_path)

    if bear_boxes:
        final_box_coords = get_zoom_rect(bear_boxes)

        bear_boxes = [final_box_coords]

        image.crop((final_box_coords.min_x, final_box_coords.max_y, final_box_coords.max_x, final_box_coords.min_y))

        image.save(photo_data.image_path)

    return add_meta(image,
                    image_path_orig=photo_data.image_path,
                    date_submission=str(photo_data.date_of_creation),
                    date_photo_made=str(photo_data.date_of_analysis))

