from bs4 import BeautifulSoup
# 注意第38行的寫法，Select、find_All 差異
# 搭配open()可以讀HTML檔案內容
# fp - file pointer
# with區塊結束會自動關閉fp，所以不需要呼叫fp.close()
with open("Index.html", "r", encoding="utf-8") as fp:
    # 建立BeautifulSoup物件並指定檔案輸入物件
    soup = BeautifulSoup(fp, "html.parser")

# 搜尋<title>
print(f"soup.select('title')\n{soup.select('title')}")
print(f"soup.findAll('title')\n{soup.findAll('title')}")
print("-----------------------------------")
# 搜尋class值為"title"
print(f"soup.select('.title')\n{soup.select('.title')}")
print(f"soup.findAll(class_='title')\n{soup.findAll(class_='title')}")
print("-----------------------------------")
# 搜尋<p>且class值為"title"
print(f"soup.select('p.title')\n{soup.select('p.title')}")
print(f"soup.findAll('p', class_='title')\n{soup.findAll('p', class_='title')}")
print("-----------------------------------")
# 搜尋id值為"link1"
print(f"soup.select('#link1')\n{soup.select('#link1')}")
print(f"soup.findAll(id='link1')\n{soup.findAll(id='link1')}")
print("------------------f-----------------")
# 搜尋id值為"link1"或"link2"
print(f"soup.select('#link1, #link2')\n{soup.select('#link1, #link2')}")
print(f"soup.findAll(id=['link1', 'link2'])\n{soup.findAll(id=['link1', 'link2'])}")
print("-----------------------------------")
# 搜尋class值為"frog"與"link1"(兩者都需要有)
print(f"soup.select('a.frog.link1')\n{soup.select('a.frog.link1')}")
print("-----------------------------------")
# 搜尋<a>且id值為"link1"
print(f"soup.select('a#link1')\n{soup.select('a#link1')}")
print(f"soup.findAll('a', id='link1')\n{soup.findAll('a', id='link1')}")
print("--------------------d---------------")
# 搜尋<body>內的子標籤<a>
print(f"soup.select('body a')\n{soup.select('body a')}")
print(f"soup.findAll('body')[0].findAll('a')\n{soup.findAll('body')[0].findAll('a')}")
print("-----------------------------------")
# 搜尋<body>內的直屬子標籤<a>；<a>雖為子標籤，但非直屬，所以會搜尋不到
print(f"soup.select('body > a')\n{soup.select('body > a')}")
# 搜尋<p>的直屬子標籤<a>
print(f"soup.select('p > a')\n{soup.select('p > a')}")
print("-----------------------------------")
# 搜尋<p>直屬子標籤內的class值為"frog"
print(f"soup.select('p > .link')\n{soup.select('p > .link')}")
print("-----------------------------------")
# 搜尋<p>直屬子標籤內的id值為"link1"
print(f"soup.select('p > #link1')\n{soup.select('p > #link1')}")
print("-----------------------------------")

# select_one()與select()差別在於select_one()搜尋到第一個符合的就停止，與find()相同
print(f"soup.select_one('a')\n{soup.select_one('a')}")
print(f"soup.select('a')\n{soup.select('a')}")
print("-----------------------------------")

