import streamlit as st
import cv2
import pytesseract
import numpy as np
from PIL import Image

# Title of the Streamlit App
st.title("📄 Image to Text Converter (OCR)")

# File uploader for image input
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Convert image to OpenCV format
    image = Image.open(uploaded_file)
    img_array = np.array(image)  # Convert PIL image to NumPy array

    # Convert to grayscale for better OCR results
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text using Tesseract OCR
    text = pytesseract.image_to_string(gray)

    # Display extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text Output", text, height=200)
