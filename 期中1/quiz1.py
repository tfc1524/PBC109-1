price1 = int(input())
price2 = int(input())
dis = int(input())

pay = price1 + price2 - dis

if pay >= 0:
    print(pay)
else:
    print(0)
