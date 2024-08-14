# 算術指定運算子 = 算術運算子 + 指定運算子
# x = 1
# x += 1           # x = x + 1
# print(x)
# x -= 1           # x = x - 1
# print(x)
# x *= 1           # x = x * 1
# print(x)
# x /= 1           # x = x / 1
# print(x)
# x %= 1           # x = x % 1
# print(x)
# x **= 1          # x = x ** 1
# print(x)
# x //= 1          # x = x // 1
# print(x)

# 運算順序
# 1.() 括號
# 2.** 次方
# 3. // 整數除法 / 除法  % 取餘數  * 乘法
# 4. + - 加減
# 5. += -= *= /= %= **= //=

# while 迴圈
# while 會搭配一個條件式，如果條件式為 True 則執行迴圈中的程式。
# 每一次執行迴圈中的程式後，條件式會再次執行，直到條件式為 False。

# i = 0
# while i < 10:
#     print(i)
#     i += 1  # 結果：0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# break 退出迴圈
# break 會停止執行迴圈中的程式。

# i=0
# while True:
#     i = i+1
#     if i == 10: # 若是i = 10，則退出迴圈
#         break
#     print(i)
# i=0
# for i in range(10):
#     i = i + 1
#     if i == 3: # 若是i = 3，則退出迴圈
#         break
#     print(i)

# randen 隨機抽取
# import random as r    # 將random模組匯入r
# r.randint(終止值)    # 不包括終止值
# r.randint(開始值, 終止值)
# r.randint(開始值, 終止值, 遞進值)
# 隨機取一個整數，介於 a 和 b 之間
# r.randrange(終止值)    # 不包括終止值
# r.randrange(開始值, 終止值)
# r.randrange(開始值, 終止值, 遞進值)
# 隨機取一個整數，介於 a 和 b 之間
# r.choice(列表)
# 從列表中隨機取一個元素
# r.shuffle(列表)
# 把列表中的元素隨機打亂
# r.randint(開始值, 終止值)    # 不可少打開始值或中止值
# randint 會將終止值包括在其中
