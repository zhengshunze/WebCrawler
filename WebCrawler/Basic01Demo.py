import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/MobileComm/index.html"
# 有些防爬蟲網站會檢查請求標頭 (request headers) 的user-agent是否有值，以辨識是一般使用者還是爬蟲程式訪問，來決定是否拒絕請求
# 建議加上user-agent，值可以複製Chrome > F12 > Network > Headers > Request Headers > user-agent，來偽裝成一般使用者
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
response = requests.get(url, headers=headers)
# 顯示結果網頁內容
# print(response.text)
# 建立BeautifulSoup物件
soup = BeautifulSoup(response.text, "html.parser")
# 先使用Chrome觀察一篇文章範圍，並用select_one()測試
article = soup.select_one("div.r-ent")
# print(article)
# 取出標題
title = article.select_one(".title").text.strip()
# 取出連結
# 當標題為「本文已被刪除」則<a>為None
a = article.select_one(".title > a")
link = a["href"] if a is not None else ""
# 取出作者
author = article.select_one(".author").text.strip()
# 取出日期
date = article.select_one(".date").text.strip()
print(f"{title}\t{link}\n{author}\t{date}")
print("----------------------------------")
