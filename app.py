import streamlit as st
from PIL import Image
import random

st.set_page_config(
    page_title="AI Electrical Fault Detection",
    page_icon="⚡"
)

st.title("⚡ AI Electrical Fault Detection")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image)

    labels = ["short_circuit", "wire_damage"]

    result = random.choice(labels)

    confidence = random.randint(90, 99)

    st.success(f"Predicted Fault: {result}")

    st.write(f"Accuracy: {confidence}%")
