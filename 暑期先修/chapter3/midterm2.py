import csv, datetime

class Submission:
    def __init__(self, problem, status, secafterstart):
        self.problem = int(problem)
        self.status = str(status)
        self.secafterstart = int(secafterstart)


t0 = datetime.time(hour=9, minute=10, second=0)

timeStr = input().split()
starttime = datetime.datetime.strptime(timeStr[0], '%H:%M:%S').time()
td_start = datetime.datetime.combine(datetime.date.today(), starttime) - datetime.datetime.combine(datetime.date.today(), t0)
endtime = datetime.datetime.strptime(timeStr[1], '%H:%M:%S').time()
td_end = datetime.datetime.combine(datetime.date.today(), endtime) - datetime.datetime.combine(datetime.date.today(), t0)


filename = 'C:\\Users\\jack\\business_program\\暑期先修\\chapter3\\midterm2.csv'

status_code = {'Accepted' : 0, 'Compile Error' : 1, 'Runtime Error':2, 'Time Limit Exceed' : 3, 'Wrong Answer' : 4}
statistics = dict()  # 統計時間段內各題繳交情況

for i in range(1, 5):
    statistics[i] = [0] * 5

with open(file=filename, mode='r') as m2file:
    m2reader = csv.DictReader(m2file)
    sub = dict()

    for row in m2reader:
        t1 = datetime.datetime.strptime(row['SubmissionTime'], '%H:%M:%S').time()
        diff = datetime.datetime.combine(datetime.date.today(), t1) - datetime.datetime.combine(datetime.date.today(), t0)
        # subinfo = [int(row['Problem']), row['Status'], diff.seconds]
        this_subinfo = Submission(int(row['Problem']), row['Status'], diff.seconds)

        if td_start.seconds <= this_subinfo.secafterstart <= td_end.seconds:
            statistics[this_subinfo.problem][status_code[this_subinfo.status]] += 1
        # sub[row['SubmissionID']] = subinfo

ans = str()
for i in range(1, 5):
    for j in range(5):
        ans += str(statistics[i][j]) + " "

    ans = ans.strip()
    ans += ';'
print(ans)
