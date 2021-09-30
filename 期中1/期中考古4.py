infoStr = input()
infoStr = infoStr.split(',')
BUSMAN_NUM = int(infoStr[0])
GOODS_NUM = int(infoStr[1])
TRADE_NUM = int(infoStr[2])
BUY = int(infoStr[3])
# 讀取資訊

busman =[]
goods =[]
score = []

for i in range(TRADE_NUM):
    trade_infoStr = input()
    trade_infoStr = trade_infoStr.split(',')
    busman.append(int(trade_infoStr[0]))
    goods.append(int(trade_infoStr[1]))
    score.append(int(trade_infoStr[2]))

correct_trades = []

for i in range(TRADE_NUM):
    if goods[i] == BUY:
        correct_trades.append(i)
# 找出相符商品的交易

max_score = 0

for i in correct_trades:
    if score[i] >= max_score:
        max_score = score[i]
# 找出最大分數

ans_trade = []

for i in correct_trades:
    if score[i] == max_score:
        ans_trade.append(i)
# 找出並列第一的交易

ans_busman = []

for i in ans_trade:
    ans_busman.append(busman[i])
# 將最棒商人貼到答案LIST中

print(max_score, end=':')

ans_busman.sort()

for i in ans_busman:
    if len(ans_busman) > 1:
        if i != ans_busman[-1]:
            print(i, end=',')
        else:
            print(i)
    else:
        print(i)
