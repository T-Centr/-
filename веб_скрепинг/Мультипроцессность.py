from multiprocess import Pool
from multiprocess import cpu_count
import requests as requests
from bs4 import BeautifulSoup


def get_film(url):
    r = requests.get("https://www.kinopoisk.ru" + url.strip())
    html = BeautifulSoup(r.content, features='lxml')
    title = html.find("span", {"class": "moviename-title-wrapper"}).get_text()
    tags = html.find_all("td", {"class": "dollar"})
    budget = ""
    sales_www = ""
    if len(tags) > 0:
        sales_www = tags[0].get_text()
        if len(tags) > 1:
            budget = tags[0].get_text()
            sales_www = tags[1].get_text()
            if len(tags) > 2:
                sales_www = tags[2].get_text()
    return [url, title, budget, sales_www]

pool = Pool(cpu_count() * 2)
data = []
with open("films.txt", "r") as f:
    result_iter = pool.map(get_film, f)
    for result in result_iter:
        data.append(result)
print(data)
