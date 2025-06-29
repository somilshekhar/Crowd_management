import csv
import os
from datetime import datetime

LOG_PATH = "logs/log.csv"

# Create CSV header if file does not exist
if not os.path.exists(LOG_PATH):
    with open(LOG_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "TrackID", "Direction"])

def log_event(track_id, direction):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, f"ID_{track_id}", direction])
