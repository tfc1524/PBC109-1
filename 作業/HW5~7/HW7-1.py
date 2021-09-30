import operator


def dictsort(dict1):
    list1_sorted = sorted(dict1.items(), key=operator.itemgetter(1, 0), reverse=True)
    # sorted完會返回一個list，裡面有很多個tuple
    return list1_sorted

filename = input()  # 檔案名稱
keyw = input()  # 關鍵字
sentence = []  # 裝所有句子
former_freq = dict()  # 前一個字的出現頻率
latter_freq = dict()  # 後一個字的出現頻率

with open(file=filename, mode='r', encoding='utf-8') as f:
    for line in f:  # 跑檔案中的每一行
        temp = line.split('\t')

        # 將句子去除空白和換行
        temp[0] = temp[0].strip()
        temp[1] = temp[1].strip()

        # 將句子貼到list中
        sentence.append(temp[0])
        sentence.append(temp[1])

    for i in range(len(sentence)):
        while True:
            start_index = sentence[i].find(keyw)  # 找關鍵字起始位置

            if start_index == -1:  # 找不到就找下一句
                break
            if start_index == 0 and start_index + len(keyw) - 1 == len(sentence[i]) - 1:
            # 整句只有關鍵字，前後文都不統計
                sentence[i] = sentence[i][: start_index] + '%' + sentence[i][start_index + 1:]
                continue
            elif start_index == 0:  # 關鍵字在句首，只統計後一個字
                next = sentence[i][start_index + len(keyw)]
                if next in latter_freq:
                    latter_freq[next] += 1
                else:
                    latter_freq[next] = 1

            elif start_index + len(keyw) - 1 == len(sentence[i]) - 1:
                # 若關鍵字在句尾，只統計前一個字
                last = sentence[i][start_index - 1]
                # 找關鍵字的前一個字並對dictionary做相應處理
                if last in former_freq:
                    former_freq[last] += 1
                else:
                    former_freq[last] = 1

            else:
                last = sentence[i][start_index - 1]
                # 找關鍵字的前一個字並對dictionary做相應處理
                if last in former_freq:
                    former_freq[last] += 1
                else:
                    former_freq[last] = 1

                next = sentence[i][start_index + len(keyw)]
                if next in latter_freq:
                    latter_freq[next] += 1
                else:
                    latter_freq[next] = 1

            sentence[i] = sentence[i][: start_index] + '%' + sentence[i][start_index + 1:]
            # 將sentence中的關鍵字取代掉
    # 排序後的前後文(型態為list，內容型態為tuple)
    former_rank = dictsort(former_freq)
    former_num = 10 if len(former_rank) >= 10 else len(former_rank)

    latter_rank = dictsort(latter_freq)
    latter_num = 10 if len(latter_rank) >= 10 else len(latter_rank)

    # 照指定格式輸出
    print('熱門前一個字:')
    for i in range(former_num):
        ans = former_rank[i][0] + "---" + keyw
        print(ans)

    print('熱門下一個字:')
    for j in range(latter_num):
        ans = keyw + '---' + latter_rank[j][0]
        print(ans)
