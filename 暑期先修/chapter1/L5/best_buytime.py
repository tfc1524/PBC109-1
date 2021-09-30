#最佳再訂購點

#past sales
salesStr = "14 23 26 17 17 12 24 19 10 18 22 31 19 16 22 28 20 27 20 32"
sales = salesStr.split()
for i in range( len(sales) ):
    sales[ i ] = int( sales[ i ] )

#given information
stgCost = 2
invCost = 1000 * 0.073 / 365
Q = 30
I = 20


#finding the best R
bestR = 0
costOfBestR = 10000000
for R in range(Q):
    totalCost = 0

#finding the total cost of this R
    for s in sales:
        Ｉ-= s
        if I < 0:
            totalCost += -I * stgCost
            I += Q
        elif I < R:  #R isn't fixed
            I += Q

        if I > 0:
            totalCost += I * invCost
#updat bestR when necessary
    if totalCost < costOfBestR:
        bestR = R
        costOfBestR = totalCost

print(bestR)
