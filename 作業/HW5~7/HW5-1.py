def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))


def plotshift(linelist, xshift=0.0, yshift=0.0):
    for i in range(len(linelist)):
        linelist[i][0] += xshift
        linelist[i][2] += xshift
        linelist[i][1] += yshift
        linelist[i][3] += yshift

    return linelist

line = []  # 儲存線段

while True:  # 讀取線段
    inStr = input()
    if inStr == "LINESTOP":
        break

    plus = [float(j) for j in inStr.split(',')]
    line.append(plus)

shift = [float(i) for i in input().split(',')]  # 讀取平移量，依序為x平移和y平移

printlines(plotshift(line, shift[0], shift[1]))  # 平移並輸出
