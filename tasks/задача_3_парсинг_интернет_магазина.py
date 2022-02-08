import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "ittensive-python-scraper/1.0 (+https://www.ittensive.com)"
}

r = requests.get(
    "https://market.yandex.ru/catalog--kholodilniki/71639/list?glfilter=7893318"
    "%3A152776&cpa=1&hid=15450081&rs=eJwzYgpgBAABcwCG&suggest_text=Холодильники"
    "%20Саратов&suggest=1&suggest_type=categories_vendors&was_redir=1&rt=8&"
    "onstock=0&local-offers-first=0", headers=headers
)

html = BeautifulSoup(r.content, features='lxml')
# print(html)
links = html.find_all('a', {'class': '_2f75n _3xGwF cia-cs'})

# print(r.content)
# links = html.find_all("a", {"class": "grid-snippet__react-link"})
link_263 = ''
link_452 = ''
for link in links:
    if str(link).find("Саратов 263") > -1:
        link_263 = link["href"]
    if str(link).find("Саратов 452") > -1:
        link_452 = link["href"]

def find_volume(link):
    r = requests.get("https://market.yandex.ru" + link, headers=headers)
    html = BeautifulSoup(r.content, features='lxml')
    print(html)
    volume = html.find_all("span", {"class": "ZIZLH"})
    return int(''.join(i for i in volume[2].get_text() if i.isdigit()))

if link_263 and link_452:
    volume_263 = find_volume(link_263)
    volume_452 = find_volume(link_452)
    diff = max(volume_263, volume_452) - min(volume_263, volume_452)
    print(diff)
