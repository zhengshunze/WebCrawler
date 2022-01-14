import re
from bs4 import BeautifulSoup

with open("table.html", encoding="UTF-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

print(soup.select('tr td')[0:3])
print(soup.select('tr td')[3:6])

for i in soup.findAll("td"):
    print(i.string, end=" \n")

for i in soup.select('tr td'):
    print(i.string, end=" \n")

friends = []
data = soup.select('tr td')
for data in soup.select("td"):
    friend = data.text
    friends.append(friend)
print(friends)
