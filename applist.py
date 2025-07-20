import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# CIFAR-10 class labels
class_names = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

# Load model
model = load_model("cifar10_model.keras")

st.set_page_config(page_title="CIFAR-10 Classifier")
st.title("🚀 CIFAR-10 Image Classifier")

uploaded_file = st.file_uploader("Upload a 32x32 image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).resize((32, 32))
    st.image(img, caption="Uploaded Image", use_column_width=False)

    # Preprocess image
    img_array = image.img_to_array(img)
    img_array = img_array.reshape((1, 32, 32, 3)) / 255.0

    # Predict
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.success(f"Prediction: **{predicted_class}**")
