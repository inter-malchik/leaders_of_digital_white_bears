import class_model_work


def call_back(data_folder_path, save_folder_path):

    model = class_model_work.ModelWork(data_folder_path, save_folder_path)
    model.puck_data_processing(model.data_folder_path)


call_back(r"C:\Users\user\Desktop\GitHub\leaders_of_digital_white_bears\yolo\yolov7\data\folder", r"C:\Users\user\Desktop\hack\II_Moscow\test_results")