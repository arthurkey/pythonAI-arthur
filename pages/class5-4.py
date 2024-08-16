import streamlit as st
import openai
from utils import load_openai_api, encode_image

openai_api_key = load_openai_api()

st.title("AI圖片分析")
uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="已上傳的圖片", width=300)

    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    base64_image = encode_image("temp_image.png")

    prompt = st.chat_input("請輸入想要對話的訊息")
    if prompt:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
        )

        assistant_message = response.choices[0].message.content
        st.write(assistant_message)
