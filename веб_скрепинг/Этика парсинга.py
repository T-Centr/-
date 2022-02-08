import time
import requests


headers = {"User-Agent": "ittensive-python-scraper/1.0 (+https://www.ittenasive.com)"}
t = time.now()
r = requests.get("url", headers=headers)
response_time = time.now() - t
# 2-3 rps, Crawl-Delay, response.time*2-3
time.sleep(round(response_time * 3))
