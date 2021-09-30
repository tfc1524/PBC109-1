import requests
from bs4 import BeautifulSoup
import datetime
import csv

class Article:
    def __init__(self, title, pop, author, link, date):
        self.title = str(title)
        self.comment = int(comment)
        self.author = str(author)
        self.link = str(link)
        self.date = str(date)


titles = []
author = []
date = []
comnum = []
html = []

for k in range(4990, 5004):
    url = 'https://www.ptt.cc/bbs/Stock/index' + str(k) + '.html'

    stock_r = requests.get(url)  # 用request得到該網址的html

    stock_soup = BeautifulSoup(stock_r.text, 'html.parser')
    title_tag = stock_soup.title  # 標題aka網頁名稱

    attr_title = {'class': 'title'}
    attr_comnum = {'class': 'nrec'}
    attr_author = {'class': 'author'}
    attr_date = {'class': 'date'}

    div_titles = stock_soup.find_all('div', attrs= attr_title)  # 爬標題，資料型態像是一個list
    div_comnum = stock_soup.find_all('div', attrs=attr_comnum)  # 爬回復數量
    div_author = stock_soup.find_all('div', attrs=attr_author)
    div_date = stock_soup.find_all('div', attrs=attr_date)
    a_tags = stock_soup.find_all('a')


    for i in range(len(div_titles)):
        if div_titles[i].get_text().find('刪除') and div_titles[i].get_text().find('已被')== -1:  # 沒被刪除的文
            titles.append(div_titles[i].get_text().replace(',', '').strip())
            author.append(div_author[i].get_text().strip())
            date.append(div_date[i].get_text().strip())
            comnum.append(div_comnum[i].get_text().strip())

    for i in range(len(a_tags)):
        if a_tags[i]['href'].find('M.') != -1 and a_tags[i]['href'].find('.A.') != -1:
        # 表示是該文章連結
            newlink = 'https://www.ptt.cc' + a_tags[i]['href']
            html.append(newlink.strip())
print(len(date), len(titles), len(author), len(html), len(comnum))

filename = 'C:\\Users\\jack\\business_program\\期末練習\\stockptt.csv'
with open(file=filename, mode='w', encoding='cp950') as f:
    f.write('標題,作者,人氣,日期,連結' + '\n')
    for i in range(len(titles)):
        newarticle = titles[i] + ',' + author[i] + ',' + comnum[i] + ','
        newarticle += date[i] + ',' + html[i] + '\n'
        f.write(newarticle)
