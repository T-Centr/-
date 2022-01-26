import requests
import json

r = requests.get(
    'https://geocode-maps.yandex.ru/1.x?geocode=Самара&'
    'apikey=a5d5d613-b4f7-449d-8719-d0e4a511bc8c&format=json&results=1'
)
geo = json.loads(r.content)
# print(geo)
print(geo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
      ['Point']['pos'].split(' ')[0])
