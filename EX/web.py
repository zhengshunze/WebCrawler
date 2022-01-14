"""
test01
"""

try:
    import os
    import sys
    import re
    import textwrap
    import requests
    from bs4 import BeautifulSoup as bs4
except ModuleNotFoundError:
    while True:
        Promote = input("錯誤: 尚未安所需的套件! 是否自動安裝所需套件(Y/n)? : ")
        if Promote == "Y":
            command_1 = 'pip install BeautifulSoup4'
            command_2 = 'pip install requests'
            os.system(command_1)
            os.system(command_2)
            basename = os.path.basename(__file__)
            os.system('python ' + basename)
            quit()
        elif Promote == 'n':
            os.exit()

url = "https://www.tenlong.com.tw/search?availability=buyable&display=list&keyword=python&langs%5B%5D=all"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
response = requests.get(url, headers=headers)
# 建立BeautifulSoup物件
soup = bs4(response.text, "html.parser")

# Method_1
# price = [price.get_text().strip() for price in soup.find_all('span', attrs={'class': 'price'})]
# data = [data.get_text().strip() for data in soup.find_all('span', attrs={'class': 'publish-date'})]
# name = [name.get_text().strip() for name in soup.find_all('strong', attrs={'class': "text-xl"})]
# for x in range(len(price)):
#     print(price[x], data[x], name[x])


# Method_2

for div in soup.select("div.book-data"):
    # print(div)
    book_name = div.select_one("strong.text-xl").text.strip()
    #  book_name = div.a.text.strip()

    book_data = div.select_one("span.publish-date").text.strip()
    # book_price = div.select_one("span.price")
    print(book_name, book_data)
input('\n.......輸入Enter鍵，關閉視窗...........')

# print("for a in soup.findAll('a'): print(a['href'])")
# for a in soup.findAll("a"):
#     print(a["href"])
# for price in soup.find_all('span', attrs={'class': 'price'}):
#     print(price.get_text().strip())
#
#
# for data in soup.findAll('span', attrs={'class': 'publish-date'}):
#     print(data.get_text())

# price = soup.find_all('span', attrs={'class': 'price'})
# print(price)

# page = soup.findAll('span', attrs={'class': 'price'},text=True)
# print(page)

# regions = soup.select('div.content')
# for article in regions:
#     # print(article)
#     price = article.findAll('span', attrs={'class': 'price'})
#     print(price)

# for article in soup.find_all('span', attrs={'class': 'price'}):
#     print(article.get_text().strip())

# # 搜尋所有<p>標籤，而且class值為"title"；因為「class」為Python關鍵字，所以BeautifulSoup改為「 class_ 」
# print(f"soup.findAll('p', class_='title')\n{soup.findAll('p', class_='title')}")

# for article in soup.find_all("div", {"class": "center-container"}):
#     price = article.findAll('span', class_='price')
#     print(price.text)
