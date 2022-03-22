# WebCrawler
BeautifulSoup4(bs4) 功能說明 \
**1.  讀取資料來源**
- 直接讀取HTML內容

```
# pyhon 內建解析器
soup = BeautifulSoup(htmlDoc, "html.parser") 
# 速度快，需額外安裝套件[ pip install lxml]
soup = BeautifulSoup(htmlDoc, "xml") 
# 速度快，需額外安裝套件[ pip install lxml]
soup = BeautifulSoup(htmlDoc, "lxml") 
# 速度慢，需額外安裝套件 [ pip install html5lib]
soup = BeautifulSoup(htmlDoc, "html5lib")
```
- 開啟文字檔.txt後讀取HTML檔內容

```
# 使用open方式以r(reading)模式來打開本地端文件
with open("Index.html", "r") as fp:
soup = BeautifulSoup(fp, "html.parser")
```
