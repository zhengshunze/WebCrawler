from bs4 import BeautifulSoup

with open("basic.html", "r", encoding="UTF-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# 取得<ul>內所有<li>的文字
for tag in soup.ul("li"):
    # strip()可去除前後空白字元
    text = tag.text.strip()
    print(text)

# 取得"GOOGLE搜尋網站"的超連結
for a in soup("a", string="GOOGLE搜尋網站"):
    print(a["href"])


