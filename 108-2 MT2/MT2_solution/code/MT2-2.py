
num, capacity = input().split(',')
num = int(num)
capacity = int(capacity)

offMRT = input().split(',')
onMRT = input().split(',')
for i in range(len(offMRT)):
    offMRT[i] = int(offMRT[i])
    onMRT[i] = int(onMRT[i])

people = 0
error = 0
for i in range(num):
    # 乘客下車
    people -= offMRT[i]
    # 發生錯誤，且之前沒發生過
    if(people < 0 and error == 0):
        error = 1

    # 乘客上車
    people += onMRT[i]
    # 發生錯誤，且之前沒發生過
    if(people > capacity and error == 0):
        error = 2

print(str(people) + ',' + str(error))
