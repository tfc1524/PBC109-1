print ("Enter the amount of consume : ")

consume = int ( input () )
find = 1000 - consume

fiveh = find // 500
find = find - fiveh * 500

oneh =  find  // 100
find = find - oneh * 100

fifty = find // 50
find = find - fifty * 50


ten = find // 10
find = find - ten * 10

five = find // 5
find = find - five * 5

one = find

if fiveh != 0 :
    if oneh == fifty == ten == five == one == 0 :
        print ("500, " + str(fiveh)  , end = "")
    else :
        print ("500, " + str(fiveh) + "; " , end = "")

if oneh != 0 :
    if fifty == ten == five == one == 0 :
        print ("100, " + str(oneh)  , end = "")
    else :
        print ("100, " + str(oneh) + "; " , end = "")

if fifty != 0 :
    if ten == five == one == 0 :
        print ("50, " + str(fifty)  , end = "")
    else :
        print ("50, " + str(fifty) + "; " , end = "")

if ten != 0 :
    if five == one == 0 :
        print ("10, " + str(ten)  , end = "")
    else :
        print ("10, " + str(ten) + "; " , end = "")

if five != 0 :
    if one == 0 :
        print ("5, " + str(five)  , end = "")
    else :
        print ("5, " + str(five) + "; " , end = "")

if one != 0 :
    print ("1, " + str(one) , end = "")
