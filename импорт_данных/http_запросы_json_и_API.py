import requests
import pandas as pd
import json


request = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
data = pd.DataFrame(json.loads(request.text)["Valute"])
print(json.loads(request.text)["Valute"]["USD"]["Value"] /
      json.loads(request.text)["Valute"]["USD"]["Nominal"])
