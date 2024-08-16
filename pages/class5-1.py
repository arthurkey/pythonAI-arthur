from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")

# global, locals 全域變數, 區域變數

# a1 = 1

# def f():
#     a2 = 2
#           #a1 = a1 + a2 (會出錯!)
#     print(a)

# a1 = 全域變數
# a2 = 區域變數

# length = 10
# area = 3.14* 100

# def f():
#     area = length**2    # 並不會將直接算出來 # 這是區域變數
#     print(area)

# length = 10
# f() # 100!!! # 在這時才會將area計算出來
# print(area) #314!!! # 這是外面的全域變數

# length = 5
# area = 3.14 * 100

# def f():
#     print(area)       # Error!!!
#     area = length**2
#     print(area)

# f()

# length = 10
# area = 3.14 * 100

# def f():
#     global area   # 將全域變數 area 傳進 f 函數 ，使得 f 可以修改它
#     area = length**2    # 並不會將直接算出來 # 這是區域變數
#     print(area)

# print(area) #314

# def f():
#     """
#     這裡可以為函數添加說明
#     """
#     global area   # 將全域變數 area 傳進 f 函數 ，使得 f 可以修改它
#     area = length**2    # 並不會將直接算出來 # 這是區域變數
#     print(area)

# f()
# print(area) #314!!! # 這是外面的全域變數
