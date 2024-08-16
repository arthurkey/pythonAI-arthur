import streamlit as st
import openai
from utils import load_openai_api

openai_api_key = load_openai_api()

st.title("生成圖片")
prompt_text = st.text_area("請輸入圖片的描述：")
if st.button("生成圖片"):
    generatedImage = openai.images.generate(
        model="dall-e-3",
        prompt=prompt_text,
        n=1,
        size="1024x1024",
    )
    image_url = generatedImage.data[0].url
    st.image(image_url)
