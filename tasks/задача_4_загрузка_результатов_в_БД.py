import sqlite3
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/78.0.3904.97 "
                  "YaBrowser/19.12.0.358 Yowser/2.5 Safari/537.36"
}


def find_number(text):
    return int("0" + "".join(i for i in text if i.isdigit()))


def find_data(link):
    rq = requests.get("https://market.yandex.ru" + link, headers=headers)
    htm = BeautifulSoup(rq.content, features='lxml')
    title = htm.find("h1", {"class": "1BWd_ _2OAAC"}).get_text()
    price = find_number(htm.find("span", {"data-tid": "c0924aa2"}).get_text())
    tags = htm.find_all("span", {"class": "_2v4E8"})
    width = 0
    depth = 0
    height = 0
    volume = 0
    freezer = 0
    for tag in tags:
        tag = tag.get_text()
        if tag.find("ШхВхГ") > -1:
            dims = tag.split(":")[1].split("х")
            width = float(dims[0])
            depth = float(dims[1])
            height = float(dims[2].split(" ")[0])
        if tag.find("общий объем") > -1:
            volume = find_number(tag)
        if tag.find("объем холодильной камеры") > -1:
            freezer = find_number(tag)
    return [link, title, price, width, depth, height, volume, freezer]


r = requests.get(
    "https://market.yandex.ru/catalog--kholodilniki/71639/list?glfilter="
    "7893318%3A152776&cpa=1&hid=15450081&rs=eJwzYgpgBAABcwCG&suggest_text="
    "Холодильники%20Саратов&suggest=1&suggest_type=categories_vendors&"
    "was_redir=1&rt=8&onstock=0&local-offers-first=0", headers=headers
)

html = BeautifulSoup(r.content, features='lxml')
links = html.find_all("a", {"class": "grid-snippet__react-link"})
data = []
for link in links:
    if link["href"] and link.get_text().find("Саратов") > -1:
        data.append(find_data(link["href"]))
conn = sqlite3.connect("c:/sqlite/data.db3")
db = conn.cursor()
db.execute('''CREATE TABLE beru_goods
            (id INTEGER PRIMARY KEY AUTOINCREMENT not null,
            url text,
            title text default '',
            price INTEGER default 0,
            width FLOAT default 0.0,
            depth FLOAT default 0.0,
            height FLOAT default 0.0,
            volume INTEGER default 0,
            freezer INTEGER default 0)''')
conn.commit()
db.executemany(
    '''INSERT INTO beru_goods (url, title, price, width, depth, height, volume,
     freezer) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', data
)

conn.commit()
print(db.execute("SELECT * FROM beru_goods").fetchall())
db.close()
