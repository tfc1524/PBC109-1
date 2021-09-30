comStr = input()
all_com = [j for j in comStr.split(',')]  # 公司list

keywStr = input()
all_keyw = [j for j in keywStr.split(',')]  # 關鍵字list
all_keyw.sort(key=lambda s: len(s), reverse=True)  # 將關鍵字依長短排序

all_news = []  # 新聞標題list

while True:
    inStr = input()
    if inStr == 'INPUT_END':  # 讀到這個就停止讀入新聞標題
        break

    inStr = inStr.replace(" ", "")  # 把多餘空白去掉
    inStr = inStr.strip()  # 前後的空白去掉
    all_news.append(inStr)

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
        final_ans = newsansList[k]  # 只輸出NOMATCH

    print(final_ans)  # 輸出答案
