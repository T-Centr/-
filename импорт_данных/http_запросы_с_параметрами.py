import requests
import json


request_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;charset=UTF-8"
}
url = "https://postprice.ru/engine/russia/api.php?from=445143&to=620000&" \
      "mass=40&valuation=500&vat=1"
response = requests.get(url, headers=request_headers)
# print("Код ответа:", response.status_code)
response = json.loads(response.text)
# print(response)
print("Стоимость отправки:", response["simple_letter"], "руб.")
