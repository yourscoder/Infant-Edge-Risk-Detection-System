# Infant-Edge-Risk-Detection-System
Developed a real-time AI baby safety monitoring system that detects when infants approach dangerous edges of furniture or elevated surfaces. Built using Python, OpenCV, and YOLOv8, it analyzes live IP camera feeds, identifies risk zones, triggers alerts, and logs high-risk events.


An AI-powered real-time baby safety monitoring system that detects when infants approach dangerous edges of furniture or elevated surfaces using computer vision.
The system analyzes live camera feeds, identifies climbable furniture, maps risk zones, triggers alarms, and logs dangerous events to help prevent accidental falls.

🚀 Features
Real-time baby/person detection using YOLOv8


Detection of climbable furniture (beds, chairs, sofas, tables)


Intelligent edge danger zone monitoring


Automatic alarm alert when baby approaches risky areas


Snapshot logging of dangerous events


IP camera and webcam support




🧰 Tech Stack
Python


OpenCV


Ultralytics YOLOv8


IP Camera Streaming


Multi-threaded Alert System



📦 Installation
1️⃣ Clone Repository
git clone https://github.com/yourscoder/Infant-Edge-Risk-Detection-System.git
cd Infant-Edge-Risk-Detection-System


2️⃣ Install Python Requirements
Recommended Python Version:
Python 3.9 – 3.11

Install dependencies:
pip install opencv-python ultralytics playsound pygame


📷 IP Camera Setup
This project supports Android IP cameras using apps like:
IP Webcam


DroidCam


Alfred Camera


Setup Steps:
Install an IP camera app on your phone.


Connect phone and PC to the same WiFi network.


Start the camera server inside the app.


The app will display a streaming URL like:


http://192.168.X.X:8080/video

Replace the camera URL in the code:


CAMERA_URL = "http://YOUR_IP_ADDRESS:PORT/video"


🔔 Alarm Sound Functionality
The system plays an alarm when danger is detected.
To Use Custom Alarm Sound:
Place your audio file inside project folder.


Update the filename in code:


ALARM_SOUND = "alarm.mp3"

Supported formats depend on your audio library.

▶️ Running the Project
Run the main script:
python main.py


🧠 How It Works
Captures live video from IP camera or webcam


Detects baby/person using YOLOv8


Detects furniture objects


Creates edge danger zones


Monitors baby position relative to danger areas


Triggers alarm if unsafe behavior is detected


Saves snapshot logs of risky events



📁 Danger Log Storage
When danger is detected, images are saved automatically inside:
danger_logs/

These images can be used for monitoring or analysis.

⚙️ Configuration Options
You can modify:
Danger Edge Thickness
EDGE_MARGIN = 60

Alert Cooldown / Snapshot Frequency
snapshot_interval = 3

Supported Furniture Classes
CLIMBABLE_CLASSES = {56, 57, 59, 60}


💡 Future Improvements
Mobile notification alerts


Pose detection for climbing/falling prediction


Multi-camera support


Cloud logging integration


Custom baby detection model


