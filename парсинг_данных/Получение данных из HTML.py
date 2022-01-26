import requests
from bs4 import BeautifulSoup


r = requests.get(
    "https://beru.ru/catalog/smartfony-i-mobilnye-telefony/80542/list?cvredirect"
    "=3&suggest_reqId=36288023465357252998098266051946&text=Iphone%208"
)
html = BeautifulSoup(r.content, features='lxml')
# print(html)
prices = [p.get_text() for p in html.find_all("span", {"class": "_1u3j_pk1db"})]
print(prices)
