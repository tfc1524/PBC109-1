condStr = input()  # condition為題目的背景設定(幾個級距、要買幾公斤)
cond = condStr.split(',')
lv_total = int(cond[0])
kg_buy = int(cond[1])

infoStr = input()  # information，為級距和價格
info = infoStr.split(',')

lv = [0]  # 用來存級距
price = []  # 用來存價格

for i in range(lv_total):  # 將info中的資訊填到各自的list中
    lv.append(int(info[i]))
    price.append(int(info[i + lv_total]))

pay = 0  # 應付的錢

for i in range(1, lv_total + 1):
    if kg_buy >= lv[i]:
        pay += (lv[i]-lv[i - 1]) * price[i-1]
    elif lv[i - 1] <= kg_buy < lv[i]:
        pay += (kg_buy-lv[i-1]) * price[i-1]
    elif kg_buy < lv[i-1]:
        continue
    # 判斷kg_buy和前一個級距、當次級距之間的關係並做出運算

print(pay)
