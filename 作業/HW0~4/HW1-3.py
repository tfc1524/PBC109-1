adult_ticket = int(input())
adult_price = int(input())
student_ticket = int(input())
student_price = int(input())
pay = int(input())
lim_ticket = int(input())
# 讀取題目所需資料

total = adult_ticket*adult_price + student_ticket*student_price
# 算出購買總額

if lim_ticket >= (adult_ticket + student_ticket):
    print(str(lim_ticket - (adult_ticket + student_ticket)), end=",")
# 判斷張數是否超過

if pay >= total:
    print("$" + str(pay-total))
# 判斷錢夠不夠
