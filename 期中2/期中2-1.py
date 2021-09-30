def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))


def plotmirror(linelist, horv="h", loc=0):
    mirrorL = []

    for line in linelist:
        new_mirror_L =[]
        if horv == 'h':  # 對y = loc的直線做鏡射
            new_mirror_L.append(line[0])

            diff = loc - line[1]
            line[1] += 2 * diff
            new_mirror_L.append(line[1])

            new_mirror_L.append(line[2])

            diff = loc - line[3]
            line[3] += 2 * diff
            new_mirror_L.append(line[3])
        else:  # 對x = loc的直線做鏡射
            diff = loc - line[0]
            line[0] += 2 * diff
            new_mirror_L.append(line[0])

            new_mirror_L.append(line[1])

            diff = loc - line[2]
            line[2] += 2 * diff
            new_mirror_L.append(line[2])

            new_mirror_L.append(line[3])
        mirrorL.append(new_mirror_L)
    return mirrorL


lines = []  # 儲存線段
while True:  # 讀取線段
    newLStr = input()
    if newLStr == "LINESTOP":
        break

    newL = [float(j) for j in newLStr.split(',')]
    lines.append(newL)

mirrorStr = input().split(',')
HORV = mirrorStr[0]
LOC = float(mirrorStr[1])

mirrored_lines = plotmirror(lines, HORV, LOC)
printlines(mirrored_lines)
