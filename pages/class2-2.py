# 'hello world"hello python'''hello Visual Studio Code'''"'

import streamlit as st

st.title("""練習-成績判斷""")
number = st.number_input("請輸入您的成績:  ", step=0.1)
if number > 100:
    number = "A+++?"
elif number == 100:
    number = "A++"
elif number >= 95:
    number = "A+"
elif number >= 90:
    number = "A"
elif number >= 85:
    number = "B+"
elif number >= 80:
    number = "B"
elif number >= 75:
    number = "C+"
elif number >= 70:
    number = "C"
elif number >= 65:
    number = "D+"
elif number >= 60:
    number = "D"
elif number < 60 and number >= 0:
    number = "F"
else:
    number = "無法判斷"
st.markdown(f"您的成績為 {number}")
st.markdown("""---""")
st.title("""練習-按鈕""")
st.button("按我一下", key="b1", help="按鈕可以有幫助訊息")
if st.button("快點按我", key="b2", help="按鈕可以召喚大雪"):
    st.snow()
if st.button("按我!", key="b3", help="驚喜"):
    st.balloons()
st.markdown("""---""")
