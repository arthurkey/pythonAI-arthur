### 筆記：Python 程式碼說明

---

#### 1. **匯入模組與函式**

- 從 `utils.py` 匯入 `set_background` 函式來設定背景圖片。

   ```python
   from utils import set_background  
   set_background("image/python-logo.png", 20, "left bottom")
   ```

#### 2. **全域變數與區域變數**

- **全域變數 (Global Variable)**：定義在函數外部，整個程式皆可存取。
- **區域變數 (Local Variable)**：定義在函數內部，只能在函數內存取。
- 全域變數 `area` 和 `length` 可透過 `global` 關鍵字在函數內修改。
- 若在函數內定義了與全域變數同名的變數，該變數在函數內成為區域變數。
- `global` 關鍵字允許函數內部修改全域變數。

   ```python
   length = 10
   area = 3.14 * 100

   def f():
       global area   # 修改全域變數 area
       area = length ** 2
       print(area)   # 輸出新的 area 值

   f()
   print(area)  # 函數內修改後的全域變數 area 值
   ```

#### 3. **Streamlit 程式結構**

- **匯入必要的模組**：如 `streamlit`, `openai` 和 `utils` 。
- **設定背景圖片**：

   ```python
   set_background("image/python-logo.png", 20, "left bottom")
   ```

- **載入 OpenAI API 密鑰**：

   ```python
   openai.api_key = load_openai_api()
   ```

- **初始化 `st.session_state`**：管理應用狀態。
- **對話框與 AI 回應系統**：包括用戶的輸入、系統訊息設置、選擇 AI 模型和清除對話歷史。

   ```python
   if "history" not in st.session_state:
       st.session_state.history = []
   if "system_message" not in st.session_state:
       st.session_state.system_message = "每次回答只能回兩個繁體中文字元"
   ```

- **處理用戶對話輸入並顯示 AI 回應**：

   ```python
   prompt = st.chat_input("請輸入想要對話的訊息")
   if prompt:
       st.session_state.history.append({"role": "user", "content": prompt})
       response = openai.chat.completions.create(
           model=st.session_state.model,
           temperature=0.1,
           messages=[{"role": "user", "content": st.session_state.system_message}] + st.session_state.history,
       )
       assistant_message = response.choices[0].message.content
       st.session_state.history.append({"role": "assistant", "content": assistant_message})
       st.rerun()
   ```

#### 4. **生成圖片的 Streamlit 程式**

- 使用 OpenAI 的 `DALL-E` 模型生成圖片。

   ```python
   prompt_text = st.text_area("請輸入圖片的描述：")
   if st.button("生成圖片"):
       generatedImage = openai.images.generate(
           model="dall-e-3",
           prompt=prompt_text,
           n=1,
           size="1024x1024",
       )
       image_url = generatedImage.data[0].url
       st.image(image_url)
   ```

#### 5. **AI 圖片分析應用**

- 上傳圖片後，使用 `openai.chat.completions.create` 來處理圖片和用戶的文字輸入。

   ```python
   uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])
   if uploaded_file:
       st.image(uploaded_file, caption="已上傳的圖片", width=300)
       with open("temp_image.png", "wb") as f:
           f.write(uploaded_file.getbuffer())
       base64_image = encode_image("temp_image.png")

       prompt = st.chat_input("請輸入想要對話的訊息")
       if prompt:
           response = openai.chat.completions.create(
               model="gpt-4o-mini",
               messages=[
                   {"role": "user", "content": [
                       {"type": "text", "text": prompt},
                       {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                   ]},
               ],
           )
           assistant_message = response.choices[0].message.content
           st.write(assistant_message)
   ```

---
