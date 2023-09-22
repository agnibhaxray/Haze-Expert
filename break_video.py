import cv2
import sys
import os

def extract_frames(video_path, output_dir):
    # Open the video file for reading
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frame_count = 0

    # Loop through the video frames
    while True:
        # Read the next frame from the video
        ret, frame = cap.read()

        # If the frame was not read successfully, break out of the loop
        if not ret:
            break

        # Construct the output file path
        output_file = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")

        # Save the frame as an image
        cv2.imwrite(output_file, frame)

        # Increment the frame count
        frame_count += 1

    # Release the video file and close any open windows
    cap.release()
    cv2.destroyAllWindows()

    print(f"{frame_count} frames extracted and saved to {output_dir}")

# Example usage:
# Specify the path to the video file and the output directory
video_path = sys.argv[1]
output_directory = "input_frames"

# Call the function to extract frames
extract_frames(video_path, output_directory)
