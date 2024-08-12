import streamlit as st

st.markdown(
    """
## 基本語法與運算

### 單行與多行註解

```python
# 這是單行註釋

'''
這
是
多
行
注
解
'''
```

- 單行註解使用 `#`，通常用來簡單描述某行代碼的功能。
- 多行註解使用三引號 (`'''`) 包含，適合用來註解較長的段落或解釋。

### 輸出到終端機

```python
print("在終端機顯示文字")
```

- `print()` 函數用來在終端機顯示文字或變數的值。

### 資料型態

```python
print(1)  # int
print(1.0)  # float
print("1")  # str
print(True)  # bool
```

- `int`：整數
- `float`：浮點數
- `str`：字串
- `bool`：布林值

### 變數

```python
a = 10  # 新增變數a 並用'='設質為10
print(a)  # 在終端機顯示a的值
```

- 使用 `=` 來賦值給變數。

### 基本運算符

```python
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 ** 1)  # 次方
print(1 % 1)  # 取餘數
print(1 // 1)  # 整數除法
```

- 基本數學運算符號：`+`、`-`、`*`、`/`、`**`、`%`、`//`。

### 計算順序

```python
# 1.() 括號
# 2.** 次方
# 3. // 整數除法 / 除法  % 取餘數  * 乘法
# 4. + - 加減
```

- 運算順序：括號 > 次方 > 乘除與取餘數 > 加減。

## 字串操作

### 字串運算

```python
print("1" + "1")  # 字串加法 = 11
print("1" * 3)  # 字串乘法 = 111
```

- 字串的 `+` 用來連接字串，`*` 用來重複字串。

### 字串格式化

```python
print(f"1{1}ekfjbv{234698}1")  # f 字串格式化
```

- 使用 `f` 來進行字串插值，將變數的值插入字串中。

### 取長度

```python
print(len("1"))  # 字串長度 = 1
print(len([1, 2, 3]))  # 陣列長度 = 3
```

- 使用 `len()` 函數來獲取字串或列表的長度。

## 資料類型與轉換

### 取得資料物件的屬性

```python
print(type(1))  # int
print(type("1"))  # str
print(type([1, 2, 3]))  # list
```

- 使用 `type()` 函數來查看變數的資料型態。

### 型態轉換

```python
# 轉為整數 int
int(1.0)  # 1
int("1")  # 1

# 轉為浮點數 float
float(1)  # 1.0

# 轉為字串 str
str(1)  # "1"

# 轉為布林值 bool
bool(1)  # True
```

- 常見的型態轉換函數有 `int()`、`float()`、`str()` 和 `bool()`。

## 輸入與輸出

### 讀取輸入

```python
a = input("請輸入一個整數：")  # 讀取輸入
print(a)  # 輸出讀取的輸入
```

- 使用 `input()` 函數來讀取使用者輸入，並將輸入值賦值給變數。

### 圓面積計算範例

```python
pi = 3.14
a = int(input("Please enter the radius of the circle: "))
print(a * a * pi)
```

- 結合輸入與型態轉換來進行簡單的計算。

## Streamlit 基本用法

### 顯示標題

```python
import streamlit as st
st.title("這是標題")
```

- 使用 `st.title()` 來顯示標題。

### 顯示文字與格式化字串

```python
st.write(
    "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
)
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
```

- `st.write()` 支援顯示多種格式的內容。
- `st.text()` 僅能顯示純文字。

### 使用 Markdown 語法

```python
st.markdown(
    '''
    # 這是最大標題
    ## 這是第二大標題
    ### 這是第三大標題
    例如：
    * **粗體文字**
    * *斜體文字*
    * [連結](https://www.example.com)
    * 代碼塊：
    ```python
    print("Hello, Streamlit!")
    ```
    '''
)
```

- `st.markdown()` 可用來顯示含有 Markdown 語法的字串，支援多種格式如標題、連結、代碼塊等。


"""
)
