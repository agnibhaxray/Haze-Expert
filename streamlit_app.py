import streamlit as st
import cv2
import numpy as np
import argparse
from PIL import Image
import dehaze  # Replace with the name of your image processing script

# Title and description
st.title("Desmoking/Dehazing Web App")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

if st.button("Process Image"):
    # Read the uploaded image
    output_image_path = "output_image.jpg"  # Provide an output path
    dehaze.dehaze(uploaded_image, output_image_path)
    processed_image = Image.open(output_image_path)
    st.image(processed_image, caption="Processed Image", use_column_width=True)
    
    