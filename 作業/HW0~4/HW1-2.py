x1 = int(input())
p1 = int(input())
x2 = int(input())
p2 = int(input())
t = int(input())
b = int(input())
# 讀取題目所需資料

total = x1*p1 + x2*p2
# 算出購買總額

if b >= (x1 + x2):  # 沒超過購票限制的情況下
    if t >= total:  # 檢查t夠不夠付錢
        print(str(b - (x1 + x2)) + "," + "$" + str(t-total))
    else:
        print(str(b - (x1 + x2)) + "," + "-2")
else:  # 超過購票限制了
    if t >= total:  # 檢查t夠不夠付錢
        print("-1" + "," + "$" + str(t-total))
    else:
        print("-1" + "," + "-2")
