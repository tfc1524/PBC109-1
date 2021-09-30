kg_buy = int(input())
lv1 = int(input())
price1 = int(input())
lv2 = int(input())
price2 = int(input())
lv3 = int(input())
price3 = int(input())

pay = int()

if kg_buy <= lv1:
    pay = kg_buy * price1
elif lv1 < kg_buy <= lv2:
    pay = lv1*price1 + (kg_buy-lv1) * price2
else:
    pay = lv1*price1 + (lv2-lv1) * price2 + (kg_buy-lv2) * price3
# 各級距下應付的錢的算法

print(pay)
