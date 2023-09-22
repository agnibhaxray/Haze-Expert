import streamlit as st 
import dehaze
import cv2
def main():
    st.title("Dehazing/Desmoking")
    uploaded_file = st.file_uploader("Upload a file", type=["jpg", "png", "jpeg","mp4", "mov"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded File", use_column_width=True)
        
        # Process the image when a button is clicked
        if st.button("Process File"):
            processed_file = dehaze.process_file(uploaded_file)
            st.image(processed_file, caption="Processed Image", use_column_width=True)

if __name__ == "__main__":
    main()
        