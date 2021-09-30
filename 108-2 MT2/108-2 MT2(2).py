infoStr = input().split(',')
station = int(infoStr[0])  # 站數
limit = int(infoStr[1])  # 載客限制

offStr = input()
onStr = input()
off = [int(j) for j in offStr.split(',')]  # 各站下車人數
on = [int(j) for j in onStr.split(',')]  # 各站上車人數

onboard = 0  # 車上人數
error = []

for k in range(station):
    # 先檢查下車
    if off[k] > onboard:
        error.append(1)

    # 再檢查上車
    if onboard - off[k] + on[k] > limit:
        error.append(2)

    # 運算
    onboard = onboard - off[k] + on[k]

print(onboard, end=',')

print(0 if len(error) == 0 else error[0])
