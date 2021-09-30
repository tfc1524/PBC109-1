cost = int ( input("Enter the cost of inventory:") )
rev = int ( input("Enter the price of goods:") )
n = int ( input("Enter the maximum of demand:") )
sv = int( input("Enter the salvage value: ") )

#read in the probability
p = []
counter = 0
print("Enter the probability of conditions: ")
while counter <= n:
    p.append( float(input()) )
    counter += 1

profit = float() #預期利潤
d = 0 #d為從0開始的各種可能的需求
maxprofit = float()
maxd = float()

for order in range (0 , n+1) :
    for i in p : #for 迴圈 ， 跑可能的機率
        if d >= order :
            profit += ( rev - cost ) * order * i * 100 # 乘上100 為了躲避浮點數的不精確
        else :
            profit += ( d * rev + ( (order - d) * sv ) - cost * order ) * i * 100

        #print (profit)
        d += 1# 每執行完一次for d上升1

    profit /= 100.0 #把先前乘上的100除掉

    if profit > maxprofit :
        maxprofit = profit
        maxd = order

    d = 0
    profit = 0.0

print (int(maxd // 1) , int(maxprofit // 1) )
