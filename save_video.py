import cv2
import sys
import os

# Parameters
image_folder = './output_frames/'  # Replace with the path to your image folder
video_name = sys.argv[1]
fps = 29.70  # Frames per second

# Get a list of image files in the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]

frame = cv2.imread(os.path.join(image_folder, images[0]))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'XVID' for AVI format
out = cv2.VideoWriter(video_name, fourcc, fps, (frame.shape[1], frame.shape[0]))
print(str(images))
for image in sorted(images):
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    out.write(frame)  # Write the frame to the video

# Release the VideoWriter and close the window
out.release()

print(f"Video '{video_name}' created successfully.")
