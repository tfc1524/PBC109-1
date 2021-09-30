def player_avg(seasons, records, player_number):
    p_avg = float()
    atbat = int()
    hit = int()  # 打數 安打數
    for i in range(len(records)):  # 跑每一筆資料
        for j in seasons:  # 跑指定賽季
            if records[i][2] == j:  # 若賽季相符
                if records[i][1] == player_number:  # 若球員相符
                    atbat += records[i][3]  # 將打數和安打累加
                    hit += records[i][4]
    p_avg = hit / atbat  # 算出avg
    return p_avg


def team_avg(seasons, records, team_name):
    t_avg = float()
    atbat = int()
    hit = int()
    for i in range(len(records)):  # 跑每一筆資料
        for j in seasons:  # 跑指定賽季
            if records[i][2] == j:  # 若賽季相符
                if records[i][0] == team_name:  # 若球隊相符
                    atbat += records[i][3]  # 將打數和安打累加
                    hit += records[i][4]
    t_avg = hit / atbat  # 算出avg
    return t_avg


def best_player(seasons, records):
    bp = []  # 打擊王list
    for season in seasons:  # 找出每個球季打擊王
        max_avg = -1.0  # 最高打擊率
        best_p = 999  # 目前打擊王背號
        bp_atbat = 999  # 目前打擊王打數
        for j in range(len(records)):  # 跑每一筆球員資料
            if records[j][2] == season:  # 若年度相符
                avg = float()
                avg = (records[j][4] / records[j][3])  # 算打擊率
                if avg > max_avg:  # 若打擊率超過則取代
                    max_avg = avg
                    best_p = records[j][1]
                    bp_atbat = records[j][3]
                elif avg == max_avg:  # 若打擊率相等
                    if records[j][3] < bp_atbat:  # 比打數較小者獲勝
                        max_avg = avg
                        best_p = records[j][1]
                        bp_atbat = records[j][3]
                    elif records[j][3] == bp_atbat:  # 若打數相同
                        if records[j][1] < best_p:  # 比背號較小者獲勝
                            max_avg = avg
                            best_p = records[j][1]
                            bp_atbat = records[j][3]

        bp.append(best_p)  # 貼答案，在進行下一輪比較
    return bp


def best_team(seasons, records):
    bt = []  # 最佳球隊list
    for season in seasons:  # 找出每個球季最好球隊
        all_team = []  # 該年所有球隊list
        for k in range(len(records)):  # 找出該年所有球隊
            if records[k][0] not in all_team:
                if records[k][2] == season:
                    all_team.append(records[k][0])

        max_avg = -1.0  # 最高打擊率
        best_t = "default"  # 目前最好球隊
        bt_atbat = 999  # 目前最好球隊打數

        for team in all_team:  # 跑該年所有球隊
            atbat = int()  # 打數
            hit = int()  # 安打
            avg = float()  # 打擊率

            for j in range(len(records)):  # 跑每一筆球員資料
                if records[j][2] == season:  # 若年度相符
                    if records[j][0] == team:  # 若球隊相符
                        atbat += records[j][3]
                        hit += records[j][4]

            avg = (hit / atbat)

            if avg > max_avg:  # 若打擊率超過則取代
                max_avg = avg
                best_t = team
                bt_atbat = atbat
            elif avg == max_avg:  # 若相等
                if atbat < bt_atbat:  # 比打數較小者獲勝
                    max_avg = avg
                    best_t = team
                    bt_atbat = atbat
                elif atbat == bt_atbat:  # 打數又相等
                    if team < best_t:  # 比隊伍編號，排較前面者獲勝
                        max_avg = avg
                        best_t = team
                        bt_atbat = atbat
        bt.append(best_t)
    return bt


def chop(avg):  # 無條件捨去至小數第二位的函數
    avg = int(avg*100) / 100
    return avg if avg > 0 else 0
"""
函數定義結束，以下為
讀取資料及輸出資料
"""
record = []
while True:
    infoStr = input()
    if infoStr == 'RECORDSTOP':  # 接收到這個指令就跳出迴圈
        break

    new = []  # 裝新資料的list
    infoStr = infoStr.split(',')

    for i in range(len(infoStr)):  # 將新資料裝到list中
        if i > 0:
            new.append(int(infoStr[i]))
        else:
            new.append(infoStr[i])

    record.append(new)

function = []  # 存題目要求的list
while True:
    inStr = input()
    if inStr == 'FUNCTIONSTOP':  # 接收到這個指令就跳出迴圈
        break

    inStr = inStr.split()
    mode = int(inStr[0])  # 模式(用哪個函數)
    season_giveStr = inStr[1]  # 球季
    season_giveStr = season_giveStr.split(',')
    season_give = []
    for i in season_giveStr:
        season_give.append(int(i))

    plus = []  # 欲新增的要求
    plus.append(mode)
    plus.append(season_give)

    # 有時會有三項，有時只有兩項，因此設條件式判別
    if mode == 1:
        player = int(inStr[2])
        plus.append(player)
    elif mode == 2:
        team = inStr[2]
        plus.append(team)

    function.append(plus)  # 貼到function後，接受下一句要求

for i in range(len(function)):  # 根據每行題目要求使用不同的函數
    if function[i][0] == 1:  # 即mode = 1
        value = player_avg(function[i][1], record, function[i][2])
        # 依序傳入所求球季、紀錄、背號
        ans = chop(value)
        print(ans)
    elif function[i][0] == 2:  # 即mode = 2
        value = team_avg(function[i][1], record, function[i][2])
        # 依序傳入所求球季、紀錄、球隊名
        ans = chop(value)
        print(ans)
    elif function[i][0] == 3:  # 即mode = 3
        ansList = best_player(function[i][1], record)
        for i in range(len(ansList)):
            if i != (len(ansList) - 1):  # 根據題目要求輸出
                print(ansList[i], end=',')
            else:
                print(ansList[i])
    elif function[i][0] == 4:  # 即mode = 4
        ansList = best_team(function[i][1], record)
        for i in range(len(ansList)):
            if i != (len(ansList) - 1):  # 根據題目要求輸出
                print(ansList[i], end=',')
            else:
                print(ansList[i])
