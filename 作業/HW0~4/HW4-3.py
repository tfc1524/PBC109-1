infoStr = input()
infoStr = infoStr.split(',')
num = int(infoStr[0])  # 物品個數
limit = int(infoStr[1])  # 總重限制

weightStr = input()
weight = []
weightStr = weightStr.split(',')

valueStr = input()
value = []
valueStr = valueStr.split(',')

for i in range(num):
    weight.append(float(weightStr[i]))
    value.append(float(valueStr[i]))
# 將資料貼到list中

cp = []
for i in range(num):
    cp.append(value[i] / weight[i])
# 算cp值

ansV = []  # 儲存v演算法的答案
totalW_V = 0
maxV = 0
maxV_code = 0

while totalW_V < limit:  # 當總重沒超過
    for i in range(num):  # 找出目前最好的解
        if (i not in ansV) and ((totalW_V + weight[i]) <= limit):
            # 去除找過的和超重的
            if value[i] > maxV:
                maxV_code = i
                maxV = value[i]
            elif value[i] == maxV:
                if weight[i] < weight[maxV_code]:
                    # 效用相同，比重量。重量再相同則取編號小的所以用 < 而非 <=
                    maxV_code = i
                    maxV = value[i]
    if maxV != 0:  # 檢查是否為特殊情況
        totalW_V += weight[maxV_code]
        ansV.append(maxV_code)
        maxV = 0
        maxV_code = 0

    else:
        break
        """
        特殊情況:總重沒超過的情況下所有物品都會讓總重超重
        找不到適合的解但迴圈還是一直跑，就不要再找了
        """

ansCP = []
totalW_CP = 0
maxCP = 0
maxCP_code = 0

while totalW_CP < limit:  # 當總重沒超過
    for i in range(num):  # 找出目前最好的解
        if (i not in ansCP) and ((totalW_CP + weight[i]) <= limit):
            # 去除找過的和超重的
            if cp[i] > maxCP:
                maxCP_code = i
                maxCP = cp[i]
            elif cp[i] == maxCP:
                if weight[i] < weight[maxCP_code]:
                    # cp相同，比重量。重量再相同則取編號小的所以用 < 而非 <=
                    maxCP_code = i
                    maxCP = cp[i]
    if maxCP != 0:  # 檢查是否為特殊情況
        totalW_CP += weight[maxCP_code]
        ansCP.append(maxCP_code)
        maxCP = 0
        maxCP_code = 0
    else:
        break
        """
        特殊情況:總重沒超過的情況下所有物品都會讓總重超重
        找不到適合的解但迴圈還是一直跑，就不要再找了
        """

totalV_V = totalV_CP = float()

for i in ansV:
    totalV_V += value[i]

for i in ansCP:
    totalV_CP += value[i]

if totalV_CP > totalV_V:
    ansCP.sort()  # 將ans從小排到大

    for i in ansCP:  # 根據要求輸出ans
        if i != ansCP[-1]:
            print(i+1, end=',')
        else:
            print(i+1)
else:
    ansV.sort()  # 將ans從小排到大

    for i in ansV:  # 根據要求輸出ans
        if i != ansV[-1]:
            print(i+1, end=',')
        else:
            print(i+1)
