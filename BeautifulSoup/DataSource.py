# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

htmlDoc = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>HTML文件</title>
</head>
<body>

</body>
</html>"""
# 可以讀HTML文字內容
# 建立BeautifulSoup物件並指定HTML文字內容
soup = BeautifulSoup(htmlDoc, "html.parser")
print(f"HTML文字內容:\n{soup}")
print("-----------------------------------")
print(f"顯示排版好的內容:\n{soup.prettify()}")
print("-----------------------------------")

## 搭配open()可以讀HTML檔案內容
# fp - file pointer
# with區塊結束會自動關閉fp，所以不需要呼叫fp.close()
with open("Index.html", "r", encoding="utf-8") as fp:
    # 建立BeautifulSoup物件並指定檔案輸入物件
    soup = BeautifulSoup(fp, "html.parser")

print(f"HTML檔案:\n{soup}")
print("-----------------------------------")

# 搭配requests可以讀遠端網頁內容
# 取得指定網址的網頁內容
res = requests.get("https://sites.google.com/site/ronforwork/Home/python")
# 建立BeautifulSoup物件並指定網頁內容
soup = BeautifulSoup(res.text, "html.parser")
print(f"遠端網頁:\n{soup}")
print("-----------------------------------")
