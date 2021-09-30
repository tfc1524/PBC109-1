item_filename = input()
genre_filename = input()
search_id = int(input())

genre = dict()  # 儲存類別代碼對應的類別

# 將類別資訊從檔案中存到list中
with open(file=genre_filename, mode='r', encoding='ISO-8859-1') as gen:
    for line in gen:
        if line != '\n':
            line = line.split('|')
            genre[int(line[1])] = line[0]

# 將有用的電影資訊提取出來存入movieinfo(dict)
movieinfo = dict()
with open(file=item_filename, mode='r', encoding='ISO-8859-1') as item:
    for line in item:
        if line != '\n':
            line = line.split('|')

            movieid = int(line[0])  # 電影id
            title_and_genre = [line[1]]  # 電影名稱和所屬類別

            for k in range(5, 24):
                if line[k] == '1':
                    title_and_genre.append(genre[k - 5])

            movieinfo[movieid] = title_and_genre
            # 電影id當key，名稱和類別存放在list內當value

if search_id in movieinfo:  # 看欲尋找的id有沒有在movieinfo內
    # 依照題目指定格式輸出
    ans = str()
    ans += movieinfo[search_id][0] + ": "

    for i in range(1, len(movieinfo[search_id])):
        ans += movieinfo[search_id][i] + ', '

    ans = ans.strip(', ')
    print(ans)

else:
    print('No movie found.')
