info = input().split(',')
num = int(info[0])  # 向量個數
dim = int(info[1])  # 向量維度(子項項數)

# 讀取向量
vector = []  # 存向量的list
for i in range(num):
    vectorStr = input().split(',')
    new_v = []
    for j in range(dim):
        new_v.append(int(vectorStr[j]))

    vector.append(new_v)

min_dist = 999999

# 算兩兩向量間的距離
for i in range(num):
    for j in range((i + 1), num):
        this_dist = 0
        for k in range(dim):
            this_dist += pow((vector[i][k] - vector[j][k]), 2)
            if k == dim - 1:  # 算完兩向量的距離
                if this_dist < min_dist:
                    min_dist = this_dist  # 成為新的最小值

print(min_dist)
