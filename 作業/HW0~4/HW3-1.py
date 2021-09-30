numStr = input()
if len(numStr) == 1:
    numStr += "000"
elif len(numStr) == 2:
    numStr += "00"
elif len(numStr) == 3:
    numStr += "0"
# 不足四位數補0

answer = []  # 用來存答案的list
counter = 0  # 計算while迴圈的次數，print時用

if int(numStr) == 6174:  # 最特殊的情況
    print(int(numStr))

while int(numStr) != 6174:
    counter += 1
    bigList = sorted(numStr, reverse=True)  # 由大排到小
    smaList = sorted(numStr)

    bigger = int(bigList[0])*1000 + int(bigList[1])*100 + int(bigList[2])*10 + int(bigList[3])*1
    smaller = int(smaList[0])*1000 + int(smaList[1])*100 + int(smaList[2])*10 + int(smaList[3])*1

    num = bigger - smaller

    answer.append(num)

    numStr = str(num)

    if len(numStr) == 1:
        numStr += "000"
    elif len(numStr) == 2:
        numStr += "00"
    elif len(numStr) == 3:
        numStr += "0"
    # 不足四位數補0

for i in range(counter):
    if i < counter - 1:  # 為輸出指定格式而設的if判斷
        print(answer[i], end=",")
    else:
        print(answer[i])
