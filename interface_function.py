import class_model_work


def call_back(data_folder_path, save_folder_path):

    model = class_model_work.ModelWork(data_folder_path, save_folder_path)
    model.puck_data_processing(model.data_folder_path)
