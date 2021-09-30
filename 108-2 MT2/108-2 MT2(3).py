num = int(input())
costmatrix = []  # 成本矩陣

for i in range(num):
    new_employeeStr = input().split(',')
    new_employee = [int(j) for j in new_employeeStr]
    costmatrix.append(new_employee)

matched = dict()  # 配對好的員工和工作
mincost = 999999999
matched_emp = 999999
matched_work = 999999
total_cost = 0
match_e_list = []  # 已配對的員工
match_w_list = []  # 已配對的工作

for time in range(num):
    for i in range(num):
        for j in range(num):
            if i + 1 not in match_e_list and j + 1 not in match_w_list:
                if costmatrix[i][j] < mincost:
                    mincost = costmatrix[i][j]
                    matched_emp = i + 1
                    matched_work = j + 1
                elif costmatrix[i][j] == mincost:
                    if (i + j + 2) < (matched_emp + matched_work):
                        mincost = costmatrix[i][j]
                        matched_emp = i + 1
                        matched_work = j + 1
                    elif (i + j + 2) == (matched_emp + matched_work):
                        if (i + 1) < matched_emp:
                            mincost = costmatrix[i][j]
                            matched_emp = i + 1
                            matched_work = j + 1

    match_e_list.append(matched_emp)
    match_w_list.append(matched_work)

    matched[matched_emp] = matched_work
    total_cost += mincost

    mincost = 99999999
    matched_emp = 999999
    matched_work = 999999

for k in range(1, num + 1):
    print(matched[k], end=',') if k < num else print(matched[k], end=';')

print(total_cost)
