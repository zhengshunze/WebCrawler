import json
import requests

# 餐飲開放資料JSON格式網址
url = "https://gis.taiwan.net.tw/XMLReleaseALL_public/restaurant_C_f.json"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
response = requests.get(url, headers=headers)
# 需要標註內容使用"utf-8-sig"編碼，
# 否則產生"JSONDecodeError("Unexpected UTF-8 BOM (decode using utf-8-sig)"錯誤
response.encoding = "utf-8-sig"
dic = json.loads(response.text)
infoList = dic["XML_Head"]["Infos"]["Info"]
print("只列出前10筆資料")
for i in range(10):
    print(infoList[i])
