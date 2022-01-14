# -*- coding: utf-8 -*-
# 只需爬第⼀⾴所有書的售價、出版⽇期、書名並顯⽰如下
# 售價: $616 出版⽇期：2019-10-11 Python 技術者們
# 售價: $562 出版⽇期：2021-12-06 Python 出神入化

import requests
from bs4 import BeautifulSoup

url = "https://www.tenlong.com.tw/search?availability=buyable&display=list&keyword=python&langs%5B%5D=all"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

for article in soup.select("div.content"):
    #  print(article)
    price = article.select_one(soup.span("price"))
    print(price.text)
