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

bringStr = input()
bring = []
bringStr = bringStr.split(',')

for i in range(num):
    weight.append(int(weightStr[i]))
    value.append(int(valueStr[i]))
    bring.append(int(bringStr[i]))
# 將資料貼到list中

totalW = totalV = int()
# 總重與總價值

for i in range(num):
    if bring[i] == 1:  # 若有帶該物品，則將其重和價值加到總重和總價值中
        totalW += weight[i]
        totalV += value[i]

if totalW <= limit:  # 依條件輸出
    print(str(totalW) + "," + str(totalV))
else:
    print("-1")
