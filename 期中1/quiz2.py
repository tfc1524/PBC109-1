infoStr = input()
infoStr = infoStr.split(',')

price_meal = int(infoStr[0])
price_drink = int(infoStr[1])
disc = int(infoStr[2])
num_customer = int(infoStr[3])

customerStr = input()
customerStr = customerStr.split(',')

customer = []
for i in customerStr:
    customer.append(int(i))

num_meal = 0
num_drink = 0
num_disc = 0

for i in customer:
    if i == 1:
        num_meal += 1
    elif i == 2:
        num_drink += 1
    else:
        num_disc += 1

if (price_meal+price_drink-disc) >=0:
    rev = price_meal*num_meal + price_drink*num_drink + (price_meal+price_drink-disc) * num_disc
else:
    rev = price_meal*num_meal + price_drink*num_drink

print(str(num_meal + num_disc) + "," + str(num_drink + num_disc) + "," + str(rev))
