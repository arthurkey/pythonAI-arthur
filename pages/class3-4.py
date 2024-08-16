import random as r
from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")

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
    else:
        print("請不要跟本遊戲開玩笑")
    gus = input(f"請輸入您的猜測({lgs}-{lgb}): ")
    times += 1

    if times >= 15:
        print("^@^#()*^$#%^&*()")
        break
    elif times >= 10:
        print("請不要讓豬來玩本遊戲")
    elif times >= 7:
        print("智商太差了")
    elif times >= 5:
        print("有點ㄌㄡ")
# try, except
# 若是try有錯誤，則執行 except 的程式
a = 0
try:
    a = a**0
except:
    print("無法計算")
