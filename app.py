import streamlit as st
import cv2
import pytesseract
import numpy as np
from PIL import Image
import os
import subprocess

# Function to download Tesseract OCR on Streamlit Cloud
def download_tesseract():
    tesseract_url = "https://github.com/tesseract-ocr/tesseract/releases/download/5.3.3/tesseract-5.3.3-linux-x86_64.AppImage"
    tesseract_path = "tesseract"

    # Download Tesseract binary if not already downloaded
    if not os.path.exists(tesseract_path):
        st.info("Downloading Tesseract OCR... Please wait ⏳")
        subprocess.run(["wget", tesseract_url, "-O", tesseract_path])
        subprocess.run(["chmod", "+x", tesseract_path])

    # Set Tesseract path for pytesseract
    pytesseract.pytesseract.tesseract_cmd = os.path.abspath(tesseract_path)

# Run the function to ensure Tesseract is installed
# download_tesseract()

# Streamlit App Title
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
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Extract text using Tesseract OCR
    text = pytesseract.image_to_string(gray)

    # Display extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text Output", text, height=200)
