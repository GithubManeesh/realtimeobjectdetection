Real-Time Object Detection with YOLOv8

A real-time object detection application that uses YOLOv8 to detect and classify objects through your webcam feed. Features custom color-coded bounding boxes and live confidence scores.

🚀 Features
Real-time Detection: Live object detection using webcam feed

Custom Color Scheme: Unique color-coded bounding boxes for different object classes

Confidence Display: Real-time confidence scores for each detection

Webcam Integration: Seamless webcam feed processing

Multiple Model Support: Compatible with all YOLOv8 variants

📋 Prerequisites
Python 3.7 or higher

Webcam

Internet connection (for first-time model download)

🛠️ Installation
Clone the repository

bash
git clone https://github.com/GitHubManeesh/realtimeobjectdetectionAI

cd realtimeobjectdetection

## 🚀 Quick Run

pip install -r requirements.txt

python Project.py

🔧 Model Information
Default Model: YOLOv8 Medium (yolov8m.pt)

First Run: The model will automatically download (≈50MB)

Subsequent Runs: Uses cached model for instant startup

Using Different Models
Modify the model name in Project.py:

python
# Change this line to use different YOLOv8 variants:
model = YOLO('yolov8m.pt')  # Default - Medium

# Available options:
model = YOLO('yolov8n.pt')   # Nano - Fastest, lowest accuracy

model = YOLO('yolov8s.pt')   # Small - Balanced speed/accuracy

model = YOLO('yolov8m.pt')   # Medium - Good balance (default)

model = YOLO('yolov8l.pt')  # Large - Higher accuracy

model = YOLO('yolov8x.pt')  # Extra Large - Highest accuracy, slowest

Controls:
ESC Key: Exit the application

The application uses your default webcam (index 0)

📊 Model Variants Comparison
Model	      Size	  Speed	   Accuracy	  Recommended Use
YOLOv8n	🟢 Nano	🟢 Fastest	🟢 Lowest	  Low-end hardware

YOLOv8s	🟡 Small	🟡 Fast	🟡 Low	  Basic laptops

YOLOv8m	🟠 Medium	🟠 Moderate	🟠 Medium	  Average hardware (Default)

YOLOv8l	🔴 Large	🔴 Slow	🔴 High	High-end PCs

YOLOv8x	🔵 X-Large	🔵 Slowest	🔵 Highest	Workstations, Servers

🎨 Custom Features
Color Scheme Implementation:

Custom color palette for object classification

10 distinct colors for different object types

Professional bounding box visualization

Real-time Processing:

Efficient frame-by-frame analysis

Smooth webcam feed handling

Optimized performance for real-time use

📁 Project Structure
text
├── Project.py          # Main application - Real-time object detection
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies

🔧 Technical Details
The application implements:

YOLOv8 model integration

OpenCV webcam capture

Real-time frame processing

Custom bounding box rendering

Dynamic text overlay with confidence scores

🐛 Troubleshooting
Model Download Issues:

Ensure internet connection on first run

Check firewall settings

Verify sufficient storage space (models: 6MB-130MB)

Webcam Issues:

Ensure webcam is not being used by another application

Check camera permissions

Verify OpenCV can access camera feed

Note: First execution will download the YOLOv8 model automatically. Subsequent runs will be instant as the model is cached locally.
