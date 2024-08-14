import streamlit as st

# Columns 直排

st.title("欄位元件")

# 2columns 普通
col1, col2 = st.columns(2)
col1.button("按鈕1", key="b1")
col2.button("按鈕2", key="b2")

# 2columns 更改寬度
col1, col2 = st.columns([0.5, 1])
col1.button("按鈕1", key="b3")
if col2.button("按鈕2", key="b4"):
    st.snow()

# 3columns 更改寬度
col1, col2, col3 = st.columns([0.5, 0.5, 1])
col1.button("按鈕1", key="b5")
if col2.button("按鈕2", key="b6"):
    st.balloons()
col3.button("按鈕3", key="b7")

# with columns

col1, col2 = st.columns([0.5, 1])
with col1:
    st.button("按鈕1", key="b8")
    st.write("這是按鈕1")
with col2:
    st.button("按鈕2", key="b9")
    st.write("這是按鈕2")

# 多個columns
cols = st.columns(10)
for i in range(len(cols)):
    with cols[i]:
        if st.button(f"按鈕{i+1}", key=f"b{i+10}"):
            st.balloons()

st.markdown("""---""")

# 文字輸入元件
st.title("文字輸入元件")
# st.text_input指令格式 st.text_input(標題, value = 預設文字)
text = st.text_input("", value="請輸入文字")  #
st.markdown(f"您輸入的文字是：{text}")

st.markdown("""---""")

st.title("columns 比較排位")
st.markdown(""" ### #先分物件""")
col1, col2 = st.columns(2)

with col1:
    st.button("按鈕1", key="1")
    st.button("按鈕2", key="2")
    st.button("按鈕3", key="3")
with col2:
    st.write("這是col1")
    st.write("這是col2")
    st.write("這是col3")

st.markdown("""---""")
st.markdown(""" ### #先分欄位""")

for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"{i+4}")
    with col2:
        st.write(f"這是col{i+1}")
st.markdown("""---""")
st.title("session_state")
ans = 1
if st.button("按下去ans加1(無法增加)", key="a1"):
    ans = ans + 1
    st.write(f"ans: {ans}")
# session_state.
if "ans" not in st.session_state:
    st.session_state.ans = 1  # 設定session_state=1

col1, col2 = st.columns(2)
with col1:
    if st.button("按下去ans加1", key="a2"):
        st.session_state.ans = st.session_state.ans + 1
        st.write(f"ans: {st.session_state.ans}")
with col2:
    if st.button("按下去ans減1", key="a3"):
        st.session_state.ans = st.session_state.ans - 1
        st.write(f"ans: {st.session_state.ans}")

st.markdown("""---""")
