import streamlit as st
import tempfile
import cv2
import numpy as np
from detector import process_blood_group_image
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(page_title="Blood Group Detector", layout="wide")
st.title("🧪 Blood Group Detection App")
st.write("Upload an image from blood grouping test and detect the blood type.")

uploaded_file = st.file_uploader("Choose a blood test image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    st.image(Image.open(temp_path), caption="Uploaded Image", use_container_width=True)
    result, images = process_blood_group_image(temp_path)

    if isinstance(result, str) and result.startswith("Error"):
        st.error(result)
    else:
        st.success(f"🩸 Predicted Blood Group: **{result}**")

        st.subheader("🖼️ Image Processing Stages")
        cols = st.columns(3)
        keys = list(images.keys())

        for i in range(len(keys)):
            with cols[i % 3]:
                st.image(images[keys[i]], caption=keys[i], clamp=True, use_container_width=True)
