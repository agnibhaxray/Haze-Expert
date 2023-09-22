import os
import cv2
import subprocess
import dehaze
# Directory containing your image files
image_dir = "./input_frames/"

# List all files in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg") or f.endswith(".png")]

# Loop through each image file
for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(image_dir, image_file)

    # Load the image using OpenCV
    img = cv2.imread(image_path)

    if img is not None:
        
        # Run your script or processing on the image here
        # For example, you can apply filters, perform object detection, or any other operation.
        command = ["python3", "dehaze.py", "-i", image_dir + image_file, "-o", "./output_frames/" + image_file]
        try:
               result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
               print("processed file:" + command[3])
               print(result.stdout)
        except subprocess.CalledProcessError as e:
               print("Error:", e)

        # After processing, you can save the result or display it, depending on your needs.
        # dehaze.runDehazingAlgo(input_file_path=image_path,output_file_path="./output_frames")
        # Example: Save processed image
        # processed_img = img  # Replace with your processing code
        # output_path = "./output_frames/output_" + image_file
        # cv2.imwrite(output_path, processed_img)

    else:
        print(f"Failed to load image: {image_file}")

print("Processing complete for all images.")
