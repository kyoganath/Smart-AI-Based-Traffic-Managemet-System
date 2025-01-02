import cv2
import numpy as np

# Define video properties
frame_width = 1280
frame_height = 720
fps = 30
duration = 10  # in seconds

# Create a VideoWriter object
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Create blank frames
for _ in range(fps * duration):
    # Create a black frame
    frame = np.zeros((frame_height, frame_width, 3), np.uint8)
    
    # Optionally, draw shapes or text here on the frame
    cv2.putText(frame, 'Sample Frame', (200, 350), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
    
    # Write the frame to the video
    out.write(frame)

# Release the video writer object
out.release()

print("Video created successfully!")
