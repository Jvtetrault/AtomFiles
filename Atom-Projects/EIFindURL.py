import requests
from bs4 import BeautifulSoup
import easygui
from Tkinter import Tk
from tkFileDialog import askdirectory
import time
import errno
import os
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


def getFile(ChosenUrl, Chosenlocation):
    baseFolder = Chosenlocation
    pic_url = ChosenUrl
    datestr = time.strftime("%Y%m%d")
    timestr = time.strftime("%H%M%S") + '.pdf'

    def mkdir_p(path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    # figure out where to save the screengrab
    dayPath = os.path.join(baseFolder, datestr)
    fullPicPath = os.path.join(dayPath, timestr)

    mkdir_p(dayPath)

    # Get the image from the edgeTi web app and save to computed location
    try:
        response = requests.get(pic_url, stream=True, timeout=20)

        if response.ok:
            with open(fullPicPath, 'wb') as handle:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
    except:
        print('fail')


# Test Out the code by printing
# Rolls through each link from the URL page
# Find maintenance items
for link in RawLinks:
    if "doku.php?id=item" in link.get("href"):
        FullUrl = "http://wiki.inovkh.com/" + link.get("href") + "&do=export_pdf"
        response = requests.get(FullUrl, stream=True, timeout=2)
        getFile(FullUrl, location)

print(location)
