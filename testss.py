import streamlit as st 
import dehaze
def main():
    st.title("Dehazing/Desmoking")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_image is not None:
        # Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        
        # Process the image when a button is clicked
        if st.button("Process Image"):
            processed_image = dehaze.process_image(uploaded_image)
            st.image(processed_image, caption="Processed Image", use_column_width=True)

if __name__ == "__main__":
    main()
