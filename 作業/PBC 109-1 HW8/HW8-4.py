import csv, datetime
import matplotlib.pyplot as plt
import numpy as np

class Submission:
    def __init__(self, challenge, problem, status, daysafterstart):
        self.challenge = str(challenge)
        self.problem = int(problem)  # 小題
        self.status = str(status)  # 狀態
        self.daysafterstart = int(daysafterstart)  # 自開始過了幾天


# 各次challenge開始時間
starttime = {
'PBC 109-1 HW0': datetime.datetime.strptime('2020-09-14 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW1': datetime.datetime.strptime('2020-09-21 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW2': datetime.datetime.strptime('2020-09-28 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW3': datetime.datetime.strptime('2020-10-05 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW4': datetime.datetime.strptime('2020-10-12 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW5': datetime.datetime.strptime('2020-10-26 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW6': datetime.datetime.strptime('2020-11-02 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW7': datetime.datetime.strptime('2020-11-09 21:00:00', '%Y-%m-%d %H:%M:%S')
}

# 各次challenge結束時間
endtime = {
'PBC 109-1 HW0': datetime.datetime.strptime('2020-09-21 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW1': datetime.datetime.strptime('2020-09-28 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW2': datetime.datetime.strptime('2020-10-05 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW3': datetime.datetime.strptime('2020-10-16 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW4': datetime.datetime.strptime('2020-10-26 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW5': datetime.datetime.strptime('2020-11-04 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW6': datetime.datetime.strptime('2020-11-09 21:00:00', '%Y-%m-%d %H:%M:%S'),
'PBC 109-1 HW7': datetime.datetime.strptime('2020-11-21 21:00:00', '%Y-%m-%d %H:%M:%S')
}

# 各次challenge題數
problemnum = {
'PBC 109-1 HW0': 1, 'PBC 109-1 HW1': 4, 'PBC 109-1 HW2': 4, 'PBC 109-1 HW3': 4,
'PBC 109-1 HW4': 4, 'PBC 109-1 HW5': 3, 'PBC 109-1 HW6': 3, 'PBC 109-1 HW7': 3}

filename = 'C:\\Users\\jack\\business_program\\作業\\PBC 109-1 HW8\\HW8-4\\submission_complete.csv'
challenges = dict()

with open(file=filename, mode='r', encoding='utf-8') as f:
    fh = csv.DictReader(f)

    for row in fh:
        problemno = row['problem'][5: 6]  # 第幾個問題
        subtime = datetime.datetime.strptime(row['submit_time'][: -2], '%Y-%m-%d %H:%M:%S')
        # 繳交時間
        diff = subtime - starttime[row['challenge']]  # 距離開放作答時長
        subinfo = Submission(row['challenge'], problemno, row['status'], diff.days)
        # 此次繳交(物件)

        this_sub = [subinfo.problem, subinfo.status, subinfo.daysafterstart]
        # 要append到challenge字典內的list

        if starttime[subinfo.challenge] <= subtime <= endtime[subinfo.challenge]:
            if row['challenge'] not in challenges:
                challenges[row['challenge']] = [this_sub]
            else:
                challenges[row['challenge']].append(this_sub)

clg_attempt = []  # 各次challange的平均每題繳交次數
clg_actimes = []  # 各次challenge 平均每題AC 數
clg_acratio = []  # 各次challenge AC占總繳交次數比例
clg_peopleactimes = []  # 各次challenge 平均每人每題AC數

for clg in challenges:
    clg_attempt.append(int(len(challenges[clg]) / problemnum[clg]))

    ac_num = 0
    for sub in challenges[clg]:
        if sub[1] == 'Accepted':
            ac_num += 1
    clg_actimes.append(int(ac_num / problemnum[clg]))
    # 此challenge平均每題ac數
    clg_peopleactimes.append(ac_num / (problemnum[clg] * 1000))

    clg_acratio.append(ac_num / len(challenges[clg]))
    # 此challenge ac比例
print('各次challange 平均每題繳交次數', clg_attempt, sep=':')
print('各次challenge 平均每題AC 數', clg_actimes, sep=':')
print('各次challenge 平均每人每題AC數', clg_peopleactimes, sep=':')
print('各次challenge AC占總繳交次數比例', clg_acratio, sep=':')

pbm_attempt = []  # 各problem的平均每題繳交次數
pbm_actimes = []  # 各problem 平均每題AC 數
pbm_acratio = []  # 各problem AC占總繳交次數比例

for clg in challenges:
    pbmnum = problemnum[clg]  # 此challenge的題目數
    this_attempt = []
    this_actimes = []
    this_acratio = []

    for pbm in range(1, pbmnum + 1):
        ac_num = 0
        atmpt_num = 0

        for sub in challenges[clg]:  # 跑該clg每筆繳交紀錄
            if sub[0] == pbm:
                atmpt_num += 1
                if sub[1] == 'Accepted':
                    ac_num += 1

        this_attempt.append(atmpt_num)
        this_actimes.append(ac_num)
        this_acratio.append(ac_num / atmpt_num)

    pbm_attempt.append(this_attempt)
    pbm_actimes.append(this_actimes)
    pbm_acratio.append(this_acratio)

print('各problem繳交次數', pbm_attempt, sep=':')
print('各problem AC次數', pbm_actimes, sep=':')

for clg in range(len(pbm_acratio)):
    for pbm in range(len(pbm_acratio[clg])):
        print('{}-{}: {:.3}'.format(clg, pbm + 1, pbm_acratio[clg][pbm]))

pbm1_acratio = [pbm_acratio[k][0] for k in range(5, 8)]
pbm2_acratio = [pbm_acratio[k][1] for k in range(5, 8)]
pbm3_acratio = [pbm_acratio[k][2] for k in range(5, 8)]

width = 0.25
x1 = [5, 6, 7]
x2 = [p + width for p in x1]
x3 = [p + 2 * width for p in x1]
plt.bar(x1, pbm1_acratio, color='tab:green', width=0.25, label='Problem 1', alpha=0.7)
plt.bar(x2, pbm2_acratio, color='tab:orange', width=0.25, label='Problem 2', alpha=0.7)
plt.bar(x3, pbm3_acratio, color='tab:olive', width=0.25, label='Problem 3', alpha=0.7)
plt.legend(loc='upper right')
plt.xlabel('Challenges')
plt.ylabel('AC Rate')
plt.title('AC Rate(Challenge 5~7)')
plt.ylim(0, 0.7)
plt.yticks(np.arange(0, 0.75, 0.05))
plt.xticks([p + width for p in x1], x1)
plt.show()
