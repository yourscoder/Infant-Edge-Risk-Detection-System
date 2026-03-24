import cv2
from ultralytics import YOLO
import time
import winsound
import threading
import os
import tkinter as tk
from datetime import datetime

CAMERA_URL = "http://192.168.10.81:8080/video"
model = YOLO("yolov8n.pt")

EDGE_MARGIN = 60
CLIMBABLE_CLASSES = {56, 57, 59, 60}
PERSON_CLASS = 0


BABY_MAX_HEIGHT_RATIO = 0.40   
BABY_MAX_ASPECT_RATIO = 1.2    
BABY_MAX_WIDTH_RATIO  = 0.25   


LOG_FOLDER = "danger_logs"
alarm_active = False
last_snapshot_time = 0
snapshot_interval = 3

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

root = tk.Tk()
screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

def alarm_loop():
    global alarm_active
    while alarm_active:
        winsound.Beep(1500, 400)
        winsound.Beep(1800, 400)
        time.sleep(0.2)

def start_alarm():
    global alarm_active
    if not alarm_active:
        alarm_active = True
        threading.Thread(target=alarm_loop, daemon=True).start()

def stop_alarm():
    global alarm_active
    alarm_active = False

def is_baby(x1, y1, x2, y2, frame_w, frame_h):
    """
    Returns True if the detected person is likely a baby/toddler.
    Filters by:
      - Height relative to frame  → babies are small
      - Width relative to frame   → babies are small
      - Aspect ratio (h/w)        → babies are taller than wide when sitting/standing
    """
    box_h = y2 - y1
    box_w = x2 - x1
    height_ratio = box_h / frame_h
    width_ratio  = box_w / frame_w
    aspect_ratio = box_h / box_w if box_w > 0 else 999

    return (
        height_ratio < BABY_MAX_HEIGHT_RATIO and
        width_ratio  < BABY_MAX_WIDTH_RATIO  and
        aspect_ratio < BABY_MAX_ASPECT_RATIO
    )







