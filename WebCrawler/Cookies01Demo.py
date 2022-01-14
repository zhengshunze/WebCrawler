import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
response = requests.get(url, headers=headers)
print(response.text)
# 跟之前去PTT手機版不同，八卦版會檢查是否有點擊滿18歲的按鈕，如果沒有會導至同意畫面，而無法進一步取得文章資料
# 使用Chrome開發者工具查看：Payload、Cookies、原始碼
