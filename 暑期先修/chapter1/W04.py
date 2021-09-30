cost = int (input("Enter the cost of inventory:"))
rev = int (input("Enter the price of goods:"))
n = int (input("Enter the number maximum of demand:"))

#前三個使用者輸入的變數

print ("Enter the probability of each condition:")
p0 = float (input())
p1 = float (input())
p2 = float (input())
p3 = float (input())
p4 = float (input())
p5 = float (input())
p6 = float (input())
p7 = float (input())
p8 = float (input())

"""
9種情況各自的機率，若能用陣列概念程式碼會更簡潔
"""

profit = float() #預期利潤
d = 0 #d為從0開始的各種可能的需求
maxprofit = float()
maxd = float()

for q in range (0 , n+1) :
    for i in p0 , p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 : #for 迴圈 ， 跑8種可能的機率
        if d >= q :
            profit += ( rev - cost ) * q * i * 100 # 乘上100 為了躲避浮點數的不精確
        else :
            profit += ( d * rev - cost * q ) * i * 100

        #print (profit)
        d += 1# 每執行完一次for d上升1

    profit /= 100 #把先前乘上的100除掉

    if profit > maxprofit :
        maxprofit = profit
        maxd = q

    d = 0
    profit = 0.0

print (int(maxd //= 1) , int(maxprofit //= 1) )
