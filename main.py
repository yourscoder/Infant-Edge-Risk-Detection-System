import os
import cv2
import winsound
import threading
import tkinter as tk
from ultralytics import YOLO
from datetime import datetime

CAMERA_URL = "http://192.168.10.159:8080/video"
model = YOLO("yolov8n.pt") 

EDGE_MARGIN = 60
CLIMBABLE_CLASSES = {56, 57, 59, 60}
PERSON_CLASS = 0  

LOG_FOLDER = "danger_logs"
alarm_active = False
last_snapshot_time = 0
snapshot_interval = 3 

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()



def alarm_loop():
    global alarm_active
    while alarm_active:
        winsound.Beep(1500, 400)
        winsound.Beep(1800, 400)
        time.sleep(0.2)
///////  

def start_alarm():
    global alarm_active
    if not alarm_active:
        alarm_active = True
        threading.Thread(target=alarm_loop, daemon=True).start()  


def stop_alarm():
    global alarm_active
    alarm_active = False

def is_in_edge_zone(px, py, x1, y1, x2, y2, margin):
    if not (x1 <= px <= x2 and y1 <= py <= y2):
        return False

    inner_x1 = x1 + margin
    inner_y1 = y1 + margin
    inner_x2 = x2 - margin
    inner_y2 = y2 - margin

    if inner_x1 < px < inner_x2 and inner_y1 < py < inner_y2:
        return False

    return True

cap = cv2.VideoCapture(CAMERA_URL)

if not cap.isOpened():
    print("Camera connection failed")
    exit()






