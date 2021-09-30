num = int(input())

xStr = input()
xStr = xStr.split(',')

x = []
for i in range(num):
    x.append(int(xStr[i]))
# 讀取x並做出list

y = []
for i in range(num -1):
    sum = x[i] - x[i + 1]

    if sum >= 0:
        y.append(sum)
    else:
        y.append(0)
# 算出y

result = min(y)

print(result)
