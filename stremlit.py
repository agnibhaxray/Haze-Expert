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
        # Read the uploaded image data as bytes
        uploaded_image_bytes = uploaded_image.read()
        
        # Process the image data using the dehaze function
        processed_image_bytes = dehaze.dehaze(uploaded_image_bytes)
        
        # Display the processed image
        processed_image = Image.open(io.BytesIO(processed_image_bytes))
        st.image(processed_image, caption="Processed Image", use_column_width=True)
