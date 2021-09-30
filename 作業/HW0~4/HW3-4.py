TOTAL_Pro = int(input())  # 商品種類

discStr = input()
discStr = discStr.split(',')
disc = []  # 用來記錄折扣商品種類
for i in discStr:
    disc.append(int(i))

priceStr = input()
priceStr = priceStr.split(',')
price = []  # 用來記錄各商品單價

buy_numStr = input()
buy_numStr = buy_numStr.split(',')
buy_num = []  # 用來記錄各商品以原價購買數量

for i in range(TOTAL_Pro):  # 把資訊append到list內
    price.append(int(priceStr[i]))
    buy_num.append(int(buy_numStr[i]))

disc_pack = 999999.0  # 打9折組數
disc_5 = float()  # 打8折組數(每當disc_pack湊成5的倍數時，disc_5+1)

original_c = 0.0  # 原本應付的錢
for i in range(TOTAL_Pro):  # 先算出原本應付的錢，因為之後會動到buy_num
    original_c += price[i] * buy_num[i]

for i in disc:  # 決定湊成的打9折組數
    if buy_num[i - 1] <= disc_pack:
        disc_pack = buy_num[i - 1]

for i in disc:  # 將打9折組數從原價組數中扣除
    buy_num[i - 1] -= disc_pack

disc_5 = disc_pack // 5  # 算出湊滿5的倍數有幾組
disc_pack -= disc_5 * 5  # 扣除

new_c = 0.0
deduct = 0.0
increase = 0.0
"""
這邊我不重新計算全部的cost
只將涉及打折的商品的舊cost扣除再加上新cost
採用的公式為
new_c = original_c - deduct + increase
"""

if disc_5 > 0:  # 折扣組數>=5的情況
    for i in disc:
        deduct += price[i - 1]*(buy_num[i - 1]+disc_pack+disc_5 * 5)
        increase += price[i - 1]*(buy_num[i - 1] * 1.0+disc_pack * 0.9+disc_5 * 5 * 0.8)
else:  # 折扣組數<5的情況
    for i in disc:
        deduct += price[i - 1]*(buy_num[i - 1] + disc_pack)
        increase += price[i - 1]*(buy_num[i - 1] * 1.0+disc_pack * 0.9)

saving = deduct - increase  # 用來使下面兩行程式碼不要太冗長而設的變數
new_c = original_c - saving
people = saving // 1000

if people > 0:  # 輸出的條件判斷
    print(str(int(new_c)) + "," + str(int(people)))
else:
    print("So sad. I messed up.")
