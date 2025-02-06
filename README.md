
# 📄 Image to Text Converter (OCR) using EasyOCR

This project demonstrates an OCR (Optical Character Recognition) application built with **EasyOCR** and **Streamlit**. The app allows users to upload an image and extracts the text from the image using OCR technology.

## Features

- **OCR Functionality**: Converts text from images (PNG, JPG, JPEG) to editable text using EasyOCR.
- **Image Upload**: Simple drag-and-drop image uploader in the UI.
- **Text Output**: Displays extracted text in a readable format.
- **Easy Setup**: Automatically initializes the OCR model and handles the image processing.

## How it Works

1. **Image Upload**: The user uploads an image file (PNG, JPG, or JPEG).
2. **Preprocessing**: The image is converted to grayscale for improved OCR accuracy.
3. **OCR Extraction**: EasyOCR processes the image and extracts the text.
4. **Text Display**: The extracted text is displayed in a text area for easy copying.

## Requirements

To run this project, you'll need the following libraries installed:

- `streamlit`
- `easyocr`
- `numpy`
- `opencv-python`
- `Pillow`

You can install these dependencies using `pip`:

```bash
pip install streamlit easyocr numpy opencv-python Pillow
```

## Setup

1. Clone this repository or download the project files.
2. Install the required dependencies using the command above.
3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open the app in your browser, upload an image, and view the extracted text!

## Notes

- The OCR model is stored in the `model_data` directory. This directory will be created automatically if it doesn't exist.
- Currently, the app supports OCR for **English** text only. You can modify the language in the `easyocr.Reader()` initialization if you'd like to support other languages.

## Contributing

Feel free to fork the project, make improvements, or add additional features! If you encounter any issues or have suggestions, please open an issue.

## License

This project is licensed under the MIT License.
