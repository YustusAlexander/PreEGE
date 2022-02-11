import requests
from bs4 import BeautifulSoup
import json




url = "http://os.fipi.ru/api/tasks/17484"
url1 = 'http://os.fipi.ru/api/tasks/CheckAnswer/17484'
url2 = 'http://os.fipi.ru/api/tasks/17484/CheckAnswer'

headers = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.2.834 Yowser/2.5 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.text

with open("index17484.html", "w", encoding="UTF-8") as file:
     file.write(src)

# soup = BeautifulSoup(src, "lxml")
# all_tasks = soup.find_all(class_="MsoNormal")
# for item in all_tasks:
#     print(item.text)
