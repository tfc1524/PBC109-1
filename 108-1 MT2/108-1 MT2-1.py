info = input().split(';')
num = int(info[0])  # 人數
weight = [float(j) for j in info[1].split(',')]  # 加權

title = input()  # 標題

student = dict()  # key為學生編號，values為一個list代表各次成績
for i in range(num):
    studentStr = input().split(',')
    grades = [float(studentStr[k]) for k in range(1, 5)]
    student[int(studentStr[0])] = grades

max_t_score = 0.0
max_id = 9999999

for sid in student:
    t_score = float()
    for j in range(4):
        t_score += student[sid][j] * weight[j]

    if t_score > max_t_score:
        max_id = sid
        max_t_score = t_score
    elif t_score == max_t_score:
        if sid < max_id:  # 分數相同取編號小
            max_id = sid
            max_t_score = t_score

print(max_id, int(max_t_score/100.0), sep=',')
