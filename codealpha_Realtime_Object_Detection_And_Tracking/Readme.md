🎯 Real-Time Object Detection and Tracking using YOLO & Deep SORT

📌 Project Overview
This project implements a *real-time object detection and tracking* system using state-of-the-art computer vision and deep learning techniques. The system detects multiple objects from live video input and tracks them consistently across frames by assigning *unique tracking IDs*.

The project integrates:
- *YOLO (You Only Look Once)* for fast and accurate object detection
- *Deep SORT (Deep Simple Online Realtime Tracking)* for robust multi-object tracking



🚀 Key Features
- Real-time object detection using a pre-trained YOLOv8 model
- Multi-object tracking with Deep SORT
- Unique ID assignment for each object
- Robust tracking during occlusions and overlaps
- Live webcam or video file support
- Clean and safe program termination
- Modular and extensible codebase


🧠 Technologies & Tools Used

🔹 Programming Language
    * Python 3.x

🔹 Libraries & Frameworks
    Tool - Purpose 

  1.OpenCV - Video capture, frame processing, visualization 
  2.YOLOv8 (Ultralytics) - Real-time object detection 
  3.Deep SORT - Multi-object tracking & re-identification 
  4.PyTorch - Deep learning backend 
  5.NumPy - Numerical operations 

🏗️ System Architecture

Video Input (Webcam / Video File)
            ↓
Frame Extraction (OpenCV)
            ↓
Object Detection (YOLOv8)
            ↓
Feature Extraction (Deep SORT CNN)
            ↓
Kalman Filter Prediction
            ↓
Hungarian Algorithm Matching
            ↓
Tracking ID Assignment
            ↓
Real-Time Display with IDs

The application runs in a continuous loop to process live video streams. The detection and tracking stop when the user presses the ESC key or closes the video window, after which the webcam is released and all OpenCV resources are safely deallocated.