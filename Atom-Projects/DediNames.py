from Tkinter import Tk
from bs4 import BeautifulSoup
# import click
import requests
import sys


print(sys.executable)
print(sys.version)


url = "http://wiki.inovkh.com/doku.php?id=xpr_component_table"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

rows = soup.find_all('tr')

print (rows)

# for tr in rows:
#     for td in tr.descendants:
#         print(obj)

# for tr in rows:
#     tds = soup.find_all('td')
#     print(tds[3].text)


# Tk().withdraw()
#
# RawLinks = soup.find_all("a")
# RawTr = soup.findAll('tr')
# data = [[td.findChildren(text=True) for td in tr.findall("td")]]
#
# new = "result: " + RawNames
# print(new)
