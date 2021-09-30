fn1 ="C:\\Users\\jack\\business_program\\test_in.txt"
fh1 = open(  fn1 , 'r', encoding = 'utf-8' )

linecount = 0

for aline in fh1 :
    linecount += 1

    if len(aline) < 75 :
        print("%02d:%s" % (linecount , aline.strip() ) )

    else :
        print("%02d:%s...(truncated)" % ( linecount , aline[0:75] ))


fh1.close()
