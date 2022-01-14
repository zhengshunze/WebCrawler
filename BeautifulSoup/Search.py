import re

from bs4 import BeautifulSoup

# 搭配open()可以讀HTML檔案內容
# fp - file pointer
# with區塊結束會自動關閉fp，所以不需要呼叫fp.close()
with open("Index.html", "r", encoding="utf-8") as fp:
    # 建立BeautifulSoup物件並指定檔案輸入物件
    soup = BeautifulSoup(fp, "html.parser")

# 搜尋指定標籤
# 搜尋所有<a>標籤並列出內容
print("soup.findAll('a')")
for a in soup.findAll("a"):
    print(a)
print("-----------------------------------")
# 搜尋所有<a>標籤，並將href屬性值列出
print("for a in soup.findAll('a'): print(a['href'])")
for a in soup.findAll("a"):
    print(a["href"])
print("-----------------------------------")

# 使用BeautifulSoup提供的關鍵字：id, class_, href, attrs
# 可以適時搭配正規表示式做模糊查詢
# 搜尋ID值為"link1"的標籤
print(f"soup.findAll(id='link1')\n{soup.findAll(id='link1')}")
print("-----------------------------------")
# 搜尋所有ID值含有"link"的標籤
print(f"soup.findAll(id=re.compile('link'))\n{soup.findAll(id=re.compile('link'))}")
print("-----------------------------------")
# 搜尋ID有值的所有標籤
print(f"soup.find_all(id=True)\n{soup.find_all(id=True)}")
print("-----------------------------------")
# 搜尋所有<p>標籤，而且class值為"title"；因為「class」為Python關鍵字，所以BeautifulSoup改為「 class_ 」
print(f"soup.findAll('p', class_='title')\n{soup.findAll('p', class_='title')}")
# 或改成下列寫法
print(f"soup.findAll('p', 'title')\n{soup.findAll('p', 'title')}")
print("-----------------------------------")
# 搜尋所有class值含有"link"的標籤
print(f"soup.findAll(class_=re.compile('link'))\n{soup.findAll(class_=re.compile('link'))}")
print("-----------------------------------")
# 搜尋所有href含有"frog"標籤
print(f"soup.find_all(href=re.compile('frog'))\n{soup.find_all(href=re.compile('frog'))}")
print("-----------------------------------")
# 搜尋所有href與id有指定值的標籤
print(f"soup.find_all(href=re.compile('frog'), id='link1'))")
print(soup.find_all(href=re.compile('frog'), id='link1'))
print("-----------------------------------")
# BeautifulSoup沒有提供name關鍵字來指定HTML的name屬性，所以要改用attrs來指定
# 搜尋所有符合屬性名稱為"name"與值為"comment"的標籤
print("soup.find_all(attrs={'name': 'comment'})")
print(soup.find_all(attrs={'name': 'comment'}))
print("-----------------------------------")

# 搜尋指定文字值
print(f"soup.find_all(string='小青'))\n{soup.find_all(string='小青')}")
print("-----------------------------------")
# 搜尋符合list的文字值
print(f"soup.find_all(string=['小青', '小蛙', '小呱'])\n{soup.find_all(string=['小青', '小蛙', '小呱'])}")
print("-----------------------------------")
# 搜尋所有指定標籤內含有指定文字值
print(f"soup.find_all('a', string='小青'))\n{soup.find_all('a', string='小青')}")
print("-----------------------------------")
# 搜尋局部符合正規表示式的文字值
print(f"soup.find_all(string=re.compile('蛙'))\n{soup.find_all(string=re.compile('蛙'))}")
print("-----------------------------------")

# 加上函式功能
print("搜尋有class屬性但沒有id屬性的標籤")


def has_class_but_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr('id')


print(soup.find_all(has_class_but_no_id))
print("-----------------------------------")
print("回傳不含有'frog3'的連結")


def not_lacie(href):
    return href and not re.compile("frog3").search(href)


# 只將href值傳入，沒有將整個標籤內容傳入
print(soup.find_all(href=not_lacie))
print("-----------------------------------")

# limit參數
# 搜尋所有<a>標籤，但限縮在前2筆
print(f"soup.find_all('a', limit=2)\n{soup.find_all('a', limit=2)}")
print("-----------------------------------")

# 呼叫標籤方法與呼叫find_all()方法功能相同
print(f"soup.find_all('a')\n{soup.find_all('a')}")
print(f"soup('a')\n{soup('a')}")
print("-----------------------------------")
print(f"soup.find_all(string='小青')\n{soup.find_all(string='小青')}")
print(f"soup(string='小青')\n{soup(string='小青')}")
print("-----------------------------------")

# find()與findAll()差別在於find()搜尋到第一個符合的就停止
print(f"soup.find('a')\n{soup.find('a')}")
print(f"soup.find_all('a')\n{soup.find_all('a')}")
print("-----------------------------------")
