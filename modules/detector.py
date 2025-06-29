from ultralytics import YOLO

# Load and fuse YOLOv8n model
model = YOLO("yolov8n.pt")
model.fuse()

def detect_people(frame):
    results = model(frame, conf=0.75, verbose=False)[0]
    detections = []

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = model.names[cls]

        if label != "person":
            continue

        w, h = x2 - x1, y2 - y1
        center_x = (x1 + x2) // 2

        if w < 50 or h < 100:
            continue
        if center_x > 360:
            continue

        detections.append(([x1, y1, w, h], conf, 'person'))

    return detections
