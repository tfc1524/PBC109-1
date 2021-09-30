def newscut(all_com, all_keyw, all_news):
    all_keyw.sort(key=lambda s: len(s), reverse=True)  # 將關鍵字依長短排序

    newsansList = []  # 新聞答案(已用斜線分隔)
    comp_num = [[i]for i in range(len(all_com))]
    # 各公司在各新聞標題出現的次數，第一項為公司index，後續為各新聞中的出現次數

    for news in all_news:  # for跑所有新聞

        check_com = []  # 此新聞中各公司出現次數
        for comp in all_com:  # for 跑所有公司
            check_com.append(news.count(comp))  # 算出現次數並貼到check_com

        for i in range(len(all_com)):  # 將此次新聞出現次數貼到comp_num
            for j in range(len(check_com)):
                if i == j:  # 相對應的公司
                    comp_num[i].append(check_com[j])

        if sum(check_com) == 0:  # 若欲關注公司都沒出現
            newsansList.append('NO_MATCH')
            continue  # 跑下一則新聞

        keyw_index = []  # 有出現的關鍵字的長度、起始位置、結束位置+1

        for keyw in all_keyw:  # for 跑所有關鍵字
            temp = news  # 換一個新關鍵字就要把暫時文重置
            while True:
                start = temp.find(keyw)

                if start == -1:  # 沒找到關鍵字
                    break

                attribute = [0] * 3  # 分別儲存關鍵字的長度，出現位置，結束位置+1
                attribute[0] = len(keyw)
                attribute[1] = start
                attribute[2] = start + len(keyw)

                keyw_index.append(attribute)  # 把新發現貼到keyw_index
                temp = temp[0: start] + "%" * len(keyw) + temp[attribute[2]:]

        keyw_index = sorted(keyw_index, key=lambda s: s[1])
        # 將keyw_index依據出現順序排序

        for i in range(len(keyw_index)):  # i 是keyw_index的 index(會跑每一項)
            for j in range(i + 1, len(keyw_index)):  # j 從 i 的下一項開始跑(只跟i後面的比)
                if keyw_index[i][2] > keyw_index[j][1]:  # i和j重疊到
                    if keyw_index[j][0] > keyw_index[i][0]:
                        # 後面長度比前面長度大(排序較後的關鍵字能贏的唯一情況)
                        keyw_index[i][0] = -1
                        keyw_index[i][1] = 0
                        keyw_index[i][2] = 0
                    else:
                        # 排序較前的關鍵字贏了
                        keyw_index[j][0] = -1
                        keyw_index[j][1] = 0
                        keyw_index[j][2] = 0

        keyw_index_ans = []  # 等等用來slicing ans用
        for i in range(len(keyw_index)):
            if keyw_index[i][0] != -1:
                keyw_index_ans.append(keyw_index[i])

        new_ans = str()  # 此新聞的答案
        for i in range(len(keyw_index_ans)):
            if i == 0:
                if news[0: keyw_index_ans[i][1]] != "":
                    new_ans += news[0: keyw_index_ans[i][1]] + "/"
                if news[keyw_index_ans[i][1]: keyw_index_ans[i][2]] != "":
                    new_ans += news[keyw_index_ans[i][1]: keyw_index_ans[i][2]] + "/"
                if len(keyw_index_ans) == 1:  # 若只抓到一個關鍵字
                    if news[keyw_index_ans[i][2]:] != "":  # 最後一段
                        new_ans += news[keyw_index_ans[i][2]:]

            elif i == len(keyw_index_ans) - 1:  # 後面要小心有空字串變成一項，輸出//這種情況
                if news[keyw_index_ans[i - 1][2]: keyw_index_ans[i][1]] != "":
                    new_ans += news[keyw_index_ans[i - 1][2]: keyw_index_ans[i][1]] + "/"
                if news[keyw_index_ans[i][1]: keyw_index_ans[i][2]] != "":
                    new_ans += news[keyw_index_ans[i][1]: keyw_index_ans[i][2]] + "/"
                if news[keyw_index_ans[i][2]:] != "":  # 最後一段
                    new_ans += news[keyw_index_ans[i][2]:]

            else:
                if news[keyw_index_ans[i - 1][2]: keyw_index_ans[i][1]] != "":
                    new_ans += news[keyw_index_ans[i - 1][2]: keyw_index_ans[i][1]] + "/"
                if news[keyw_index_ans[i][1]: keyw_index_ans[i][2]] != "":
                    new_ans += news[keyw_index_ans[i][1]: keyw_index_ans[i][2]] + "/"
        new_ans = new_ans.strip('/')  # 去除多餘斜線
        newsansList.append(new_ans)  # 紀錄答案後進入下一則新聞

    processed_title = []
    for k in range(len(all_news)):
        comp_num = sorted(comp_num, key=lambda com: com[0])
        # 先排公司輸入順序(次要條件)
        comp_num = sorted(comp_num, key=lambda com: com[k+1], reverse=True)
        # 後排出現次數(主要條件)
        comp_ans = str()  # 公司面答案
        final_ans = str()  # 最終答岸

        for j in range(len(comp_num)):
            if comp_num[j][k + 1] != 0:  # 若公司有出現
                comp_ans += all_com[comp_num[j][0]] + ","  # 則把公司名放到答案裡面

        comp_ans = comp_ans.strip(',')  # 把多餘逗號去掉

        if newsansList[k] != 'NO_MATCH':  # 如果關注公司有出現
            final_ans = comp_ans + ";" + newsansList[k]
            # 輸出公司名和處理過的新聞內容
        else:
            final_ans = comp_ans + ";" + newsansList[k]

        processed_title.append(final_ans)
    return processed_title


