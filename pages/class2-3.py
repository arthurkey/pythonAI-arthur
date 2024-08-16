# 'hello world"hello python'''hello Visual Studio Code'''"'
from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")

import streamlit as st

st.title("""練習-迴圈""")
st.markdown(
    """
for 迴圈
迴圈變數可隨意取名
迴圈變數會從 in 後面的變數中從起始值(或0)到中止值(不包括終止值)中取值
a = 10, for i in a, 會取出0, 1, ~, 9
a = 2, 10 會取出2 ~ 9
range 或 變數後的括號中, 第一個數是起始值, 第二個數是終止值, 第三個數是取值的間隔
for i in range(10):
    print(i) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(2, 10):
    print(i) # = 2, 3, 4, 5, 6, 7, 8, 9
for i in range(10, 2, -1):
    print(i) =10, 9, 8, 7, 6, 5, 4, 3
    """
)
