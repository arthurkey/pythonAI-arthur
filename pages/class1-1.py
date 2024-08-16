# 'hello world"hello python'''hello Visual Studio Code'''"'
from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")

"""

這
是
多
行
注
解

"""

# # 這是單行注釋
# print("在終端機顯示文字")  # print 是在終端機顯示文字的指令
# # ctrl + ? 可快速註解或取消註解

# print(1)  # int
# print(1.0)  # float
# print("1")  # str
# print(True)  # bool

# 變數
# a = 10 #新增變數a 並用'='設質為10
# print(a) #在終端機顯示 a 的值

# print(1+1) #加法
# print(1-1) #減法
# print(1*1) #乘法
# print(1/1) #除法
# print(1**1) #次方
# print(1%1) #取餘數
# print(1//1) #整數除法
# print(1/1) #除法

# 計算順序
# 1.() 括號
# 2.** 次方
# 3. // 整數除法 / 除法  % 取餘數  * 乘法
# 4. + - 加減

# 字串運算
# print("1" + "1") # 字串加法 = 11
# print("1" * 3) # 字串加法 = 111

# 字串格式化
# print(f"1{1}ekfjbv{234698}1") # f 字串格式化 11ekfjbv2346981

# # 取長度
# print(len("1")) = 1 # 字串長度 = 1
# print(len([1, 2, 3])) = 1 # 陣列長度 = 3

# 取得資料物件的屬性
# print(type(1)) # int
# print(type("1")) # str
# print(type([1, 2, 3])) # list
# print(type({1, 2, 3})) # dict

# 轉換型態
# 轉為整數 int
# int(1.0) # 1
# int("1") # 1
# int(True) # 1
# 轉為浮點數 float
# float(1) # 1.0
# float("1") # 1.0
# float(True) # 1.0
# 轉為字串 str
# str(1) # "1"
# str(1.0) # "1.0"
# str(True) # "True"
# 轉為布林值 bool
# bool(1) # True
# bool("1") # True
# bool(1.0) # True

# input 讀取輸入
# a = input("請輸入一個整數：") # 讀取輸入
# print(a) # 輸出讀取的輸入

# pi = 3.14
# a = int(input("Please enter the radius of the circle: "))
# print(a * a * pi)
