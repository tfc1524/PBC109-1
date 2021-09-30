import datetime


class Dog:
    def __init__(self, name, height, weight, adopted_date):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)
        self.adopted_date = adopted_date
        self.dust = 0
        self.walk_count = 0
        self.longest_duration = 0
        self.last_walk_date = adopted_date
        self.is_small_dog = self.check_if_small_dog()

    def check_if_small_dog(self):
        if self.height > 60 or self.weight > 30:
            # 判 斷 是 否 為 小 型 犬， 回 傳 boolean 值
            return False
        else:
            return True

    def walk(self, walk_date):
        # 更 新 散 步 次 數、 最 大 散 步 間 隔 時 間、 最 近 散 步 日 期
        if (walk_date - self.last_walk_date).days > self.longest_duration:
            self.longest_duration = (walk_date - self.last_walk_date).days

        self.walk_count += 1
        self.last_walk_date = walk_date

        if self.is_small_dog:
            self.dust += 3
            # 依 據 小 型 犬 的 灰 塵 累 積 效 率 更 新 累 積 灰 塵 量
        else:
            self.dust += 2
            # 依 據 大 型 犬 的 灰 塵 累 積 效 率 更 新 累 積 灰 塵 量

    def bathe(self):
        self.dust = 0
        # 更 新 累 積 灰 塵 量

    def __str__(self):
        return self.name + ',' + str(self.height) + ',' + str(self.weight) + ',' + str(self.dust)


todayStr = input()
today = datetime.datetime.strptime(todayStr, '%Y/%m/%d')  # 今天日期

taskStr = input()  # 讀入task

dogDict = dict()
while True:
    event = input()
    if event == 'Done':
        break

    event = event.split('|')
    name = event[1]

    if event[0] == 'A':
        height = event[2]
        weight = event[3]
        ad_date = datetime.datetime.strptime(event[4], '%Y/%m/%d')

        dogDict[name] = Dog(name, height, weight, ad_date)

    elif event[0] == 'B':
        dogDict[name].bathe()  # 狗洗澡

    elif event[0] == 'W':
        walk_d = datetime.datetime.strptime(event[2], '%Y/%m/%d')
        dogDict[name].walk(walk_d)  # 狗散步

    elif event[0] == 'L':
        try:
            del dogDict[name]  # 將狗狗從字典中刪除
        except KeyError:
            pass

if len(taskStr) > 5:
    taskStr = taskStr.split(',')
    if taskStr[0].strip() == 'TaskA':
        dog_to_find = taskStr[1].strip()
        print(dogDict[dog_to_find])

else:
    if taskStr == 'TaskB':
        min_walkfreq = 9999999
        min_weight = -1
        min_height = -1
        min_big = 1
        min_name = 'Zzz'

        for dog in dogDict:
            walkfreq = float()
            try:
                walkfreq = dogDict[dog].walk_count / (today - dogDict[dog].adopted_date).days
            except ZeroDivisionError:
                continue

            if walkfreq < min_walkfreq:  # 比散步頻率
                min_name = dog
                min_walkfreq = walkfreq
                min_height = dogDict[dog].height
                min_weight = dogDict[dog].weight

            elif walkfreq == min_walkfreq:
                if dogDict[dog].is_small_dog < dogDict[min_name]:  # 比是否大型，0為大型1為小型
                    min_name = dog
                    min_walkfreq = walkfreq
                    min_height = dogDict[dog].height
                    min_weight = dogDict[dog].weight

                elif dogDict[dog].is_small_dog == dogDict[min_name]:
                    if dogDict[dog].weight > min_weight:  # 比體重重
                        min_name = dog
                        min_walkfreq = walkfreq
                        min_height = dogDict[dog].height
                        min_weight = dogDict[dog].weight

                    elif dogDict[dog].weight == min_weight:
                        if dogDict[dog].height > min_height:  # 比高度高
                            min_name = dog
                            min_walkfreq = walkfreq
                            min_height = dogDict[dog].height
                            min_weight = dogDict[dog].weight

                        elif dogDict[dog].height == min_height:
                            if dog < min_name:  # 比字母靠前
                                min_name = dog
                                min_walkfreq = walkfreq
                                min_height = dogDict[dog].height
                                min_weight = dogDict[dog].weight

        print(dogDict[min_name])

    if taskStr == 'TaskC':
        max_duration = -9999999
        max_weight = -1
        max_height = -1
        max_big = 1
        max_name = 'Zzz'
        for dog in dogDict:
            if dogDict[dog].longest_duration > max_duration:  # 比最大間隔時間
                max_name = dog
                max_duration = dogDict[dog].longest_duration
                max_height = dogDict[dog].height
                max_weight = dogDict[dog].weight

            elif dogDict[dog].longest_duration == max_duration:
                if dogDict[dog].is_small_dog < dogDict[max_name].is_small_dog:  # 比是否大型
                    max_name = dog
                    max_duration = dogDict[dog].longest_duration
                    max_height = dogDict[dog].height
                    max_weight = dogDict[dog].weight

                elif dogDict[dog].is_small_dog == dogDict[max_name]:
                    if dogDict[dog].weight > max_weight:  # 比體重重
                        max_name = dog
                        max_duration = dogDict[dog].longest_duration
                        max_height = dogDict[dog].height
                        max_weight = dogDict[dog].weight

                    elif dogDict[dog].weight == max_weight:
                        if dogDict[dog].height > max_height:  # 比高度高
                            max_name = dog
                            max_duration = dogDict[dog].longest_duration
                            max_height = dogDict[dog].height
                            max_weight = dogDict[dog].weight

                        elif dogDict[dog].height == max_height:
                            if dog < max_name:  # 比字母靠前
                                max_name = dog
                                max_duration = dogDict[dog].longest_duration
                                max_height = dogDict[dog].height
                                max_weight = dogDict[dog].weight

        print(dogDict[max_name])

    if taskStr == 'TaskD':
        max_dust = -9999999
        max_weight = -1
        max_height = -1
        max_big = 1
        max_name = 'Zzz'

        for dog in dogDict:
            if dogDict[dog].dust > max_dust:  # 比灰塵量大
                max_name = dog
                max_dust = dogDict[dog].dust
                max_height = dogDict[dog].height
                max_weight = dogDict[dog].weight

            elif dogDict[dog].dust == max_dust:
                if dogDict[dog].is_small_dog < dogDict[max_name].is_small_dog:  # 比是否大型
                    max_name = dog
                    max_dust = dogDict[dog].dust
                    max_height = dogDict[dog].height
                    max_weight = dogDict[dog].weight

                elif dogDict[dog].is_small_dog == dogDict[max_name]:
                    if dogDict[dog].weight > max_weight:  # 比體重重
                        max_name = dog
                        max_dust = dogDict[dog].dust
                        max_height = dogDict[dog].height
                        max_weight = dogDict[dog].weight

                    elif dogDict[dog].weight == max_weight:
                        if dogDict[dog].height > max_height:  # 比高度高
                            max_name = dog
                            max_dust = dogDict[dog].dust
                            max_height = dogDict[dog].height
                            max_weight = dogDict[dog].weight

                        elif dogDict[dog].height == max_height:
                            if dog < max_name:  # 比字母靠前
                                max_name = dog
                                max_dust = dogDict[dog].dust
                                max_height = dogDict[dog].height
                                max_weight = dogDict[dog].weight
        print(dogDict[max_name])
