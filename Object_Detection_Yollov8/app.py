import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import os
from moviepy.editor import VideoFileClip

# Header
st.markdown("Created by: [Engr. Hamesh Raj](https://www.linkedin.com/in/datascientisthameshraj/)")

# Set up the Streamlit interface
st.title("🔍 YOLOv8 Object Detection on Video")
st.write("Upload a video file and perform object detection using YOLOv8.")

# File uploader
uploaded_file = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

# If a file is uploaded
if uploaded_file is not None:
    st.sidebar.video(uploaded_file)

    # Define a submit button
    if st.sidebar.button("Submit"):
        # Load YOLOv8 model
        model = YOLO("yolov8n.pt")

        # Save the uploaded video to a temporary file
        temp_video_path = "temp_video.mp4"
        output_path = "processed_video.mp4"
        
        # Ensure the temp file is written only once
        if not os.path.exists(temp_video_path):
            with open(temp_video_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        # Open the video file
        video = cv2.VideoCapture(temp_video_path)

        if not video.isOpened():
            st.error("Error: Could not open video file.")
        else:
            # Get video properties
            frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = video.get(cv2.CAP_PROP_FPS)

            # Define codec and create VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'avc1')
            out = cv2.VideoWriter("no_audio.mp4", fourcc, fps, (frame_width, frame_height))

            while video.isOpened():
                ret, frame = video.read()
                if not ret:
                    break

                # Perform object detection
                results = model(frame)

                # Draw bounding boxes on the frame
                for result in results:
                    boxes = result.boxes
                    for box in boxes:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        conf = box.conf[0]
                        cls = box.cls[0]
                        label = f'{model.names[int(cls)]} {conf:.2f}'

                        # Draw bounding box and label on frame
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

                # Write the frame with bounding boxes to the output video
                out.write(frame)

            # Release resources
            video.release()
            out.release()

            # Add audio back to the processed video
            clip = VideoFileClip(temp_video_path)
            audio = clip.audio
            video = VideoFileClip("no_audio.mp4")
            final = video.set_audio(audio)
            final.write_videofile(output_path, codec="libx264")

            st.success("Video processing complete.")

            # Display the processed video in the output section
            video_file = open(output_path, "rb").read()
            st.video(video_file)

            # Provide download link for the processed video
            with open(output_path, "rb") as file:
                st.download_button(
                    label="Download Processed Video",
                    data=file,
                    file_name="processed_video.mp4",
                    mime="video/mp4"
                )

        # Clean up the temporary files
        if os.path.exists(temp_video_path):
            os.remove(temp_video_path)
        if os.path.exists("no_audio.mp4"):
            os.remove("no_audio.mp4")
