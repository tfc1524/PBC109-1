#旅行者問題
#set up the distance matrix
"""
#skip input process
numLoc = 5 #有5個地點

dst = [
[0 , 9 , 6 , 7 , 4] ,
[9 , 0 , 5 , 9 , 6] ,
[6 , 5 , 0 , 3 , 1] ,
[7 , 9 , 3 , 0 , 4] ,
[4 , 6 , 1 , 4 , 0]
]
"""
#input process
numLoc = int( input() )
dst = []
for i in range(numLoc) :
    dst.append( input().split() )
    for j in range(numLoc) :
        dst[i][j] = int( dst[i][j] )
#set up the origin
origin = 0

"""
tour : a list that will contain the solution
tourLen : the total distance of the solution
unvisited : a list that contains those unvisited locations at any time
"""

tour = [origin]
tourLen = 0
unvisited = []

for i in range(numLoc) :
    unvisited.append(i)
unvisited.remove(origin)

#The algorithm
cur = origin
for i in range(numLoc - 1) :

    print(tour , tourLen)

    #find the next location to visit
    next = -1
    minDst = 999
    for j in unvisited :
        if dst[cur][j] < minDst :
            next = j
            minDst = dst[cur][j]

    #move "next" from unvisited to tour
    unvisited.remove(next)
    tour.append(next)
    tourLen += minDst



    #run the next iteration from the next location
    cur = next

#complete the final step
tour.append(origin)
tourLen += dst[cur][origin]

#print out the solution
print(tour , tourLen)