def buyprocess(distri, company, limit):
    while True:
        for i in range(len(distri)):
            if distri[i] >= limit:
                company[i][2] += limit
                limit = 0
                return company
            elif distri[i] < limit:
                company[i][2] += distri[i]
                limit -= distri[i]
    return company

news_title_filename = input()
keyw_dict_filename = input()
category_filename = input()
portfolio = input()  # 產業類別、 總張數、分配方式
portfolio = portfolio.split(',')

industry = portfolio[0]  # 欲關注產業類別
total_buynum = int(portfolio[1])  # 總購買張數
distribution = [int(j) for j in portfolio[2].split(':')]  # 分配張數

category = dict()  # key是類別，value為list，裡面存著一個個字串(公司)
with open(file=category_filename, mode='r', encoding='utf-8') as cateFile:
    for line in cateFile:
        line = line.split()
        if line[1] in category:
            category[line[1]].append(line[0])
        else:
            category[line[1]] = [line[0]]

keyw_weight = dict()  # key為關鍵字(str), value為加權分(int)
keyw_list = []  # 關鍵字List，等等6-3的函數要用
with open(file=keyw_dict_filename, mode='r', encoding='utf-8') as keywFile:
    for line in keywFile:
        line = line.split()
        keyw_weight[line[0]] = int(line[1])
        keyw_list.append(line[0])

org_newstitle = []  # 原始新聞標題
# 把原始新聞標題放進list
with open(file=news_title_filename, mode='r', encoding='utf-8') as newsFile:
    for line in newsFile:
        line = line.replace(" ", "")
        line = line.strip()
        org_newstitle.append(line)

if industry in category:
    focus_com = category[industry]  # 欲關注公司list

    totalscore_com = []
    for i in range(len(focus_com)):
        totalscore_com.append([focus_com[i], 0, 0])
        # 0:公司名稱 1:分數 2:購買張數

    com_and_processednews = newscut(focus_com, keyw_list, org_newstitle)
    # 處理成6-3 答案的格式

    for c_pn in com_and_processednews:
        c_pn = c_pn.split(';')
        if c_pn[1] != 'NO_MATCH':
            company = c_pn[0].split(',')
            piece = c_pn[1].split('/')
            score = 0  # 此標題分數

            # 計算此標題分數
            for j in range(len(piece)):
                if piece[j] in keyw_list:
                    score += keyw_weight[piece[j]]

            for k in range(len(company)):  # 此則新聞提到的公司
                for j in range(len(focus_com)):  # 所有公司
                    # 將該公司的分數加上此標題的分數
                    if totalscore_com[j][0] == company[k]:
                        totalscore_com[j][1] += score
    # 依條件排序
    totalscore_com = sorted(totalscore_com, reverse=True, key=lambda s: (s[1], s[0]))

    # 決定分配股票方法
    dist_num = min(len(distribution), len(totalscore_com))
    distribution = distribution[: dist_num]

    # 購買流程
    totalscore_com = buyprocess(distribution, totalscore_com, total_buynum)

    # 根據條件輸出
    for i in range(len(totalscore_com)):
        if totalscore_com[i][2] != 0:
            ans = totalscore_com[i][0] + "購買" + str(totalscore_com[i][2]) + "張"
            print(ans)
else:
    print('NO_MATCH')
