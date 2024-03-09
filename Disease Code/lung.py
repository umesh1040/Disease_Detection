import streamlit as st
import numpy as np
import pickle as pk
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model


# Load the trained model
loaded_model = load_model("Models/lung_cancer_model.h5")


# Function to preprocess the user-uploaded image
def preprocess_image(image):
    # Resize the image to match the input size used during training
    img_size = (256, 256)
    img = cv2.resize(image, img_size)
    img = img.reshape((1,) + img.shape + (1,))
    return img


st.markdown(
    "<h1 style='text-align: center;'>Lung Cancer Detection</h1>",
    unsafe_allow_html=True,
)
st.write(
    "Welcome to our Lung Cancer Detection tool! To get started, please upload a clear and high-resolution image of your chest CT scan. Our advanced model will analyze the image and provide you with insights on potential lung conditions. "
    "The Lung Cancer Detection algorithm is designed using Convolutional Neural Networks (CNNs), a robust approach for image recognition. The process involves preprocessing the CT scan images by resizing and applying Gaussian blur to enhance image quality and reduce noise."
)

image_path = "Images/lung.png"
st.image(image_path, output_format="JPEG", use_column_width=True)

# Upload image through Streamlit
uploaded_file = st.file_uploader("Upload you chest CT Scan Image:", type="jpg")

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file).convert("L")  # Convert to grayscale
    col1, col2, col3 = st.columns([1, 2, 2])
    with col2:
        st.image(
            image,
            caption="Image Uploaded Successfullly",
            use_column_width=False,
            width=400,
        )

    # Preprocess the image
    processed_image = preprocess_image(np.array(image))

    # Make prediction
    prediction = loaded_model.predict(processed_image)

    st.write("### Prediction Result:")
    heart_message_style = (
        "font-size: 20px; font-weight: bold; padding: 10px; border-radius: 5px; "
        "background-color: #FFD2D2; color: #FF0000; text-align: center;"
    )

    no_heart_message_style = (
        "font-size: 20px; font-weight: bold; padding: 10px; border-radius: 5px; "
        "background-color: #C2E0FF; color: #0000FF; text-align: center;"
    )

    if np.argmax(prediction) == 1:
        st.markdown(
            "<div style='{}'>No lung Cancer Detected.</div>".format(
                heart_message_style
            ),
            unsafe_allow_html=True,
        )
    elif np.argmax(prediction) == 0:
        st.markdown(
            "<div style='{}'>Lung Cancer Detected.</div>".format(heart_message_style),
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<div style='{}'>It is the average case might be present or might not be..!</div>".format(
                heart_message_style
            ),
            unsafe_allow_html=True,
        )
