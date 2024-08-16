import streamlit as st
import os
from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")

st.title("圖片元件")
st.image("image/apple.png", width=300)

image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

image_size = st.number_input(
    "輸入圖片大小", min_value=50, max_value=500, step=50, value=100
)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=True)
