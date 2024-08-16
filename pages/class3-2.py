import streamlit as st
from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")

if "meals" not in st.session_state:
    st.session_state.meals = []

st.title("點餐機")

col1, col2 = st.columns(2)
with col1:
    st.write("請在下面輸入你想要的餐點:")
    meal = st.text_input("餐點名稱")
with col2:
    st.write("寫完後按下下面的按鈕加入點餐機")
    st.write("")
    st.write("")
    if st.button("增加餐點", key="add"):
        st.session_state.meals.append(meal)

st.markdown("""## 購物籃""")
for i in range(len(st.session_state.meals)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.meals[i])

    with col2:
        if st.button("刪除", key=i):
            st.session_state.meals.pop(i)
            st.rerun()
