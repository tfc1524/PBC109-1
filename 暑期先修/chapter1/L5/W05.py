#第五週作業：基地臺位址選擇

#基礎資料讀取 幾個城鎮 選幾個 覆蓋距離
infStr = input()
inf = infStr.split()

#轉成整數
for i in range(3) :
    inf[ i ] = int( inf[ i ] )

n = inf[ 0 ]
p = inf[ 1 ]
d = inf[ 2 ]

#各城鎮的座標及人口數 可思考用二維list(感覺會變快)
x = []
y = []
pop = []

#讀取各城鎮的資料並轉成整數加入list
counter = 0
while counter < n :
    townStr = input()
    town  = townStr.split()

    for i in range(3) :
        town[ i ] = int( town[ i ] )

    x.append( town[ 0 ] )
    y.append( town[ 1 ] )
    pop.append( town[ 2 ] )

    counter += 1

#計算各城鎮的覆蓋人口
sum = 0
cover = []

for i in range(n) :
    sum = 0

    for j in range(n) :
        eachd =  float()
        eachd = pow( pow( x[ i ] - x [ j ] , 2 ) + pow( y[ i ] - y [ j ] , 2 ) , 0.5 )
        #print( str(i) + " " + str( j ) + "distance" + str(eachd) )

        if eachd <= d :
            sum += pop[ j ]


    cover.append(sum)
    #print(str(i)+" " + str(sum))


#找出最佳位址
maxt = 0
maxcover = 0
townselect = []
coverSum = 0

counter = p

#選p個
while counter > 0 :
    #找出最大cover人口
    for i in range(n) :
        if cover[ i ] > maxcover :
            maxcover = cover[ i ]
            maxt = i
    #紀錄結果
    townselect.append( maxt +1 )
    coverSum += maxcover
#有被覆蓋到的城鎮  城鎮人口變為0
    for j in range(n) :
        eachd = float()
        eachd = pow( pow( x[ j ] - x [ maxt ] , 2 ) + pow( y[ j ] - y [ maxt ] , 2 ) , 0.5 )
        #print( str(i) + " " + str( j ) + "distance" + str(eachd) )

        if eachd <= d :
            pop[ j ] = 0

    sum = 0
    cover = []

    #再算一次cover數
    for i in range(n) :
        sum = 0

        for j in range(n) :
            eachd =  float()
            eachd = pow( pow( x[ i ] - x [ j ] , 2 ) + pow( y[ i ] - y [ j ] , 2 ) , 0.5 )
            #print( str(i) + " " + str( j ) + "distance" + str(eachd) )

            if eachd <= d :
                sum += pop[ j ]


        cover.append(sum)
        #print(str(i)+" " + str(sum))

    maxt = 0
    maxcover = 0
    counter -= 1

for i in range( p ) :
    if i < p - 1 :
        print( townselect[ i ]  ,  end = " " )
    else  :
        print(  townselect[ i ] , coverSum )
