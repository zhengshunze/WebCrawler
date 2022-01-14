import re
from bs4 import BeautifulSoup

with open("basic.html", encoding="UTF-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

for ul in soup.ul:
    print(ul.string, end="")

for a in soup.findAll("a", string="GOOGLE搜尋網站"):
    print(a["href"])


