Smart Baby Safety Monitor
Real-time computer vision system that detects when a baby gets dangerously close to furniture edges.

What It Does
Streams live video from an IP camera over WiFi, detects babies and nearby furniture using YOLOv8, and triggers a warning overlay plus audio alarm if a baby enters a furniture edge zone. Danger snapshots are saved automatically to a local folder. Runs fully offline on your local network.

Setup

Install dependencies:

pip install ultralytics opencv-python

Open baby_monitor.py and set your camera URL:
CAMERA_URL = "http://YOUR_PHONE_IP:8080/video"

Use an app like IP Webcam on Android to get the stream URL. Then run:
python baby_monitor.py
Press ESC to exit. YOLOv8 weights download automatically on first run.

How It Works
Each frame is passed through YOLOv8 nano for object detection. Furniture boxes (bed, sofa, chair) get an inner edge danger margin calculated inside them. Person detections are then filtered by bounding box size and aspect ratio to separate babies from adults. If a baby's center point falls inside the edge strip, danger is triggered. The alarm runs in a background thread and snapshots are saved with a 3-second cooldown between saves.

Key Parameters
EDGE_MARGIN (default 60px) — width of the danger zone inside furniture boxes.
BABY_MAX_HEIGHT_RATIO (default 0.40) — baby box height must be under 40% of frame height.
BABY_MAX_WIDTH_RATIO (default 0.25) — baby box width must be under 25% of frame width.
snapshot_interval (default 3 sec) — cooldown between saved snapshots.

If your camera is mounted low or close to the subject, increase BABY_MAX_HEIGHT_RATIO to 0.55.

Tech Stack
Python, OpenCV, YOLOv8 (Ultralytics), Threading, Tkinter
