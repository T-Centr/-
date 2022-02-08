import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.kinopoisk.ru/top/lists/1/")
html = BeautifulSoup(r.content, features='lxml')
def find_links(links, keyword):
    links_filtered = {}
    for link in links:
        if link.has_attr("href") and link["href"].find(keyword) > -1 and \
                link["href"].find("/cast/") == -1:
            links_filtered[link["href"]] = 1
    return list(links_filtered.keys())
films = []
films.extend(find_links(html.find_all("a"), "/film/"))
pages = []
pages.extend(find_links(html.find_all("a"), "/page/"))
for page in pages:
    r = requests.get("https://www.kinopoisk.ru" + page)
    html = BeautifulSoup(r.content)
    films.extend(find_links(html.find_all("a"), "/film/"))
with open("films.txt", "w") as f:
    f.write("\n".join(films))
