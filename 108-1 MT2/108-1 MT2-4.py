sentence = input()
sentence = sentence.lower()  # 變小寫

banned_list = input()
banned_list = banned_list.lower()
banned_list = banned_list.split(',')


words = sentence.split()  # 把句子依空格分開
processed_words = []  # 處理後的字

# 注意string為immutable，所以刪除多於字元不能用淺拷貝方法，只能再創一個list
for word in words:
    word = word.strip()
    word = word.strip('.')
    word = word.strip(',')
    word = word.strip(':')
    word = word.strip(';')
    word = word.strip('!')
    word = word.strip('?')
    if word != '' and word not in banned_list:
        processed_words.append(word)

if len(processed_words) == 0:
    print('-1')
else:
    words_dict = dict()

    for word in processed_words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    max_appearance = -1
    max_word = 'ZZZZZZZ'

    for word in words_dict:
        if words_dict[word] > max_appearance:
            max_appearance = words_dict[word]
            max_word = word
        elif words_dict[word] == max_appearance:
            if word < max_word:
                max_appearance = words_dict[word]
                max_word = word

    print(max_word, max_appearance, sep=',')
