import math  # 引入套件


def printlines(linelist):  # 輸出指定格式的函數
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))


def rotate(lines, degree=90):  # 旋轉的函數，為何不能跟第一題一樣的做法?
    line_2 = []  # 存旋轉過後的線

    for i in range(len(lines)):  # for把每個點都旋轉
        plus = [0] * 4  # 用來儲存旋轉過後的點的list
        plus[0] = lines[i][0]*math.cos(degree*2*math.pi/360) - lines[i][1]*math.sin(degree*2*math.pi/360)
        plus[1] = lines[i][0]*math.sin(degree*2*math.pi/360) + lines[i][1]*math.cos(degree*2*math.pi/360)

        plus[2] = lines[i][2]*math.cos(degree*2*math.pi/360) - lines[i][3]*math.sin(degree*2*math.pi/360)
        plus[3] = lines[i][2]*math.sin(degree*2*math.pi/360) + lines[i][3]*math.cos(degree*2*math.pi/360)
        # 運算過程

        line_2.append(plus)  # 貼到list中

    return line_2

line = []  # 儲存題目給的線段

while True:  # 讀取線段
    inStr = input()
    if inStr == "LINESTOP":  # 如果讀到這個訊息就中斷迴圈
        break

    new = [float(j) for j in inStr.split(',')]  # 新讀到的線
    line.append(new)  # 貼到list中

deg = float(input())  # 旋轉度數

line_ans = rotate(line, degree=deg)  # 答案

printlines(line_ans)  # 輸出答案
