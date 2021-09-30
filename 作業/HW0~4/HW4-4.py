infoStr = input()
infoStr = infoStr.split(',')
NUM = int(infoStr[0])  # 標的個數
LIMIT = int(infoStr[1])  # 總資金限制
COEF = int(infoStr[2])  # 風險趨避指數

cost = []  # 投資各標地所需花的資金

costStr = input()
costStr = costStr.split(',')
for i in range(NUM):
    cost.append(int(costStr[i]))
# 讀取花費資金並貼到list

value = []  # 投資各標地的預期報酬
valueStr = input()
valueStr = valueStr.split(',')
for i in range(NUM):
    value.append(int(valueStr[i]))
# 讀取報酬並貼到list

var = [[0] * NUM for i in range(NUM)]  # 儲存變異數和共變數的list

for i in range(NUM):
    varStr = input()
    varStr = varStr.split(',')
    for j in range(NUM):
        var[i][j] = int(varStr[j])
# 讀取變異數和共變數並貼到list
"""
檢查點
print(cost)
print(value)
print(var)
"""

ans = []  # 已選擇的投資標的
totalCost = 0  # 已花費資金
maxResult = 0  # 目標式的最大結果
maxResult_code = 0  # 使目標式最大的投資標的

while totalCost < LIMIT:  # 當總資金沒超過
    for i in range(NUM):  # 找答案的for
        if (i not in ans) and cost[i] + totalCost <= LIMIT:  # 符合條件才能進來比
            risk = var[i][i]  # 先將risk宣告為自己的變異數

            if len(ans) > 0:
                for j in ans:
                    risk += var[i][j] * 2  # 因為矩陣是對稱的所以直接乘2

            result = value[i] - (COEF*risk)  # 算目標式結果
            if result > maxResult:  # 比大小
                maxResult = result
                maxResult_code = i
            elif result == maxResult:  # 目標式結果平手的情況
                if cost[i] < cost[maxResult_code]:
                    maxResult = result
                    maxResult_code = i
                    # 報酬相同，比花費。花費再相同則取編號小的所以用 < 而非 <=

    if maxResult != 0:  # 檢查是否為特殊情況
        totalCost += cost[maxResult_code]
        ans.append(maxResult_code)
        maxResult = 0
        maxResult_code = 0
    else:
        break
        """
        特殊情況:總資金沒超過的情況下所有物品都會讓總資金爆掉
        找不到適合的解但迴圈還是一直跑，就不要再找了
        """

if len(ans) > 0:  # 若投資標的個數 > 0
    ans.sort()  # 排序編號
    for i in ans:
        if i != ans[-1]:
            print(i + 1, end=",")
        else:
            print(i + 1)
else:  # 沒選任何標的
    print(0)
