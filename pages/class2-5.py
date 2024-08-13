# 'hello world"hello python'''hello Visual Studio Code'''"'

# list 列表
# 用 [] 表示, 可放入任意資料內容, 用逗號隔開
# a = [1, 1.0, "1", True, [1, 1.0, "1", True]]
# print(a)

# 計算串列長度
# print(len(a))
# l = [1, 2, 3, a, b, c]
# for i in range(len(l)):
#     print(l[i]) # 會生成 l 的所有元素


# 讀取串列
# print(a[0])  # 列表第一個元素
# print(a[1:3])  # 列表第二個元素至第三個元素
# print(a[1:3:2])  # 列表第二個元素至第三個元素, 間隔為2
# print(a[1:])  # 列表第二個元素至最後一個元素
# print(a[:-1])  # 列表第一個元素至最後一個元素
# print(a[::-1])  # 列表第一個元素至最後一個元素, 反向

# !!!!!!!!!! #
# a = [1, 2, 3]
# b = a # 把b和a放在同一個記憶體位置, b改變, a 也會改變
# b[0] = 2
# print(a)
# a 會是 [2, 2, 3] !!!!!!!!!

# a = [1, 2, 3]
# b = a.copy() #!!!# # 複製a 的值給b, b改變, a 不會改變
# b[0] = 2
# print(a)
# a 會是 [1, 2, 3]

# append 增加
# l = [1, 2, 3]
# l.append(4)
# print(l)
# 結果會是 [1, 2, 3, 4]

# remove 刪除
# l = [1, 2, 3, 4]
# l.remove(2)
# print(l)
# 結果會是 [1, 3, 4] # 只會刪除第一個府和條件的值
# 如果想刪除所有值, 可以用 for 迴圈
l = [1, 2, 3, 4, 1]
for i in l:
    if i == 1:
        l.remove(i)
# pop 可移除指定index的值
# 若沒有指定index, 則刪除最後一個值
