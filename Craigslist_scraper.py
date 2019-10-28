#! python3

from bs4 import BeautifulSoup

import requests

url = "https://portland.craigslist.org/search/jjj?"

response = requests.get(url)

print(response)

data = response.text
# calls import
soup = BeautifulSoup(data, "html.parser")

titles = soup.find_all("a", {"class":"result-title"})
# outputs title of job
# for title in titles:
#     print(title.text)

# outputs addresses
addresses = soup.find_all("span",{"class":"result-hood"})
# for address in addresses:
#     print(address.text)

jobs = soup.find_all("p",{"class":"result-info"})
# How to output the result-info on each listing
for job in jobs:
    title = job.find("a",{"class":"result-title"}).text
    location_tag = job.find("span",{"class":"result-hood"})
    location = location_tag.text[2:-1] if location_tag else "N/A"
    date = job.find("time",{"class":"result-date"}).text
    link = job.find("a",{"class":"result-title"}).get("href")
    print("Job Title", title, "\nLocation", location, "\nDate", date, "\nLink", link, "\n---")