# Description: This script streams the video from the RTMP server and runs YOLOv8 inference on the frames.

import cv2
from ultralytics import YOLO


# Load a YOLO model
version = "cubic100-v8m"
model = YOLO(f"../models/custom/{version}.pt")

# Stream the video from the RTMP server
stream_url = "rtmp://127.0.0.1//"
stream_key = "q3"
cap = cv2.VideoCapture(stream_url + stream_key)

# Set the window size
width = 640
height = 640
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', width, height)

# Loop through the video frames
while cap.isOpened():
    # Read the next frame
    success, frame = cap.read()
    if not success:
        break

    # Run YOLOv8 inference on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the frame with the results
    cv2.imshow('frame', annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
