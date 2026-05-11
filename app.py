import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# ---------- PAGE CONFIG ----------

st.set_page_config(
    page_title="AI Electrical Fault Detection",
    page_icon="⚡",
    layout="centered"
)

# ---------- STYLISH UI ----------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

h1 {
    text-align: center;
    color: cyan;
    font-size: 50px;
}

.stFileUploader {
    background-color: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 15px;
}

.stButton>button {
    background: linear-gradient(to right, #ff416c, #ff4b2b);
    color: white;
    border-radius: 12px;
    border: none;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

img {
    border-radius: 20px;
    border: 3px solid cyan;
}

</style>
""", unsafe_allow_html=True)

# ---------- LOAD MODEL ----------

model = load_model("model.h5")

# ---------- LABELS ----------

labels = ["short_circuit", "wire_damage"]

# ---------- MAPPINGS ----------

fire_map = {
    "short_circuit": "yes",
    "wire_damage": "no"
}

voltage_map = {
    "short_circuit": "high",
    "wire_damage": "low"
}

place_map = {
    "short_circuit": "indoor",
    "wire_damage": "outdoor"
}

# ---------- TITLE ----------

st.markdown(
    "<h1>⚡ AI Electrical Fault Detection ⚡</h1>",
    unsafe_allow_html=True
)

st.write("Upload image or use camera for smart detection 🔥")

# ---------- FILE UPLOAD ----------

uploaded_file = st.file_uploader(
    "Upload Electrical Fault Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    img = cv2.imdecode(file_bytes, 1)

    st.image(img, caption="Uploaded Image", use_container_width=True)

    img_resized = cv2.resize(img, (128, 128))
    img_resized = img_resized / 255.0
    img_resized = np.expand_dims(img_resized, axis=0)

    prediction = model.predict(img_resized)

    index = np.argmax(prediction)

    result = labels[index]

    confidence = np.max(prediction) * 100

    st.success(
        f"Predicted Fault: {result} ({confidence:.2f}%)"
    )

    st.write("🔥 Fire:", fire_map[result])

    st.write("⚡ Voltage:", voltage_map[result])

    st.write("📍 Place:", place_map[result])

    if result == "short_circuit":
        st.warning("💡 Solution: Replace damaged wires and turn off power.")
    else:
        st.info("💡 Solution: Replace insulation and secure wiring.")

    st.balloons()

# ---------- CAMERA ----------

st.subheader("📷 Live Camera Detection")

camera_image = st.camera_input("Take a picture")

if camera_image is not None:

    file_bytes = np.asarray(
        bytearray(camera_image.read()),
        dtype=np.uint8
    )

    img = cv2.imdecode(file_bytes, 1)

    st.image(img, caption="Camera Image", use_container_width=True)

    img_resized = cv2.resize(img, (128, 128))
    img_resized = img_resized / 255.0
    img_resized = np.expand_dims(img_resized, axis=0)

    prediction = model.predict(img_resized)

    index = np.argmax(prediction)

    result = labels[index]

    confidence = np.max(prediction) * 100

    st.success(
        f"Predicted Fault: {result} ({confidence:.2f}%)"
    )

    st.write("🔥 Fire:", fire_map[result])

    st.write("⚡ Voltage:", voltage_map[result])

    st.write("📍 Place:", place_map[result])

    st.balloons()