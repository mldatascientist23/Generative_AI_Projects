import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from tempfile import NamedTemporaryFile
import os

# Initialize YOLOv8 model
model = YOLO("yolov8n.pt")

# Streamlit app title and creator information

st.markdown("Created by: [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)")

st.title("🎥 YOLOv8 Object Detection on Videos")

# Sidebar for video upload
st.sidebar.header("Upload Video")
uploaded_video = st.sidebar.file_uploader("Choose a video...", type=["mp4", "mov", "avi", "mkv"])

if uploaded_video is not None:
    # Save the uploaded video to a temporary file
    temp_video = NamedTemporaryFile(delete=False)
    temp_video.write(uploaded_video.read())
    video_path = temp_video.name

    # Display the uploaded video
    st.sidebar.video(uploaded_video)

    # Submit button to process the video
    if st.sidebar.button("Submit"):
        st.subheader("Processing Video...")

        # Open the video file
        cap = cv2.VideoCapture(video_path)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Create a temporary file to save the output video
        temp_output_video = NamedTemporaryFile(delete=False, suffix='.mp4')
        output_video_path = temp_output_video.name

        # Define codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

        # Process each frame of the video
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Perform object detection
            results = model(frame)

            # Draw bounding boxes on the frame
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = box.conf[0]
                    cls = box.cls[0]
                    label = f'{model.names[int(cls)]} {conf:.2f}'

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            out.write(frame)

        cap.release()
        out.release()

        # Display the processed video
        st.subheader("Processed Video")
        st.video(output_video_path)

        # Download button for the processed video
        with open(output_video_path, "rb") as file:
            st.download_button(
                label="Download Processed Video",
                data=file,
                file_name="processed_video.mp4",
                mime="video/mp4"
            )

        # Clean up temporary files
        os.remove(video_path)
        os.remove(output_video_path)
