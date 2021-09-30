DOTNUM = int(input())
x_locStr = input()
y_locStr = input()

x_locStr = x_locStr.split(',')
y_locStr = y_locStr.split(',')

x_loc = []
y_loc = []

for i in range(DOTNUM):
    x_loc.append(int(x_locStr[i]))
    y_loc.append(int(y_locStr[i]))

# 存取xy座標

dst_x = [([0] * DOTNUM) for i in range(DOTNUM)]

for i in range(DOTNUM):
    for j in range(DOTNUM):
        dist = x_loc[i] - x_loc[j]
        if dist >= 0:
            dst_x[i][j] = dist
        else:
            dst_x[i][j] = -dist
# 算x差距

dst_y = [([0] * DOTNUM) for i in range(DOTNUM)]

for i in range(DOTNUM):
    for j in range(DOTNUM):
        dist = y_loc[i] - y_loc[j]
        if dist >= 0:
            dst_y[i][j] = dist
        else:
            dst_y[i][j] = -dist
# 算y差距

dst_xy = [([0] * DOTNUM) for i in range(DOTNUM)]

for i in range(DOTNUM):
    for j in range(DOTNUM):
        dist = dst_x[i][j] + dst_y[i][j]
        if dist >= 0:
            dst_xy[i][j] = dist
        else:
            dst_xy[i][j] = -dist
# 把xy差距加起來變總差距

for i in range(DOTNUM):
    for j in range(DOTNUM):
        if j < DOTNUM - 1:
            print(dst_xy[i][j], end=',')
        else:
            print(dst_xy[i][j])
# 輸出結果
