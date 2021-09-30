numStr = input()
# 讀取輸入數字
if len(numStr) == 1:
    numStr += "00"
elif len(numStr) == 2:
    numStr += "0"
# 不足三位數補0

# 決定三個位數的大小
for i in range(0, 3):
    hun = int(numStr[0])
    ten = int(numStr[1])
    dig = int(numStr[2])
    # 讀取三個位數

    if hun > ten:
        if hun > dig:
            if ten > dig:
                max = hun
                med = ten
                min = dig
            else:
                max = hun
                med = dig
                min = ten
        else:
            max = dig
            med = hun
            min = ten

    elif ten > dig:
        if hun > dig:
            max = ten
            med = hun
            min = dig
        else:
            max = ten
            med = dig
            min = hun
    else:
        max = dig
        med = ten
        min = hun

    bigger = int(str(max) + str(med) + str(min))
    smaller = int(str(min) + str(med) + str(max))
    # 將數字由大排到小和由小排到大，組成新的數字

    num = bigger - smaller
    #  大的減小的

    if i < 2:
        print(num, end=',')
    else:
        print(num)
    # 輸出num

    if num < 10:
        num *= 100
    elif 10 <= num < 100:
        num *= 10
    else:
        num *= 1
    # 不足三位數，補0

    numStr = str(num)
    # 轉回字串形式以便執行下一次操作
