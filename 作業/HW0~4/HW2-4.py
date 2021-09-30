day = int(input())
sleep_hours = []
# day讀取總睡覺天數，sleep_hours是用來存每天睡覺時間的list

total = float()  # 總睡覺時數，算平均時要用
lemon_face = 0
sugar_face = 0
egg_face = 0
# 三種面膜張數

pay = float()
# 應付金額

for i in range(0, day):
    sleep_hours.append(float(input()))  # 將每天睡覺時數存到sleep_hours內

for i in sleep_hours:
    if i > 7:  # 計算睡覺時數>=7的天數
        lemon_face += 1

    total += i

avg = total / day  # 算出平均睡覺時數

lemon = float()
lemon = 1.5 * lemon_face  # 需要的檸檬顆數

if (lemon % 1) != 0:
    lemon = int(lemon + 1.0)  # 將檸檬顆數取整數

xin_ren = float()  # 杏仁油
honey = float()  # 蜂蜜
egg = float()  # 蛋(顆)
egg_box = float()  # 蛋(盒)

if avg <= 6.0:  # 平均睡眠時數<=6時，面膜及原料的計算
    sugar_face = (day - lemon_face)
    xin_ren = 4*lemon_face + 9*sugar_face
    honey = 18 * sugar_face
else:  # 平均睡眠時數>6時，面膜及原料的計算
    egg_face = (day - lemon_face)
    xin_ren = 4 * lemon_face
    honey = 6 * egg_face
    egg = 2 * egg_face  # 計算所需雞蛋數

    if egg % 3 != 0:  # 判斷所需雞蛋數是否為3的倍數，以此決定要幾盒雞蛋
        egg_box = (egg // 3) + 1
    else:
        egg_box = egg // 3

if lemon >= 5:  # 檸檬大於5顆時要打折
    pay = lemon*0.9*7 + xin_ren*0.6 + honey*1.2 + egg_box*25
else:
    pay = lemon*7 + xin_ren*0.6 + honey*1.2 + egg_box*25

print(int(pay))  # 取整數再輸出
