import cv2
import os
import time

# Function to stream images without saving a video file
def stream_images(image_folder, fps):
    # Get a list of image files in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]

    # Sort the images to ensure they are displayed in order
    images.sort()

    for image_name in images:
        img_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(img_path)

        if frame is None:
            print(f"Error: Could not read image {image_name}")
            continue

        cv2.imshow('Image Stream', frame)  # Display the frame as a stream

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Adjust the delay to match the desired frames per second (fps)
        time.sleep(1 / fps)
        

    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_folder = './input_frames/'  # Replace with the path to your image folder
    fps = 60.0  # Frames per second
    stream_images(image_folder, fps)
