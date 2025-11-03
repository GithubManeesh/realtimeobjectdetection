from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

color_list = [
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Cyan
    (255, 0, 255),   # Magenta
    (0, 255, 255),   # Yellow
    (128, 0, 128),   # Purple
    (0, 128, 255),   # Orange
    (128, 128, 0),   # Olive
    (0, 128, 128),   # Teal
]

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    results = model(frame, imgsz=416)[0]

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  
        conf = float(box.conf[0])              
        cls = int(box.cls[0])                  
        label = model.names[cls]               

        color = color_list[cls % len(color_list)]

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("Object Detection Webcam", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
