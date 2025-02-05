import streamlit as st
import easyocr
import numpy as np
import cv2
from PIL import Image
import os

# Ensure the model is stored in the correct directory
MODEL_PATH = "model_data"
os.makedirs(MODEL_PATH, exist_ok=True)

# Initialize EasyOCR Reader with English language only for testing
try:
    reader = easyocr.Reader(["en"], model_storage_directory=MODEL_PATH)
    st.write("EasyOCR initialized successfully.")
except Exception as e:
    st.write("Error initializing EasyOCR:", e)

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

    # Extract text using EasyOCR
    result = reader.readtext(gray, detail=0)

    # Join extracted text
    extracted_text = "\n".join(result)

    # Display extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text Output", extracted_text, height=200)
