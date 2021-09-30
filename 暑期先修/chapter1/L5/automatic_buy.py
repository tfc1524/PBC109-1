#自動訂補貨
#Q,R Policy
q = int( input( "Order quantity Q: ") )
r = int( input( "Reorder point R: ") )
i = int( input( "Initial inventory I: ") )

print("Inventory: " + str(i))

while True :
    sales = int( input("Sales in a day: ") )
    i = i - sales if i - sales>=0 else 0
    if i < r :#if you want to implement s,S policy , just modify this if circle
        i = i + q

        print( "Order!" )
    print( "Inventory: " + str( i ) )
