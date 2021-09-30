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

cpSort = []  # 用來存排序後的cp值
cpSort = sorted(cp, reverse=True)
# 排序cp值
counterpart = totalW = int()
ans = []

for i in range(num):  # 用來index cpSort的
    for j in range(num):  # 用來找出原本的號碼
        if cpSort[i] == cp[j]:
            counterpart = j  # 原本的號碼

    if (weight[counterpart] + totalW) <= limit:  # 看重量有沒有超過
        totalW += weight[counterpart]
        ans.append(counterpart + 1)  # 注意index跟題目編號的差別

ans.sort()  # 將ans從小排到大

for i in ans:  # 根據要求輸出ans
    if i != ans[-1]:
        print(i, end=',')
    else:
        print(i)
