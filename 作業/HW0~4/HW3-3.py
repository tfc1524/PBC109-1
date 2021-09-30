condStr = input()  # condition為題目的背景設定(幾個級距、要買幾公斤)
cond = condStr.split(',')
LV_TOTAL = int(cond[0])
BASIC_D = int(cond[1])

infoStr = input()  # information，為級距和價格
info = infoStr.split(',')

lv = [0]  # 用來存級距
price = []  # 用來存價格

for i in range(LV_TOTAL):  # 將info中的資訊填到各自的list中
    lv.append(int(info[i]))
    price.append(int(info[i + LV_TOTAL]))

bestD = 0  # 最佳購買量
CostOfBestD = 99999999  # 最佳購買量下的成本
pay = 0  # 每個購買量下須付的錢

for test_d in range(BASIC_D, lv[-1] + 1):
    for i in range(1, LV_TOTAL + 1):
        if test_d >= lv[i]:
            pay += (lv[i]-lv[i - 1]) * price[i-1]
        elif lv[i - 1] <= test_d < lv[i]:
            pay += (test_d-lv[i-1]) * price[i-1]
        elif test_d < lv[i-1]:
            break
        # 判斷test_d和前一個級距、當次級距之間的關係並做出運算

    if pay <= CostOfBestD:  # 檢查此購買量下的成本有沒有小於最佳成本，如果有則取代
        bestD = test_d
        CostOfBestD = pay

    pay = 0  # 因為pay是用+=算出來，所以要歸0

print(str(bestD) + "," + str(CostOfBestD))
