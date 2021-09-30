# 生產安排任務分配
# read and prepare n , m , and p
n = int(input("Number of jobs:"))
m = int(input("Number of machines:"))
pStr = input("Processing time:")

p = pStr.split(' ')
for i in range(n):
    p[i] = int(p[i])

# machine completion time *m*n是要創造出幾個為0的格子
loads = [0] * m
assignment = [0] * n

# in iteration j , assign job j to the least loaded machine
for j in range(n):

    # find the least loaded machine 先假設是第0台，一直比到m-1台
    leastLoadedMachine = 0
    leastLoad = loads[0]
    for i in range(1, m):
        if loads[i] < leastLoad:
            leastLoadedMachine = i
            leastLoad = loads[i]

    # schedule a job
    loads[leastLoadedMachine] += p[j]
    assignment[j] = leastLoadedMachine + 1

# the result
print("Job assignment: " + str(assignment))
print("Machine loads:" + str(loads))
