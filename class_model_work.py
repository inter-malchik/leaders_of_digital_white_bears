import os
from yolo.yolov7 import integration_model_in_ui
import exceptions
import convert_to_jpeg
from datetime import datetime
from image_add_metainformation import *


class ModelWork:

    def __init__(self, data_folder_path, save_folder_path):
        self.data_folder_path = data_folder_path
        self.save_folder_path = save_folder_path

    @staticmethod
    def photo_processing(data_path):
        integration_model_in_ui.predict_bear(data_path)

    def info_pack(self, data_folder_path, processed_data_path):
        parent_directory = data_folder_path
        processing_date = datetime.now().date()

        print(processed_data_path)

        data = os.walk(processed_data_path)
        data_list = []

        for rootPack, dirsPack, filesPack in data:
            data_list.append([rootPack, dirsPack, filesPack])

        for i in data_list:
            print(i)

        markup_path = data_list[0][0]
        markup_filename = data_list[0][2][0] if data_list[0][2][0][-7:] == '_xy.txt' else data_list[0][2][1]
        image_path = data_list[0][0]
        image_filename = data_list[0][2][0] if data_list[0][2][0][-7:] != '_xy.txt' else data_list[0][2][1]


        information = {"parent_directory": parent_directory, "processing_date": processing_date, "markup_path": markup_path + '\\' + markup_filename,
                       "markup_filename": markup_filename, "image_path": image_path + '\\' + image_filename, "image_filename": image_filename}

        for i in information:
            print(i, information[i])

        return information

    def save_photo(self, save_folder_path, file, image):
        image.save(save_folder_path + '\\' + file)

    def puck_data_processing(self, data_folder_path):
        self.check_folder_data(data_folder_path)
        print("chek ok")

        files = []
        for rootPack, dirsPack, filesPack in os.walk(data_folder_path):
            files = filesPack

        for file_name in files:
            print(f"current file {file_name}")
            self.photo_processing(data_folder_path + file_name)
            data_base = open(r"C:\Users\user\Desktop\GitHub\leaders_of_digital_white_bears\yolo\yolov7\dataBase.txt", 'r')
            information = self.info_pack(data_folder_path, r"C:\Users\user\Desktop\GitHub\leaders_of_digital_white_bears\yolo\yolov7\\" + data_base.readline())

            # обработа фото

            img_path = data_folder_path + '\\' + file_name


            temp_2 = PhotoData(information["markup_path"], img_path, datetime.fromtimestamp(os.path.getmtime(img_path)), information["processing_date"], [])

            temp_2.scan_bear_boxes(information["markup_path"])

            imgs = process_image(temp_2)

            for i, im in enumerate(imgs):
                im.save(self.save_folder_path + '\\' + str(i) + file_name)



    @staticmethod
    def check_folder_data(data_folder_path):
        data = os.walk(data_folder_path)

        kostil = []

        for i in data:
            kostil.append(i)

        root, dirs, files = kostil[0][0], kostil[0][1], kostil[0][2]

        for \
                root_pack, dirs_pack, files_pack in data:
            root = root_pack
            dirs = dirs_pack
            files = files_pack

        try:
            if len(dirs) == 0:
                for file in files:
                    filename, file_extension = os.path.splitext(file)

                    try:
                        if file_extension != '.JPG':
                            if file_extension == '.png' or file_extension == '.bmp':
                                raise exceptions.format_photo_exception(file)
                            else:
                                raise exceptions.cant_convert_file_to_jpg(file)
                    except exceptions.format_photo_exception:
                        convert_to_jpeg.convert_to_jpeg(data_folder_path +'\\' + file)

                    except exceptions.cant_convert_file_to_jpg:
                        exit(0)
            else:
                raise exceptions.folder_data(data_folder_path)
        except exceptions.folder_data:
            exit(0)


