#! python3 

from bs4 import BeautifulSoup

import requests

url = "https://www.yahoo.com/"

response = requests.get(url)

print(response)

data = response.text

soup = BeautifulSoup(data, "html.parser")
# Grabs tags with <a
tags = soup.find_all("a")
# outputs the tag <a href on whole src 
for tag in tags:
    print(tag.get("href"))