### 字典(dict) 筆記

#### 基本格式

- 格式：`{key1: value, key2: value, ...}`
- `key` 不可重複，且不能是變數。

#### 讀取、新增、刪除操作

- **讀取方式**：`dict_name[key]`
  - 不能使用索引（index）來讀取。
- **新增或修改**：`dict_name[key] = value`
  - 新增時寫的 `key` 不存在，修改時寫的 `key` 已經存在。
- **刪除方式1**：`del dict_name[key]`
  - 刪除後無法復原。
- **刪除方式2**：`dict_name.pop(key, 刪除失敗會回傳這個值)`
  - 如果資料存在則刪除並回傳刪除後的值，否則回傳 `pop` 的第二個參數。如果沒有第二個參數則會回傳錯誤。

#### 檢查及其他操作

- **檢查 key 是否存在**：`key in dict_name`
  - 回傳 True 或 False。
- **讀取所有 `key`**：`dict_name.keys()`
- **讀取所有 `value`**：`dict_name.values()`
- **讀取所有 `key, value`**：`dict_name.items()`

### 成績登記系統範例

```python
grade = {
    "小明": {"國文": [92, 80, 70], "數學": [80, 90, 100], "英文": [70, 80, 90]},
    "小美": {"國文": [80, 85, 99], "數學": [70, 80, 90], "英文": [90, 80, 70]},
    "小芳": {"國文": [70, 87, 90], "數學": [90, 60, 70], "英文": [80, 90, 100]},
}

# 得知小明的國文成績
print(grade["小明"]["國文"])

# 得知小美的第一個數學成績
print(grade["小美"]["數學"][0])

# 得知小芳的第二個英文成績
print(grade["小芳"]["英文"][1])

# 讀取所有人的國文平均成績
for name, subject in grade.items():
    chin = subject["國文"]
    avg = sum(chin) / len(chin)
    print(f"{name} 的國文平均成績為 {avg:.2f}")

# 讀取所有人的總平均成績
for name, subject in grade.items():
    total = subject["國文"] + subject["數學"] + subject["英文"]
    avg = sum(total) / (len(subject) * 3)
    print(f"{name} 的總平均成績為 {avg:.2f}")

# 計算各科目平均成績
avg_grade = {"國文": [], "數學": [], "英文": []}
for subject in grade.values():
    for subject, score in subject.items():
        avg_grade[subject] += score
print(avg_grade)
```

### Streamlit 圖片元件範例

```python
import streamlit as st
import os

st.title("圖片元件")
st.image("image/apple.png", width=300)

image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

image_size = st.number_input("輸入圖片大小", min_value=50, max_value=500, step=50, value=100)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=True)
```

### Streamlit 購買平台範例

```python
import streamlit as st
import os
import time

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
```

### 函數定義與使用範例

```python
# 定義函數
def hello():
    print("Hello World!")

# 呼叫函數
hello()

# 帶參數的函數
def hello(name):
    print("Hello " + name + "!")

hello("World")  # 結果: Hello World!

# 回傳值的函數
def add(a, b):
    return a + b

print(add(1, 2))  # 結果: 3

# 回傳多個值
def add_sub(a, b):
    return a + b, a - b

sum, sub = add_sub(5, 6)
print(f"sum = {sum}, sub = {sub}")  # 結果: sum = 11, sub = 1

# 多個 return 的函數
def add_sub(a, b):
    if a > b:
        return a - b, a + b
    else:
        return a + b, a - b

print(add_sub(5, 6))  # 結果: (11)
print(add_sub(6, 5))  # 結果: (1)

# 預設參數的函數
def add(a, b=0):
    return a + b

print(add(1))  # 結果: 1
print(add(1, 2))  # 結果: 3

# 帶提示參數的函數
def add(a: int, b: int = 0) -> int:
    return a + b

print(add(1, 2))  # 結果: 3
print(add('hello', 'world'))  # 結果: helloworld
```
