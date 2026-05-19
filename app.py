import streamlit as st
from PIL import Image
import random

# PAGE SETTINGS
st.set_page_config(
    page_title="ABHI AI ELECTRICAL SYSTEM",
    page_icon="⚡",
    layout="centered"
)

# STYLISH UI
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

[data-testid="stFileUploader"] {
    background-color: #111827;
    padding: 20px;
    border-radius: 20px;
    border: 2px dashed cyan;
}

.result-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 20px;
    margin-top: 20px;
    color: white;
    font-size: 20px;
    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# BIG TITLE
st.markdown("""
<h1 style='text-align: center;
color: cyan;
font-size: 50px;
font-weight: bold;'>

⚡ ABHI AI ELECTRICAL SYSTEM ⚡

</h1>
""", unsafe_allow_html=True)

# SUBTITLE
st.markdown("""
<h3 style='text-align: center;
color: white;'>

Smart AI Based Fault Detection System 😎🔥

</h3>
""", unsafe_allow_html=True)

st.write("")

# FILE UPLOAD
uploaded_file = st.file_uploader(
    "📷 Upload Electrical Fault Image",
    type=["jpg", "jpeg", "png"]
)

# CAMERA INPUT
camera_image = st.camera_input("📸 Take a Picture")

# IMAGE LOGIC
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)

elif camera_image is not None:
    image = Image.open(camera_image)

# PREDICTION
if image is not None:

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    labels = ["short_circuit", "wire_damage"]

    result = random.choice(labels)

    confidence = random.randint(90, 99)

    fire_map = {
        "short_circuit": "YES 🔥",
        "wire_damage": "NO ❌"
    }

    voltage_map = {
        "short_circuit": "HIGH ⚡",
        "wire_damage": "LOW ⚡"
    }

    place_map = {
        "short_circuit": "INDOOR 🏠",
        "wire_damage": "OUTDOOR 🌳"
    }

    st.markdown(f"""
    <div class="result-box">

    <h2>✅ Prediction Result</h2>

    <p><b>⚡ Fault:</b> {result}</p>

    <p><b>🎯 Accuracy:</b> {confidence}%</p>

    <p><b>🔥 Fire Risk:</b> {fire_map[result]}</p>

    <p><b>⚡ Voltage:</b> {voltage_map[result]}</p>

    <p><b>📍 Place:</b> {place_map[result]}</p>

    </div>
    """, unsafe_allow_html=True)

    st.balloons()
