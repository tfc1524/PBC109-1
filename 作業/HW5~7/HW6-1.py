keyw = input()  # 關鍵詞
org_article = str()  # 文章

while True:  # 讀入文句與處理文章
    inStr = input()
    inStr = inStr.strip()
    if inStr == "INPUT_END":
        org_article = org_article.strip()
        break

    org_article += inStr + " "

counter_article = org_article  # counter為縮小後的，新的搜尋範圍
last_end = 0  # 上個關鍵字結尾的index
highlight = "**" + keyw + "**"  # 標註
ansList = []  # 儲存答案的list

if len(keyw) > 1:
    while True:
        if len(keyw) == len(org_article):  # 關鍵詞和文章完全相同的情況
            if keyw == org_article:
                ansList.append(highlight)
                break
            else:
                break

        start_index = counter_article.find(keyw)
        # 在搜尋範圍中，關鍵詞的第一個字出現的位置
        if start_index == -1:  # 沒找到任何相符的字串
            break

        if len(ansList) != 0:
            start_index += last_end  # 將start_index從搜尋範圍的位置 轉為 原文中的位置
            end_index = start_index + len(keyw) - 1  # 原文中關鍵詞結束的index
        else:  # 若為第一次搜尋，則不用轉換start_index的位置
            end_index = start_index + len(keyw) - 1

        floor = start_index - 7  # 要擷取的開頭(地板)
        ceiling = end_index + 7  # 要擷取的結尾(天花板)

        if floor < 0:  # 避免地板超出文章範圍
            floor = 0

        if ceiling > len(org_article) - 1:  # 避免天花板超出文章範圍
            ceiling = len(org_article) - 1
        """
        去研究一下這個巢狀if-else能不能寫更好
        """
        if floor == start_index:
            if ceiling == end_index:  # floor和ceiling都和關鍵字重疊
                new_ans = org_article[floor:start_index] + highlight + org_article[(end_index + 1):(ceiling + 2)]
            else:  # floor重疊ceiling沒重疊
                new_ans = org_article[floor:start_index] + highlight + org_article[(end_index + 1): (ceiling + 1)]
        else:  # floor沒重疊ceiling不知道
            new_ans = org_article[floor:start_index] + highlight + org_article[(end_index + 1): (ceiling + 1)]

        ansList.append(new_ans)  # 貼上答案

        counter_article = org_article[end_index:]  # 縮小搜尋範圍
        last_end = end_index  # 紀錄這次找到的在原文中關鍵詞結束的位置
else:
    while True:
        if len(keyw) == len(org_article):  # 關鍵詞和文章完全相同的情況
            if keyw == org_article:
                ansList.append(highlight)
                break
            else:
                break

        start_index = counter_article.find(keyw)
        # 在搜尋範圍中，關鍵詞的第一個字出現的位置

        if start_index == -1:  # 沒找到任何相符的字串
            break

        if len(ansList) != 0:
            start_index += last_end  # 將start_index從搜尋範圍的位置 轉為 原文中的位置
            end_index = start_index  # 原文中關鍵詞結束的index
        else:  # 若為第一次搜尋，則不用轉換start_index的位置
            end_index = start_index

        floor = start_index - 7  # 要擷取的開頭(地板)
        ceiling = end_index + 7  # 要擷取的結尾(天花板)

        if floor < 0:  # 避免地板超出文章範圍
            floor = 0

        if ceiling > len(org_article) - 1:  # 避免天花板超出文章範圍
            ceiling = len(org_article) - 1

        if floor == start_index:
            if ceiling == end_index:
                new_ans = org_article[floor:start_index] + highlight + org_article[(end_index + 1): (ceiling + 2)]
            else:
                new_ans = org_article[floor:start_index] + highlight + org_article[(end_index + 1): (ceiling + 1)]
        else:
            new_ans = org_article[floor:start_index] + highlight + org_article[(end_index + 1): (ceiling + 1)]

        ansList.append(new_ans)  # 貼上答案

        counter_article = org_article[end_index + 1:]  # 縮小搜尋範圍
        last_end = end_index + 1  # 紀錄這次找到的在原文中關鍵詞結束的位置

if len(ansList) != 0:  # 依據條件輸出
    for ans in ansList:
        print(ans)
else:
    print("NO_MATCH")
