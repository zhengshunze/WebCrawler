import time
import requests
from bs4 import BeautifulSoup

url = "https://ifconfig.me"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}

# 使用Proxy功能，注意免費Proxy多半無效
# proxies = {
#     "http": "http://18.214.35.123:80",
#     "https": "https://185.201.88.128:6969"
# }
# response = requests.get(url, headers=headers, proxies=proxies)
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
ip_address = soup.select_one("td#ip_address_cell").text
print(f"IP Address: {ip_address}")
user_agent = soup.find("td", string="User Agent").find_next("td").text
print(f"User Agent: {user_agent}")
