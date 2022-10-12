from bs4 import BeautifulSoup

import requests
URL = "https://www.geeksforgeeks.org/"
r = requests.get(URL)
print(r.content)