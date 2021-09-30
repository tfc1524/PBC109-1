infoStr = input()
infoStr = infoStr.split(',')
num = int(infoStr[0])  # 物品個數
limit = int(infoStr[1])  # 箱重限制

item_wStr = input()
item_wStr = item_wStr.split(',')

item_w = []
for i in range(num):
    item_w.append(int(item_wStr[i]))
# 讀取各物品重量並貼到list

item_w.sort(reverse=True)
# 將物品重量由大到小排序

box =[0]

for i_w in range(num):
    for b_w in range(len(box)):
        if (item_w[i_w] + box[b_w]) <= limit:
            box[b_w] += item_w[i_w]
            item_w[i_w] = 0
        else:
            continue

    if item_w[i_w] != 0:  # 代表沒有箱子可以裝
        box.append(item_w[i_w])

"""
為何不能不用index，直接指定list裡面的物件?
若用以下寫法，我的答案box永遠不會變:
for i_w in item_w:
    for b_w in box:
        if (i_w + b_w) <= limit:
            b_w += i_w(是因為這裡的b_w沒有再被assign回到box裡嗎?)
            i_w = 0
        else:
            continue

    if i_w != 0:  # 代表沒有箱子可以裝
        box.append(i_w)
        len_box += 1
"""
print(len(box))
