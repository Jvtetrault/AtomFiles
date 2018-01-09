import requests
from bs4 import BeautifulSoup
import easygui
# import sys
# import EIGrabClass
from Tkinter import Tk
from tkFileDialog import askdirectory

# print(sys.executable)
# print(sys.version)


# Open inquiery box for URL
url = easygui.enterbox(
    msg="Paste Table URL here",
    title="Table URL Retrieval",
    strip=True,
    default="")
# Transforms HTML Tree into easily navigatable Python Tree.
page = requests.get(url)
# Beginning of Tree Parsing to find specific objects
soup = BeautifulSoup(page.content, "html.parser")

Tk().withdraw()
location = askdirectory()

# Finds all links in page
RawLinks = soup.find_all("a")


# Test Out the code by printing
# Rolls through each link from the URL page
# Find maintenance items
for link in RawLinks:
    if "doku.php?id=item" in link.get("href"):
        print(link.get("href"))
