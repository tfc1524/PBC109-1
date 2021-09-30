x1 = int(input())
p1 = int(input())
x2 = int(input())
p2 = int(input())
t = int(input())
# 讀取題目所需資料

total = x1*p1 + x2*p2
# 算出購買總額

if t >= total:  # 檢查t夠不夠付錢
    print("$" + str(t-total))
else:
    print("-1")
