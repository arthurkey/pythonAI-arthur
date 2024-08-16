# 'hello world"hello python'''hello Visual Studio Code'''"'
from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")

# 比較運算子
# print(1 == 1) = True # == 等於
# print(1 != 1) = False # != 不等於
# print(1 > 1) = False # > 大於
# print(1 < 1) = False # < 小於
# print(1 >= 1) = True # >= 大於或等於
# print(1 <= 1) = True # <= 小於或等於

# 邏輯運算子
# and
# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False
# or
# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False
# not
# print(not True) # False
# print(not False) # True

# 計算順序
# 1.() 括號
# 2.** 次方
# 3. // 整數除法 / 除法  % 取餘數  * 乘法
# 4. + - 加減
# 5. == != > < >= <= 比較運算子
# 6. and not or 邏輯運算子

# if 與 else (while)
# 檢查密碼
# password = input("請輸入密碼：")
# while password == 123456:
#     password = input("請輸入密碼：")
#     if password == "123456":
#         print("密碼正確")
#     elif len(password) != 6:
#         print("密碼錯誤")
#         print("您的密碼由六個數字組成")
#         print("請重新輸入")
#     else:
#         print("密碼錯誤")

# if 與 else 的差別
# 如果用很多if來判斷同個東西，就算第一個if成功了，後面的if也會執行，直到最後一個if失敗。
# 如果用else來判斷，只有第一個if失敗時，才會執行else。
