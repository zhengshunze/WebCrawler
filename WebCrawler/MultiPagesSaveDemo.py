import os
import re

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/MobileComm/index.html"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
# 網站起始url
urlStart = "https://www.ptt.cc"

## 當網頁內容多或是多頁面時，應該存檔方便之後使用，否則太佔記憶體空間
# 存放目錄不存在就建立，相對路徑代表存放位置跟執行的Python檔案放在同一目錄
dir = "MultiPagesSaveDemo"
if not os.path.isdir(dir):
    os.makedirs(dir)

number = int(input("要顯示幾頁? "))
for i in range(number):
    print(url)
    ## 以URL的原始檔名當作存檔名稱
    # 去除URL的分隔符號"/" (+ 代表1個以上) 後會得到list，最後一個元素就是檔案名稱
    fileName = re.compile("/+").split(url)[-1]
    # 也可只去除一個"/"，取list最後一個元素也是檔案名稱
    # print(url.split("/")[-1])
    response = requests.get(url, headers=headers)
    ## 將網頁內容存檔
    # 存檔路徑
    path = f"{dir}/{fileName}"
    # "w"-寫入，encoding設定寫入編碼
    file = open(path, "w", encoding="UTF-8")
    file.write(response.text)
    print(f"{fileName} 存檔完成")
    # 儲存完畢要關閉，存檔才會成功
    file.close()

    ## 取得上頁連結
    soup = BeautifulSoup(response.text, "html.parser")
    link = soup.select("div.btn-group.btn-group-paging a")
    url = urlStart + link[1]["href"]


