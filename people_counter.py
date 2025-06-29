import cv2
import pygame
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load optimized YOLOv8 model
model = YOLO("yolov8n.pt")
model.fuse()  # Speed boost

# Deep SORT tracker
tracker = DeepSort(
    max_age=60,          # Track stays alive for 60 frames without detection
    n_init=3,            # Needs 3 hits to confirm
    max_iou_distance=0.7 # Adjusts matching sensitivity
)

# Pygame window setup
pygame.init()
screen = pygame.display.set_mode((416, 320))
pygame.display.set_caption("People Counter (Final)")
clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 416)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

# Counting variables
line_x = 208
enter_count = 0
exit_count = 0
tracked_ids = {}    # ID -> last_x
counted_ids = {}    # ID -> 'entered' or 'exited'

print("People Counter Running... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (416, 320))
    results = model(frame, conf=0.75, verbose=False)[0]  # Set threshold here

    detections = []

    # ---- DETECTION FILTERING ----
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
        if center_x > 360:  # Mirror zone (adjust as per your camera)
            continue

        detections.append(([x1, y1, w, h], conf, 'person'))

    # ---- TRACKING ----
    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        x1, y1, x2, y2 = map(int, track.to_ltrb())
        center_x = (x1 + x2) // 2

        prev_x = tracked_ids.get(track_id)
        direction = counted_ids.get(track_id)

        if prev_x is not None:
            if prev_x < line_x and center_x >= line_x and direction != "entered":
                enter_count += 1
                counted_ids[track_id] = "entered"
                print(f"✅ ID_{track_id} ENTERED")

            elif prev_x > line_x and center_x <= line_x and direction != "exited":
                exit_count += 1
                counted_ids[track_id] = "exited"
                print(f"🔁 ID_{track_id} EXITED")

        tracked_ids[track_id] = center_x

        # Draw box and ID
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID_{track_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # ---- VISUALS ----
    cv2.line(frame, (line_x, 0), (line_x, 320), (0, 0, 255), 2)
    cv2.putText(frame, f"Entered: {enter_count}", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, f"Exited: {exit_count}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # ---- PYGAME DISPLAY ----
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    surf = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))
    screen.blit(surf, (0, 0))
    pygame.display.flip()
    clock.tick(30)

    # ---- QUIT ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            cap.release()
            pygame.quit()
            exit()
