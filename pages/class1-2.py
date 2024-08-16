# 'hello world"hello python'''hello Visual Studio Code'''"'
from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")

import streamlit as st

st.title("這是標題")
st.write(
    "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
)
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
st.markdown(
    """
# 這是最大標題
## 這是第二大標題
### 這是第三大標題
#### 這是第四大標題
##### 這是第五大標題
###### 這是第六大標題
這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
例如：
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 代碼塊：
```python
print("Hello, Streamlit!")
```
"""
)


st.markdown(
    """
            # 這是最大標題

- 這是第一個項目
- 這是第二個項目
- 這是第三個項目

## 這是第二大標題

```python
print("hello world")
```

---

### 這是第三大標題

---
[連結](https://www.google.com)

#### 這是第四大標題

---

##### 這是第五大標題

---

###### 這是第六大標題

---

            """
)
