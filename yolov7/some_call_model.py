import os

def detect_bear(file_name):
    os.system(fr"python detect.py --weights data/best.pt --source {file_name} --save-txt")

# detect_bear(r"data\folder\1488.JPG")