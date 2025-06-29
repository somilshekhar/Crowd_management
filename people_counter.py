import cv2
import pygame

from modules.detector import detect_people
from modules.tracker_module import get_tracks
from modules.counter import count_and_draw
from modules.display import init_window, draw_ui

# Initialize window and webcam
screen, clock = init_window()
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 416)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

print("People Counter Running... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (416, 320))

    detections = detect_people(frame)
    tracks = get_tracks(detections, frame)
    enter_count, exit_count = count_and_draw(tracks, frame)

    draw_ui(screen, frame, enter_count, exit_count)
    clock.tick(30)

    # Quit handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            cap.release()
            pygame.quit()
            exit()
