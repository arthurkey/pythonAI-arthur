# 'hello world"hello python'''hello Visual Studio Code'''"'
import streamlit as st

st.title("""數字金字塔""")

number = st.number_input("請輸入一個數字:  ", step=1)

for i in range(1, number + 1):
    x = str(i) * i
    st.write(x)
st.markdown("""---""")

st.title("""箭頭金字塔""")

num = st.number_input("input a number:", step=1)

a = ""
for i in range(1, num + 1):
    a = a + (" " * (num - i) + "*" * (i * 2 - 1) + "\n")

for i in range(num):
    a = a + (" " * (num - 1) + "*" + "\n")

st.markdown(f"```\n結果:\n{a}\n```")
