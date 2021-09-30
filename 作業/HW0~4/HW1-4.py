# 讀取題目所需資料
pm = int(input())
temp = int(input())
ld = int(input())
standard = float(input())

# 宣告所需變數
w0 = 0.5
wa = float()  # 空氣赴約意願
wh = float()  # 濕度赴約意願
w = float()  # 最終赴約意願
wet = float()  # 濕度

# 算wa
if pm <= 35:
    wa = w0 + ((100-pm) * 0.005)
else:
    wa = w0 + ((45-pm) * 0.02)

# 驗證wa是否超出範圍
if wa >= 1.0:
    wa = 1.0
if wa <= 0.0:
    wa = 0.0

# print("wa" , wa) 驗算用

# 算wh
wet = 100 - 5 * (temp-ld)
if wet <= 30:
    wh = (w0 / 60.0) * (110-wet)
else:
    wh = (w0 / 45.0) * (90-wet)

# 驗證wh是否超出範圍
if wh >= 1.0:
    wh = 1.0
if wh <= 0.0:
    wh = 0.0

# print("wh" , wh) 驗算用

# 取較小者變成赴約意願值
if wa <= wh:
    w = wa
else:
    w = wh

# 輸出赴約意願值到小數第二位
print('{:.2f}'.format(w))

# 判斷是否大於臨界意願
if w >= standard:
    print("Let's go together.")
else:
    print("I wouldn't go out with you.")
