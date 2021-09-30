lv_total = int(input())
kg_buy = int(input())
# 讀取級距數和要買的量

lv_previous = 0
pay = 0
# lv_previous是為了紀錄前一個級距，pay則是應付的錢

for i in range(0, lv_total):
    lv = int(input())
    price = int(input())
    # 讀取每個t以及r

    if kg_buy >= lv:
        pay += (lv-lv_previous) * price
    elif lv_previous <= kg_buy < lv:
        pay += (kg_buy-lv_previous) * price
    elif kg_buy < lv_previous:
        continue
    # 判斷kg_buy和前一個級距、當次級距之間的關係並做出運算

    lv_previous = lv
    # 在下次迴圈開始前，將當次級距指派為下次的前一個級距

print(pay)
