import requests
from bs4 import BeautifulSoup
import easygui
from Tkinter import Tk
from tkFileDialog import askdirectory
# import time
# import os
# import errno
# import sys

# print(sys.executable)
# print(sys.version)


# Open user inquiery box for URL string
url = easygui.enterbox(
    msg="Paste Table URL here",
    title="Table URL Retrieval",
    strip=True,
    default="")
# Transforms HTML Tree into easily navigatable Python Tree.
page = requests.get(url)
# Beginning of Tree Parsing to find specific objects
soup = BeautifulSoup(page.content, "html.parser")
# Allows user to pick file destination
Tk().withdraw()
location = askdirectory()
# Finds all links in page
RawLinks = soup.find_all("a")


# Test Out the code by printing
# Rolls through each link from the URL page
# Find maintenance items
for link in RawLinks:
    if "doku.php?id=item" in link.get("href"):
        FullUrl = "http://wiki.inovkh.com/" + link.get("href")
        response = requests.get(FullUrl)
        print(FullUrl)


print(location)
