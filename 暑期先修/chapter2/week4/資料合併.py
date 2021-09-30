import csv  # 引進csv模組
mktfn_sorted = "C:\\Users\\jack\\business_program\\暑期先修\\chapter2\\week4\\mkt_sorted.csv"

fh4 = open(mktfn_sorted, 'r' , encoding = 'utf-8' , newline = '')
reader2 = csv.DictReader(fh4)
# loop through files

mktret = dict()
sret = []
sdate = []
last_coid =""
for arow in reader2:  #process return
    this_coid = arow['COID'].strip()
    this_name = arow['Name'].strip()
    if (this_coid) != last_coid:
        if (len(sret) > 3):
            pass  # run regression here

            # reset sret and sdate
            sret = [float(arow['ROIA'].strip())]
            sdate = [arow['MDATE'].strip()]
        else:
            sret.append(float(arow['ROIA'].strip()))
            sdate.append(arow['MDATE'].strip())

        last_coid = this_coid

fh4.close()
print("Read %d market return data" % len(mktret))
