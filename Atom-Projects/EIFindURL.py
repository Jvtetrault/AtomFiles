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
# Creates object with all HTML links <a> from URL after passing through requests
# and BeautifulSoup
RawLinks = soup.find_all("a")


def getFile(ChosenUrl, Chosenlocation, fileName):
    baseFolder = Chosenlocation
    pic_url = ChosenUrl
    nfile = fileName + 'pdf'
    datestr = time.strftime("%Y%m%d")


    def mkdir_p(path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    # figures out where to place the folder and name it
    dayPath = os.path.join(baseFolder, datestr)
    # Generates directory with name as timestamp
    mkdir_p(dayPath)

    # Created path for file to be dropped into new directory
    # Creates path type C:\**Basefolderpath\filename.pdf
    filePath = os.path.join(dayPath, nfile)



    # Get the image from the edgeTi web app and save to computed location
    try:
        response = requests.get(pic_url, stream=True, timeout=2)

        if response.ok:
            with open(filePath, 'wb') as handle:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
    except:
        print('fail')


for link in RawLinks:
    if "/doku.php?id=item" in link.get("href"):
        FullUrl = "http://wiki.inovkh.com/" + link.get("href") + "&do=export_pdf"
        # Tags URL of target file
        response = requests.get(FullUrl, stream=True, timeout=1000)
        fileName = link.get("title")
        # Pull in getFile() object function
        getFile(FullUrl, location, fileName)

print(location)
