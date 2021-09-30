info = input().split(';')
num = int(info[0])  # 人數
weight = [float(j) for j in info[1].split(',')]  # 加權

# 將比較高的權重放前面
if weight[2] > weight[1]:
    temp = weight[1]
    weight[1] = weight[2]
    weight[2] = temp

titles = input().split(',')

# 分別裝第0~4欄
col0 = []
col1 = []
col2 = []
col3 = []
col4 = []

for i in range(num):
    studentStr = input().split(',')
    col0.append(float(studentStr[0]))
    col1.append(float(studentStr[1]))
    col2.append(float(studentStr[2]))
    col3.append(float(studentStr[3]))
    col4.append(float(studentStr[4]))

cols = [col0, col1, col2, col3, col4]

student = dict()
for title in range(len(titles)):
    student[titles[title]] = cols[title]

max_t_score = 0.0
max_id = 9999999

for stu in range(num):
    t_score = float()
    t_score += student['HW'][stu] * weight[0] + student['F'][stu] * weight[3]

    if student['MT1'][stu] >= student['MT2'][stu]:
        t_score += student['MT1'][stu] * weight[1] + student['MT2'][stu] * weight[2]
    else:
        t_score += student['MT2'][stu] * weight[1] + student['MT1'][stu] * weight[2]

    if t_score > max_t_score:
        max_id = student['ID'][stu]
        max_t_score = t_score
    elif t_score == max_t_score:
        if student['ID'][stu] < max_id:  # 分數相同取編號小
            max_id = student['ID'][stu]
            max_t_score = t_score

print(int(max_id), int(max_t_score/100.0), sep=',')
