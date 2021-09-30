def dectype(columnlist):
    catecnt = 0  # 不能被轉成float的個數
    for i in range(len(columnlist)):
        try:
            n = float(columnlist[i])
        except:
            catecnt += 1
    if catecnt == 0:
        return 'numerical'
    else:
        return 'categorical'


def decmaxlen(columnlist):
    maxlen = 0
    for i in range(len(columnlist)):
        columnlist[i] = columnlist[i].strip()
        thislen = len(columnlist[i])
        if thislen > maxlen:
            maxlen = thislen
    return maxlen


def decnumndecplace(columnlist):
    maxnumlen = 0
    maxdecplace = 0
    if dectype(columnlist) == 'categorical':
        return maxnumlen, maxdecplace
    else:
        for i in range(len(columnlist)):
            columnlist[i] = columnlist[i].strip('-')
            columnlist[i] = columnlist[i].strip('+')
            
            floatlist = columnlist[i].split('.')
            if len(floatlist) == 1:  # 沒有小數點
                this_numlen = len(floatlist[0])
                this_decplace = 0
            else:
                this_numlen = len(floatlist[0]) if floatlist[0] != "" else 1
                this_decplace = len(floatlist[1]) if floatlist[1] != "" else 1


            if this_numlen > maxnumlen:
                maxnumlen = this_numlen

            if this_decplace > maxdecplace:
                maxdecplace = this_decplace
        return maxnumlen, maxdecplace
filename = input()
mode = input()

with open(file=filename, mode='r', encoding='cp950') as f:
    lines = f.readlines()
    lines = [k.strip('\n')for k in lines]

cols = dict()
for line in lines:
    line = line.split(',')
    for i in range(len(line)):
        if i not in cols:
            cols[i] = [line[i]]
        else:
            cols[i].append(line[i])

colnum = len(cols.keys())  # 欄位個數
type = []
maxlen = []
maxnumlen = []
maxdecplace = []

for i in range(colnum):
    type.append('0')
    maxlen.append('0')
    maxnumlen.append('0')
    maxdecplace.append('0')

for k in cols.keys():
    type[k] = dectype(cols[k])
    maxlen[k] = decmaxlen(cols[k])
    new_maxnumlen, new_maxdecplace = decnumndecplace(cols[k])
    maxnumlen[k] = new_maxnumlen
    maxdecplace[k] = new_maxdecplace

if mode == 'TYPE':
    for i in range(colnum):
        print(i, end=': ')
        print(type[i])
elif mode == 'MAXLEN':
    for i in range(colnum):
        print(i, end=': ')
        print(maxlen[i])
elif mode == 'MAXNUMLEN':
    for i in range(colnum):
        print(i, end=': ')
        print(maxnumlen[i])
elif mode == 'MAXDECPLACE':
    for i in range(colnum):
        print(i, end=': ')
        print(maxdecplace[i])
