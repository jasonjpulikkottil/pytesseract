import streamlit as st
import easyocr
import numpy as np
import cv2
from PIL import Image
import os

MODEL_PATH = "model_data"
os.makedirs(MODEL_PATH, exist_ok=True)

try:
    reader = easyocr.Reader(["en"], model_storage_directory=MODEL_PATH)
    st.write("OCR initialized successfully.")
except Exception as e:
    st.write("Error initializing EasyOCR:", e)

st.title(" Image to Text Converter (OCR)")
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)  # Convert PIL image to NumPy array

    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    result = reader.readtext(gray, detail=0)

    extracted_text = "\n".join(result)

    st.subheader("Extracted Text:")
    st.text_area("Text Output", extracted_text, height=200)
