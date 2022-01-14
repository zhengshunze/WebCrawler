import requests
from bs4 import BeautifulSoup


# 取得網頁內容
def getPageContent(soup):
    content = ""
    for article in soup.select("div.r-ent"):
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
        content += f"{title}\t{link}\n{author}\t{date}\n"

    return content


url = "https://www.ptt.cc/bbs/MobileComm/index.html"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
# 網站起始url
urlStart = "https://www.ptt.cc"

number = int(input("要顯示幾頁? "))
# 顯示本頁與前2頁個別頁面內容
for i in range(number):
    print(url)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    # 取得網頁內容
    content = getPageContent(soup)
    print(content)
    # 取得上頁連結
    link = soup.select("div.btn-group.btn-group-paging a")
    url = urlStart + link[1]["href"]

