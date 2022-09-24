import os


def predict_bear(data_folder_path):
    os.system("python detect.py --weights runs/train/yolov7/weights/best.pt --source " + data_folder_path)
    
