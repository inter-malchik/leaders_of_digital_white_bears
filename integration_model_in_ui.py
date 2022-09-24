import os


def predict_bear(data_folder_path):
    os.system(r"python C:\Users\sahab\Desktop\yolo_test\yolov7\detect.py --weights runs/train/yolov7/weights/best.pt --source " + data_folder_path)
    
