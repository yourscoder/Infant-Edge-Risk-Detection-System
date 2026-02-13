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



def play_alarm():
    try:
        playsound(ALARM_SOUND)
    except Exception:
        print("Alarm sound error")


cap = cv2.VideoCapture(CAMERA_URL)

if not cap.isOpened():
    print("Camera connection failed")
    exit()

print("Camera connected")
