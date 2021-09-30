def eng2int(numStr):
    digital_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'eleven': 11, 'twelve': 12}
    ten_dict = {'ten': 10, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}

    num = 0
    if numStr.find('-') != -1:  # 若大於20且個位數不為0
        numStr = numStr.split('-')
        num += ten_dict[numStr[0]] + digital_dict[numStr[1]]
    elif numStr in ten_dict:  # 大於20但個位數為0
        num += ten_dict[numStr]
    elif numStr in digital_dict:  # 個位數 or 11 or 12
        num += digital_dict[numStr]
    elif numStr.find('teen') != -1:  # 13~19
        t_index = numStr.find('teen')
        num += 10 + digital_dict[numStr[: t_index]]

    return num


sentence = input().split()

former = eng2int(sentence[0])
latter = eng2int(sentence[2])
result = int()

if sentence[1] == 'plus':
    result = former + latter
    print(result)
else:
    result = former - latter
    print(result)
