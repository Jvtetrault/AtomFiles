from Tkinter import Tk
from tkFileDialog import askdirectory
from bs4 import BeautifulSoup
# import click
import requests
import easygui
import time
import errno
import os
import sys


print(sys.executable)
print(sys.version)


url = "http://wiki.inovkh.com/doku.php?id=xpr_component_table"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

rowName = soup.find_all('td')

for tr in rowName:
    for td in tr.descendants:
        print(td)


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
