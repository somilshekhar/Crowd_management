import cv2

# Constants and state
line_x = 208
enter_count = 0
exit_count = 0
tracked_ids = {}    # ID -> last_x
counted_ids = {}    # ID -> 'entered' or 'exited'

def count_and_draw(tracks, frame):
    global enter_count, exit_count

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

        # Draw bounding box and ID
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID_{track_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return enter_count, exit_count
