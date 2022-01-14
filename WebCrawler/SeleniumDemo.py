from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# 取得網頁內容
def getPageContent(soup):
    content = ""
    for article in soup.select("div.r-ent"):
        # 取出標題
        title = article.select_one(".title").text.strip()
        # 取出連結
        # 當標題為「本文已被刪除」則<a>為None
        a = article.select_one(".title > a")
        link = a["href"] if a is not None else ""
        # 取出作者
        author = article.select_one(".author").text.strip()
        # 取出日期
        date = article.select_one(".date").text.strip()
        content += f"{title}\t{link}\n{author}\t{date}\n"

    return content


# 建立Chrome Driver並指定位置
# 「./chromedriver」代表Chrome Driver檔案放在本Python程式同目錄內
driver = Chrome(service=Service("./chromedriver"))
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 連結到目標網站
driver.get(url)
# By種類參看 https://selenium-python.readthedocs.io/locating-elements.html
# 搜尋參數名稱為"yes"的元件，也就是同意按鈕，然後模擬點擊該按鈕
driver.find_element(By.NAME, "yes").click()
print(f"driver.current_url: {driver.current_url}")
# 取得網頁內容
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
content = getPageContent(soup)
print(content)
