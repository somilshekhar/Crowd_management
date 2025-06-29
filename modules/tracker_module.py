from deep_sort_realtime.deepsort_tracker import DeepSort

# Set up the Deep SORT tracker
tracker = DeepSort(
    max_age=60,
    n_init=3,
    max_iou_distance=0.7
)

def get_tracks(detections, frame):
    return tracker.update_tracks(detections, frame=frame)
