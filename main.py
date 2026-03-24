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






