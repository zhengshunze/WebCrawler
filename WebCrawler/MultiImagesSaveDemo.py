import os
import re

import requests
from bs4 import BeautifulSoup

url = "https://www.tenlong.com.tw/search"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
# 存放目錄不存在就建立，相對路徑代表存放位置跟執行的Python檔案放在同一目錄
dir = "MultiImagesSaveDemo"
if not os.path.isdir(dir):
    os.makedirs(dir)

keyword = input("輸入書名關鍵字(例如：Python): ")
data = {
    "utf8": "✓",
    "keyword": keyword
}
response = requests.get(url, headers=headers, data=data)
soup = BeautifulSoup(response.text, "html.parser")
# 爬每本書的封面照，並以該書的ISBN當作主檔名
for a in soup.select("a.cover.w-full"):
    # ISBN在<a href>連結內的子字串
    # 例如「<a class="cover w-full" href="/products/9789865028640?list_name=srh">」
    # 去除URL的分隔符號"/" (+ 代表1個以上) 後會得到list，最後一個元素有ISBN
    isbnStr = re.compile("/+").split(a["href"])[-1]
    # ISBN後面正好有"?"，該字元的index當作取ISBN的結束index
    isbn = isbnStr[0:isbnStr.find("?")]
    # 取得圖片網址
    imageSrc = a.img["src"]
    image = requests.get(imageSrc)
    # 取得圖片內容 (轉成bytes)
    imageContent = image.content
    # 存檔路徑
    path = f"{dir}/{isbn}.jpg"
    # "w"-寫入，"b"-二進位
    file = open(path, "wb")
    file.write(imageContent)
    print(f"{path} 存檔完成")
    # 儲存完畢要關閉，存檔才會成功
    file.close()
    print(type(imageContent))
