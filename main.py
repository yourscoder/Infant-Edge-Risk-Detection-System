import cv2
from ultralytics import YOLO
from playsound import playsound
import threading
import time

CAMERA_URL = "http://192.168.10.159:8080/video"
model = YOLO("yolov8n.pt")

DANGER_ZONE = [(400, 0), (640, 480)]

ALARM_SOUND = "alarm.mp3"
alert_cooldown = 5
last_alert_time = 0


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
