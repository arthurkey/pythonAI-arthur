from utils import set_background  # 從 utils.py 只匯入 set_background 函式

set_background("image/python-logo.png", 20, "left bottom")
# 字典(列表) dict

## 格式： {key1: value, key2: value, ...}
## key 不可重复
## key 不能是變數

## 讀取方式： dict_name[key]    ### 無法使用 index 來讀取
## 新增(修改)方式： dict_name[key] = value    ### 差別在於新增時寫的 key 不存在，修改時寫的 key 已經存在
## 刪除方式1： del dict_name[key]    ### 刪除後無法復原
## 刪除方式2： dict_name.pop(key, 刪除失敗會回傳這個值)
### 如果資料存在則刪除並回傳刪除後的值，否則回傳 pop 的第二個參數, 如果沒有第二個參數則會回傳錯誤
## 檢查方式： key in dict_name    ### True or False    #### 檢查 key 是否存在

## dict_name.keys() : 讀取 列表的 key
## dict_name.values() : 讀取 列表的 value
## dict_name.items() : 讀取 列表的 key, value

# 成績登記系統
## grade = {
##     "小明": {"國文": [92, 80, 70], "數學": [80, 90, 100], "英文": [70, 80, 90]},
##     "小美": {"國文": [80, 85, 99], "數學": [70, 80, 90], "英文": [90, 80, 70]},
##     "小芳": {"國文": [70, 87, 90], "數學": [90, 60, 70], "英文": [80, 90, 100]},
## }
### 得知小明的國文成績
## print(grade["小明"]["國文"])
### 得知小美的第一個數學成績
## print(grade["小美"]["數學"][0])
### 得知小芳的第二個英文成績
## print(grade["小芳"]["英文"][1])
### 讀取所有人的國文平均成績
## for name, subject in grade.items():
##     chin = subject["國文"]
##     avg = sum(chin) / len(chin)
##     print(f"{name} 的國文平均成績為 {avg:.2f}")
### 讀取所有人的總平均
## for name, subject in grade.items():
##     total = subject["國文"] + subject["數學"] + subject["英文"]
##     avg = sum(total) / (len(subject) * 3)
##     print(f"{name} 的總平均成績為 {avg:.2f}")
## avg_grade = {"國文": [], "數學": [], "英文": []}
## for subject in grade.values():
##     for subject, score in subject.items():
##         avg_grade[subject] += score
## print(avg_grade)
### avg_grade = {"國文": [92, 80, 70, 87, 70, 90],
###              "數學": [80, 90, 100, 60, 90, 70],
###              "英文": [70, 80, 90, 80, 90, 100]}
