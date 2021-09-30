infoStr = input()
infoStr = infoStr.split(',')
LIMIT_X = int(infoStr[0])  # x的最大值
LIMIT_Y = int(infoStr[1])  # y的最大值
LIM_DST = int(infoStr[2]) # 距離的最大值

POP = [[0] * (LIMIT_X + 1) for i in range(LIMIT_Y + 1)]

for i in range(LIMIT_Y + 1):
    popStr = input()
    popStr = popStr.split(',')
    for j in range(LIMIT_X + 1):
        POP[i][j] = int(popStr[j])
        # print(POP)
# 讀取各城鎮人口數

cover_pop = [[0] * (LIMIT_X + 1) for i in range(LIMIT_Y + 1)]
# print(cover_pop)
for i in range(LIMIT_Y + 1):
    for j in range(LIMIT_X + 1):  # (i,j)是以每個點為主體
        for k in range(LIMIT_Y + 1):
            for m in range(LIMIT_X + 1):  # 和(i,j)以外的每個點(k,m)算距離並看有沒有在限制內
                dst = abs(i - k) + abs(j - m)
                if dst <= LIM_DST:
                    cover_pop[i][j] += POP[k][m]
                    # print(cover_pop)
                    # print(cover_pop)
max_cover = 0
for i in range(LIMIT_Y + 1):
    for j in range(LIMIT_X + 1):
        if cover_pop[i][j] >= max_cover:
            max_cover = cover_pop[i][j]

# print(cover_pop)
print(max_cover)
