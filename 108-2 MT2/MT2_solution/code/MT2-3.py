
# 讀入 2 維矩陣
n = int(input())
data = []
for i in range(n):
    data.append(input().split(','))
    for j in range(n):
        data[i][j] = int(data[i][j])

# assigned[i] = j 意思為將工作 j 分配給第 i 個人
assigned = [0 for i in range(n)]
sum = 0
indexi = 0  # 人
indexj = 0  # 工作
for iteration in range(n):
    min = 101
    for i in range(n):
        # 若這個人已分配到工作，則跳過
        if(assigned[i] != 0):
            continue
        for j in range(n):
            # 若這個工作已被分配給某個人，則跳過
            if((j+1) in assigned):
                continue
            # 注意：只要我們是從上而下，從左至右找最小值，
            # 這個條件是充分的（若你覺得不安心可以把剩下的條件補上）
            if(data[i][j] < min):
                min = data[i][j]
                indexi = i
                indexj = j

    assigned[indexi] = indexj+1
    sum += min

for i in range(len(assigned)):
    if(i == len(assigned)-1):
        print(assigned[i], end=';')
    else:
        print(assigned[i], end=',')
print(sum)
