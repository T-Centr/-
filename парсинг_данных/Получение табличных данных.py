import requests
import pandas as pd
from bs4 import BeautifulSoup


r = requests.get("https://worldtable.info/gosudarstvo/tablica-rozhdaemosti"
                 "-po-godam-rossija.html")
html = BeautifulSoup(r.content, features='lxml')
data = []
table = html.find("table")
for tr in table.find_all("tr"):
    data.append([td.get_text() for td in tr.find_all("td")])
data = pd.DataFrame(data[1 : ], columns=["Год", "Количество"])
print(data)
