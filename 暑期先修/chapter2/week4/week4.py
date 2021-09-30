import csv # 引進csv模組
stockname ="C:\\Users\\jack\\business_program\\暑期先修\\stock.txt"
fh1 = open(stockname, 'r' ,encoding = 'cp950' , newline = '')
# file handler newline是為了讓csv模組能正確讀檔

cheader = fh1.readline()
reader1 = csv.reader(fh1, delimiter = '\t')

stockname_tmp1 = "C:\\Users\\jack\\business_program\\暑期先修\\stock_tmp1.csv"
fh3 = open(stockname_tmp1, 'w' , encoding = 'utf-8' , newline ='')
writer3 = csv.writer(fh3)

for arow in reader1:
    arow = map(lambda x : x.strip() , arow)
    writer3.writerow(arow)

fh3.close()
fh1.close()
