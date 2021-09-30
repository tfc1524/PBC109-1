# 4-6 CSV檔案排序
import csvsorter
stockname_tmp1 = "C:\\Users\\jack\\business_program\\暑期先修\\stock_tmp1.csv"
stockname_sorted = "C:\\Users\\jack\\business_program\\暑期先修\\stock_sorted.csv"

csvsorter.csvsort(mktfn_tmp1 , [0 , 2] , output_filename = mktfn_sorted , has_header = True)
# 將檔案排序
