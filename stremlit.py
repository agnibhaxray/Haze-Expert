import streamlit as st
import numpy as np
import cv2
import os
import io
from PIL import Image
from PIL import Image
import dehaze  # Import your modified dehaze.py script
save_directory = "uploaded_images"

# Title and description
st.title("Desmoking/Dehazing Web App")
def delete_files(folder_path):
# List all files in the specified directory
    file_names = os.listdir(folder_path)

# Iterate through the files and remove them
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
uploaded_image = st.file_uploader("Upload a file", type=["jpg", "png", "jpeg", "mp4"])

if uploaded_image:
    file_name = uploaded_image.name
    os.makedirs(save_directory, exist_ok=True)
    file_path = os.path.join(save_directory, file_name)
    st.success(f"Image '{file_name}' has been saved to '{file_path}'")

    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_image.read())
    file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)

if st.button("Process Image"):
    if uploaded_image is not None:
        # Convert the uploaded image data to bytes
        folder_path = './uploaded_images'

        file_names = os.listdir(folder_path)

        file_names = [file for file in file_names if os.path.isfile(os.path.join(folder_path, file))]
        for file_name in file_names:
            output_image_path = "processed_"+file_name
            print(output_image_path)
            dehaze.dehaze("./uploaded_images/"+file_name, output_image_path)
        
        # Display the processed image
        processed_image = cv2.imread("processed_"+file_name)
        delete_files("./uploaded_images")
        st.image(processed_image, caption="Processed Image", use_column_width=False)
