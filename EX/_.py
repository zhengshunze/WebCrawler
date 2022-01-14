from bs4 import BeautifulSoup

with open("Index.html", "r", encoding="UTF-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# 取得Html完整內容
# print(soup)

# 取得Html完整內容並將編排美化以內縮顯示
# print(soup.prettify())

# 取得Html的title標籤的內容
# print(soup.title)

# 取得Html的title標籤的文字
# print(soup.title.string)

# 只取得<a>標籤的第一個(找到就結束搜尋)
# print(soup.a)

# 取得<a>標籤指定屬性的值(如href)
# print(soup.a['href'])

# 若找不到任何x之屬性則是用try、except
# print(soup.a['x']) # ---->出現: KeyError(寫法如下)
# try:
#     print(soup.a['x'])
# except KeyError:
#     print("x is not exist")

# 也可以使用get('attribute')取得標籤內的屬性的值
# print(soup.a.get('href'))

# 如果get('attribute')
# 取得標籤內的屬性x的值不存在時
# 會得到'None'，可以用is檢查
# if soup.a.get("x") is None:
#     print('x is not exist')

# 指定<a>標籤內的class屬性，因為可能為多個，
# 會回傳list，兩種寫法結果一樣

# print(soup.a['class'])
# print(soup.a.attrs['class'])

# 可搭配索引值列出指定的index
# print(soup.a['class'][0])   --> 列出frog

# 取得所有文字
# print(soup.getText())
