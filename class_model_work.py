import os
import integration_model_in_ui
import exceptions
import convert_to_jpeg


class ModelWork:

    @staticmethod
    def photo_processing(data_path):
        integration_model_in_ui.predict_bear(data_path)

    def photo_get_information(self, data_path):
        pass

    def puck_data_processing(self, data_folder_path):
        self.check_folder_data(data_folder_path)

        files = []
        for rootPack, dirsPack, filesPack in os.walk(data_folder_path):
            files = filesPack

        for file_name in files:
            self.photo_processing(data_folder_path + file_name)

    @staticmethod
    def check_folder_data(data_folder_path):
        data = os.walk(data_folder_path)

        kostil = []

        for i in data:
            kostil.append(i)

        root, dirs, files = kostil[0][0], kostil[0][1], kostil[0][2]

        for root_pack, dirs_pack, files_pack in data:
            root = root_pack
            dirs = dirs_pack
            files = files_pack

        try:
            if len(dirs) == 0:
                for file in files:
                    filename, file_extension = os.path.splitext(file)

                    try:
                        if file_extension != '.jpg':
                            if file_extension == '.png' or file_extension == '.bmp':
                                raise exceptions.format_photo_exception(file)
                    except exceptions.format_photo_exception:
                        convert_to_jpeg.convert_to_jpeg(data_folder_path +'\\' + file)
            else:
                raise exceptions.folder_data(data_folder_path)
        except exceptions.folder_data:
            exit(0)


