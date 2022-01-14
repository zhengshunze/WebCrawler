from bs4 import BeautifulSoup

# 搭配open()可以讀HTML檔案內容
# fp - file pointer
# with區塊結束會自動關閉fp，所以不需要呼叫fp.close()
with open("Index.html", "r", encoding="utf-8") as fp:
    # 建立BeautifulSoup物件並指定檔案輸入物件
    soup = BeautifulSoup(fp, "html.parser")

# 取得上一層父標籤
print(f"soup.title.parent.name\n{soup.title.parent.name}")
print("-----------------------------------")
# 取得所有父標籤
print("for parent in soup.title.parents")
for parent in soup.title.parents:
    print(parent.name)
print("-----------------------------------")
# 取得指定父標籤
tag = soup.find(string="小青")
print("尋找父標籤<p>")
print(tag.find_parent('p'))
print("-----------------------------------")
# 取得指定子標籤
print(f"soup.p.b\n{soup.p.b}")
print("-----------------------------------")
# 取得所有子標籤
print("for child in soup.p.children")
for child in soup.p.children:
    print(child.name)
print("-----------------------------------")
