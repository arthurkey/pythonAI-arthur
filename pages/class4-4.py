# def 函數定義
# def hello():
#     print("Hello World!")


# # 函數呼叫
# hello()


# # 函數參數(呼叫參數時可回傳一個值)
# def hello(name):
#     print("Hello " + name + "!")


# hello("World")  # 結果: Hello World!


# return 函數參數
## 只要執行return 就會回傳函數參數, 並結束函數
## def add(a, b):
##     return a + b

## add(1, 2)  # 結果: 3


# return 可以傳入多個值
# def add_sub(a, b):
#     return a + b, a - b

# sum, sub = add_sub(5, 6)
# print(f"sum = {sum}, sub = {sub}")  # 結果: sum = 11, sub = 1

# 多個return
# def add_sub(a, b):
#     if a > b:
#         return a - b, a + b
#     else:
#         return a + b, a - b
# print(add_sub(5, 6))  # 結果: (11)
# print(add_sub(6, 5))  # 結果: (1)


# 預設參數
# 可以在函數中定義預設參數，如果函數呼叫時沒有指定參數，就會使用預設參數
# 多個參數時，有預設值的參數要放在後面
# def add(a, b=0):
#     return a + b

# print(add(1))  # 結果: 1
# print(add(1, 2))  # 結果: 3

# 提示參數
# 可以在函數定義時加上提示參數，可以提醒輸入者輸入的資料類型
# def add(a: int, b: int = 0): -> int:
#     return a + b

# print(add(1, 2))  # 結果: 1
# print(add('hello', 'world'))  # 結果: helloworld
