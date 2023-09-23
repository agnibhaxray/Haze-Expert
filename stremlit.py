import streamlit as st
from PIL import Image
import dehaze  # Import your modified dehaze.py script

# Title and description
st.title("Desmoking/Dehazing Web App")

uploaded_image = st.file_uploader("Upload a file", type=["jpg", "png", "jpeg", "mp4"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

if st.button("Process Image"):
    if uploaded_image is not None:
        # Convert the uploaded image data to bytes
        uploaded_image_bytes = uploaded_image.read()
        
        # Provide an output path for the processed image
        output_image_path = "processed_image.jpg"
        dehaze.dehaze(uploaded_image_bytes, output_image_path)
        
        processed_image = Image.open(output_image_path)
        st.image(processed_image, caption="Processed Image", use_column_width=True)
