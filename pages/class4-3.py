import streamlit as st
import os
import time
from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")

if "products" not in st.session_state:
    st.session_state.products = {
        "蘋果": {"price": 10, "stock": 10, "image": "image/apple.png"},
        "香蕉": {"price": 10, "stock": 10, "image": "image/banana.png"},
        "橘子": {"price": 10, "stock": 10, "image": "image/orange.png"},
    }

st.title("購買平台")
col_number = st.number_input("輸入欄數", min_value=1, max_value=5, value=2)
cols = st.columns(col_number)
i = 0

for product_name, details in st.session_state.products.items():
    with cols[i % len(cols)]:
        st.image(details["image"], use_column_width=True)
        st.markdown(f"### {product_name}")
        st.markdown(f"價格: ${details['price']}")
        st.markdown(f"庫存: {details['stock']}")

        if st.button(f"購買 {product_name}", key=f"{product_name}"):
            if details["stock"] > 0:
                st.session_state.products[product_name]["stock"] -= 1
                st.success(f"成功購買 {product_name}!")
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"{product_name} 無存貨，無法購買。")
    i += 1

st.title("新增商品庫存")
product_name = list(st.session_state.products.keys())

col1, col2 = st.columns(2)

with col1:
    product_name = st.selectbox("選擇要新增的商品", product_name)
with col2:
    add_number = st.number_input("輸入要新增的庫存", min_value=1, value=1)
if st.button("新增庫存", key="add"):
    st.session_state.products[product_name]["stock"] += add_number
    st.success(f"成功新增!")
    time.sleep(1)
    st.rerun()

st.write("目前庫存：")
for product_name, details in st.session_state.products.items():
    st.markdown(f"{product_name} 庫存: {details['stock']}")
