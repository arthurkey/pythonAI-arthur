# 'hello world"hello python'''hello Visual Studio Code'''"'

import streamlit as st
from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")
st.title("Arthur's world")
