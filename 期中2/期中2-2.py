final_ans = []
while True:
    inStr = input()
    if inStr == 'INPUTSTOP':
        break

    inStr = inStr.strip()  # 去除頭尾空白

    pairquotetime = inStr.count('\"') // 2  # 成對引號出現次數

    # 取代成對引號
    for i in range(pairquotetime):
        inStr = inStr.replace('\"', '「', 1)
        inStr = inStr.replace('\"', '」', 1)

    # 處理標點前後空白
    words = [word for word in inStr.split()]
    spe_symbol = [',', ':', '.']  # 需特殊處理的標點符號

    ans = str()
    for word in range(len(words)):
        if word != len(words) - 1:
            next = words[word + 1]

            if next not in spe_symbol:
                ans += words[word] + " "
            else:
                ans += words[word]
        else:
            ans += words[word]
    for sym in spe_symbol:
        new = sym + " "
        ans = ans.replace(sym, new)

    ans = ans.replace("  ", " ")
    ans = ans.strip()
    final_ans.append(ans)

for i in range(len(final_ans)):
    print(final_ans[i])
