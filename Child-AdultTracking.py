from ultralytics import YOLO

import time
import torch
import cv2
import pandas as pd
from PIL import Image
import colorsys
import numpy as np
from collections import defaultdict

from deep_sort.utils.parser import get_config
from deep_sort.deep_sort import DeepSort
from deep_sort.sort.tracker import Tracker

deep_sort_weights = 'deep_sort/deep/checkpoint/ckpt.t7'
tracker = DeepSort(model_path=deep_sort_weights, max_age=70)

model = YOLO("best (1).pt")

video_path = "video/Play Therapy Session working on Feelings with Candy Land Game - Trim.mp4"
cap = cv2.VideoCapture(video_path)
# Get the video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_path = 'output3.mp4'
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))


track_history = defaultdict(lambda: [])
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        out.write(cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR))
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
