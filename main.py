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


print("Camera connected!")

cv2.namedWindow("Smart Baby Safety Monitor", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Smart Baby Safety Monitor",
                      cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (screen_width, screen_height))
    results = model(frame, verbose=False)

    furniture_boxes = []
    baby_centers = []

    for r in results:
        boxes = r.boxes
        if boxes is None:
            continue  


for box in boxes:
            cls = int(box.cls[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if cls in CLIMBABLE_CLASSES:
                furniture_boxes.append((x1, y1, x2, y2))
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.rectangle(frame,
                              (x1 + EDGE_MARGIN, y1 + EDGE_MARGIN),
                              (x2 - EDGE_MARGIN, y2 - EDGE_MARGIN),
                              (0, 255, 0), 2)

            if cls == PERSON_CLASS:
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)
                baby_centers.append((cx, cy))
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 3)
                cv2.circle(frame, (cx, cy), 6, (0, 255, 255), -1)

    danger_detected = False

    for (cx, cy) in baby_centers:
        for (fx1, fy1, fx2, fy2) in furniture_boxes:
            if is_in_edge_zone(cx, cy, fx1, fy1, fx2, fy2, EDGE_MARGIN):
                danger_detected = True

    if danger_detected:
        cv2.putText(frame,
                    "WARNING: Baby Near Furniture Edge!",
                    (50, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2,
                    (0, 0, 255),
                    4)

        start_alarm()

        current_time = time.time()
        if current_time - last_snapshot_time > snapshot_interval:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(LOG_FOLDER, f"danger_{timestamp}.jpg")
            cv2.imwrite(filename, frame)
            print("Snapshot saved:", filename)
            last_snapshot_time = current_time
    else:
        stop_alarm()

    cv2.imshow("Smart Baby Safety Monitor", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
stop_alarm()






