import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/MobileComm/index.html"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
# 網站起始url
urlStart = "https://www.ptt.cc"
## 想看之前文章，先使用Chrome觀察如何取得上頁連結
# 顯示本頁與前2頁個別頁面的url
for i in range(3):
    print(url)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    # 取得上頁連結
    link = soup.select("div.btn-group.btn-group-paging a")
    # 因為上頁連結排在第2個，所以index為1
    url = urlStart + link[1]["href"]
