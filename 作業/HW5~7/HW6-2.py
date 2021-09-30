MAX_INTERVAL = int(input())
keyw1 = input()
keyw2 = input()
org_article = str()  # 文章

while True:  # 讀入文句與處理文章
    inStr = input()
    inStr = inStr.strip()
    if inStr == "INPUT_END":
        org_article = org_article.strip()
        break

    org_article += inStr + " "

counter_article1 = org_article  # 關鍵字一的搜尋範圍
counter_article2 = org_article  # 關鍵字二的搜尋範圍
highlight1 = "**" + keyw1 + "**"  # highlight關鍵字一
highlight2 = "**" + keyw2 + "**"  # highlight關鍵字二
last_end = 0
ansList = []

if len(keyw1) > 1:
    while True:
        start_index1 = counter_article1.find(keyw1)

        if start_index1 == -1:
            break

        start_index1 += last_end  # 將start_index從搜尋範圍的位置 轉為 原文中的位置
        end_index1 = start_index1 + len(keyw1) - 1  # 原文中關鍵詞1結束的index

        counter_article2 = org_article[end_index1 + 1: end_index1 + MAX_INTERVAL + len(keyw2) + 1]
        # 找到關鍵詞一後，向他後面固定長度尋找關鍵詞二
        while True:
            start_index2 = counter_article2.find(keyw2)

            if start_index2 == -1:
                break

            start_index2 += end_index1 + 1
            end_index2 = start_index2 + len(keyw2) - 1

            floor = start_index1 - 7  # 要擷取的開頭(地板)
            ceiling = end_index2 + 7  # 要擷取的結尾(天花板)
            if floor < 0:  # 避免地板超出文章範圍
                floor = 0

            if ceiling > len(org_article) - 1:  # 避免天花板超出文章範圍
                ceiling = len(org_article) - 1

            new_ans = org_article[floor: start_index1] + highlight1 + org_article[end_index1 + 1: start_index2] + highlight2 + org_article[end_index2 + 1: ceiling + 1]
            ansList.append(new_ans)

            counter_article2 = org_article[end_index1 + 1: start_index2] + "%" * len(keyw2) + org_article[end_index2 + 1:  end_index1 + MAX_INTERVAL + len(keyw2) + 1]
            # 將這次找到的關鍵字在搜尋範圍中替換成%，下次就不會重複找到


        counter_article1 = org_article[end_index1:]  # 縮小關鍵字一的搜尋範圍
        last_end = end_index1  # 紀錄上次找到關鍵字一的位置

if len(ansList) != 0:  # 依據條件輸出
    for ans in ansList:
        print(ans)
else:
    print("NO_MATCH")
