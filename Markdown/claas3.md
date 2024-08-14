### 1. Streamlit - 欄位元件 (Columns)

- **直排欄位 (Columns)**
  - 使用 `st.columns()` 來創建多個直排欄位，並可以設定每個欄位的寬度。
  - 例子：創建兩個欄位，並在每個欄位中放置按鈕。

    ```python
    col1, col2 = st.columns(2)
    col1.button("按鈕1", key="b1")
    col2.button("按鈕2", key="b2")
    ```

- **更改欄位寬度**
  - 可以通過傳遞一個列表來指定每個欄位的寬度比例。

    ```python
    col1, col2 = st.columns([0.5, 1])
    col1.button("按鈕1", key="b3")
    if col2.button("按鈕2", key="b4"):
        st.snow()
    ```

- **多個欄位 (3 columns)**
  - 可以創建多個欄位，並依次在每個欄位中放置元素。

    ```python
    col1, col2, col3 = st.columns([0.5, 0.5, 1])
    col1.button("按鈕1", key="b5")
    if col2.button("按鈕2", key="b6"):
        st.balloons()
    col3.button("按鈕3", key="b7")
    ```

- **使用 `with` 來組織欄位內容**
  - 可以使用 `with` 語法在欄位內部放置多個元素。

    ```python
    col1, col2 = st.columns([0.5, 1])
    with col1:
        st.button("按鈕1", key="b8")
        st.write("這是按鈕1")
    with col2:
        st.button("按鈕2", key="b9")
        st.write("這是按鈕2")
    ```

- **多個欄位的迴圈處理**
  - 透過 `for` 迴圈和 `st.columns()` 結合，可以動態創建多個欄位並放置元素。

    ```python
    cols = st.columns(10)
    for i in range(len(cols)):
        with cols[i]:
            if st.button(f"按鈕{i+1}", key=f"b{i+10}"):
                st.balloons()
    ```

### 2. Streamlit - 文字輸入元件

- **文字輸入框 (Text Input)**
  - 使用 `st.text_input()` 來創建文字輸入框，並可以設置預設值。

    ```python
    text = st.text_input("", value="請輸入文字")
    st.markdown(f"您輸入的文字是：{text}")
    ```

### 3. Streamlit - Session State

- **Session State**
  - 使用 `st.session_state` 保存狀態，如計數器或其他全局變數。
  - 例子：按鈕點擊後更新計數。

    ```python
    if "ans" not in st.session_state:
        st.session_state.ans = 1  # 設定 session_state = 1

    if st.button("按下去 ans 加1", key="a2"):
        st.session_state.ans += 1
        st.write(f"ans: {st.session_state.ans}")
    ```

### 4. Python 基礎

- **算術指定運算子**
  - `+=`、`-=`、`*=`、`/=`、`%=`、`**=`、`//=`：將算術運算與賦值結合的操作。

    ```python
    x = 1
    x += 1  # 等同於 x = x + 1
    ```

- **迴圈與條件**
  - **while 迴圈**：反覆執行一段程式碼，直到條件為 False。
  - **break**：中斷迴圈的執行。

    ```python
    i = 0
    while i < 10:
        print(i)
        i += 1
    ```

- **隨機操作 (Random)**
  - `random.randint()`：從指定範圍中隨機選擇一個整數。
  - `random.shuffle()`：隨機打亂列表中的元素。

    ```python
    import random as r
    ans = r.randint(1, 100)
    ```

- **例外處理 (Try, Except)**
  - 使用 `try` 來包裹可能出錯的程式碼，並在 `except` 區塊中處理錯誤。

    ```python
    a = 0
    try:
        a = a**0
    except:
        print("無法計算")
    ```

### 5. 猜數字遊戲

- 結合 `while` 迴圈、隨機數和條件語句，實作簡單的猜數字遊戲。

  ```python
  import random as r
  ans = r.randint(1, 100)
  lgb = 100
  lgs = 0
  gus = input(f"請輸入您的猜測({lgs}-{lgb}): ")
  times = 0

  while True:
      if int(gus) < ans and int(gus) > int(lgs):
          print("太小了")
          lgs = gus
      elif int(gus) > ans and int(gus) < int(lgb):
          print("太大了")
          lgb = gus
      elif int(gus) == ans:
          print("恭喜您，您猜對了")
          break
      gus = input(f"請輸入您的猜測({lgs}-{lgb}): ")
      times += 1
  ```
