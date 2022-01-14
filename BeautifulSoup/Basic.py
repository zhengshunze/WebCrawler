from bs4 import BeautifulSoup

# 搭配open()可以讀HTML檔案內容
# fp - file pointer
# with區塊結束會自動關閉fp，所以不需要呼叫fp.close()
with open("Index.html", "r", encoding="utf-8") as fp:
    # 建立BeautifulSoup物件並指定檔案輸入物件
    soup = BeautifulSoup(fp, "html.parser")

# 取得<title>標籤完整內容
print(f"soup.title\n{soup.title}")
print("-----------------------------------")
# 如果標籤不存在會得到None，可用is檢查
if soup.x is None:
    print("soup.x不存在")
print("-----------------------------------")
# 取得<title>標籤名稱
print(f"soup.title.name\n{soup.title.name}")
print("-----------------------------------")
# 取得<title>標籤文字值
print(f"soup.title.string\n{soup.title.string}")
print("-----------------------------------")
# 只會取得第一個<a>標籤
print(f"soup.a\n{soup.a}")
print("-----------------------------------")
# 取得<a>標籤指定屬性的值
print(f"soup.a['href']\n{soup.a['href']}")
print("-----------------------------------")
# 如果標籤的屬性不存在，會產生KeyError，需使用try-except
try:
    print(f"soup.a['x']\n{soup.a['x']}")
except KeyError:
    print("soup.a['x']不存在")
print("-----------------------------------")
# 也可呼叫get('attribute')取標籤內指定屬性的值
print(f"soup.a.get('href')\n{soup.a.get('href')}")
print("-----------------------------------")
# get('attribute')取屬性值時，如果該屬性不存在，會得到None，可用is檢查，較方便
if soup.a.get('x') is None:
    print("soup.a.get('x')不存在")
print("-----------------------------------")
# 指定<a>標籤內的class屬性，其值可能有多個，所以回傳list
print(f"soup.a['class']\n{soup.a['class']}")
print("-----------------------------------")
# 可搭配索引取值
print(f"soup.a['class'][0]\n{soup.a['class'][0]}")
print("-----------------------------------")
# 取得<a>標籤內的所有屬性，回傳list
print(f"soup.a.attrs\n{soup.a.attrs['class']}")
print("-----------------------------------")
# 取出所有文字值
print(f"soup.getText()\n{soup.getText()}")
print("-----------------------------------")
