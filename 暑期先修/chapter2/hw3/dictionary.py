nmStr = input()
nm = nmStr.split()

n = int( nm[ 0 ] )
m = int( nm[ 1 ] )

#讀取牆n面，油漆次數m

wall = dict()
number = []

for i in range( 1 , n + 1 ) :
    wall[ i ] = 0

#建構dictionary完成


for i in range( 0 , m ) :

    paintStr = input()
    paint = paintStr.split()

    start = int( paint[ 0 ] )
    final = int( paint[ 1 ] )
    color = int( paint[ 2 ] )

    number.append( color )
    for i in range( start , final + 1 ) :
        wall[ i ] = color
#上色過程

count = dict()
for key in range( 1 , n + 1 ) :
    if wall[ key ] not in count :
        count[ wall[ key ] ] = 1
    else:
        count[ wall[ key ] ] += 1
print(wall.items())
print(count.items())
counter = 0
"""
for i in number :
    if counter < m - 1 :
        print( str( i ) + " " + str( count[ i ] ) , end = ";" )
    else:
        print( str( i ) + " " + str( count[ i ] ) , end = "" )
"""
