
def strToInt(num, single, ten, special):
    # 找出 0~9
    if(num in single):
        return single.index(num)

    # 找出 10 的倍數
    if(num in ten):
        return ten.index(num)*10

    # 找出 11 ~ 19
    if(num in special):
        return special.index(num)+10

    # 找出 21~29、31~39、...、91~99
    for i in range(2, 10):
        for j in range(1, 10):
            if(num == ten[i] + '-' + single[j]):
                return i*10+j

    # 自己 debug 時比較方便
    # 但若程式是與他人合作時應該要用 exception
    return -1


# 定義個位數
single_digit = ['zero', 'one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine']
# 定義十位數
ten_digit = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty',
             'sixty', 'seventy', 'eighty', 'ninety']
# 定義10~19
special = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen']

num1, calculate_type, num2 = input().split(' ')
num1 = strToInt(num1, single_digit, ten_digit, special)
num2 = strToInt(num2, single_digit, ten_digit, special)

if(num1 == -1 or num2 == -1):
    print('error')
if(calculate_type == 'plus'):
    print(num1 + num2)
if(calculate_type == 'minus'):
    print(num1 - num2)
