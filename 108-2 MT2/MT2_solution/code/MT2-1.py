
def distance_square(p1, p2):
    # 計算兩點之間的距離
    if(len(p1) != len(p2)):
        return -1
    sum = 0
    for i in range(len(p1)):
        sum += (p1[i]-p2[i]) ** 2
    return sum


m, n = input().split(',')
m = int(m)
n = int(n)
data = []
for i in range(m):
    data.append(input().split(','))
    for j in range(n):
        data[i][j] = int(data[i][j])

min = 200 * 200 * 10
# 窮舉任兩個點之間的距離
for i in range(m):
    for j in range(i+1, m):
        dis = distance_square(data[i], data[j])
        if(dis < min):
            min = dis

print(min)
