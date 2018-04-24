from Tkinter import Tk
from tkFileDialog import askdirectory
from bs4 import BeautifulSoup
import requests
import easygui
import time
import errno
import os
import sys
import Xmlm
import Interpreter as i
import Load
import argparse


# Function to accept URL and Destination folder arguments

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Provide Table destination URL from DocuWiki")
    parser.add_argument("destination", help="Provide destination for the XML and PDF files to download")

    args = parser.parse_args()

    url = args.url
    location = args.destination

else:
    url = easygui.enterbox(
        msg="Paste Table URL here",
        title="Table URL Retrieval",
        strip=True,
        default="")

    Tk().withdraw()
    location = askdirectory()


# Open user inquiery box for URL string
# url = easygui.enterbox(
#     msg="Paste Table URL here",
#     title="Table URL Retrieval",
#     strip=True,
#     default="")


# Transforms HTML Tree into easily navigatable Python Tree.
page = requests.get(url)
# Beginning of Tree Parsing to find specific objects
soup = BeautifulSoup(page.content, "html.parser")
# Allows user to pick file destination
# Tk().withdraw()
# location = askdirectory()
# Creates object with all HTML links <a> from URL after passing through requests
# and BeautifulSoup
RawLinks = soup.find_all("a")


# Main Download function
def getFile(ChosenUrl, Chosenlocation, fileName):
    baseFolder = Chosenlocation
    pic_url = ChosenUrl
    nfile = fileName + '.pdf'
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

    # Load.pbar(filePath, pic_url)
    # Get the image from the edgeTi web app and save to computed location

    try:
        response = requests.get(pic_url, stream=True, timeout=100)

        if response.ok:
            with open(filePath, 'wb') as handle:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
    except:
        print('fail')




# Main Script



    # Download Loop


for link in RawLinks:
    if "/doku.php?id=item" in link.get("href"):


        # Combines into simple read request pulling for pdf export.
        # Seperate forms of URL with/wuthout export function
        PartialUrl = "http://wiki.inovkh.com/" + link.get("href")
        FullUrl = PartialUrl  + "&do=export_pdf"


        # Tags URL of target file
        response = requests.get(FullUrl, stream=True, timeout=1000)
        fileName = link.get("title")


        # Pull in getFile() object function
        getFile(FullUrl, location, fileName)
        print("Item: " + fileName + " Downloaded.")




# Builds blank XML file in the User chosen location.
maintenancefile = str(Xmlm.build(location))
print(maintenancefile)


# XML Generation/Appending Loop
for string in soup.find_all('tr'):
    for Link in string:
        if '<td class="col0"><a class="wikilink1" href=' in str(Link):
            Id = (Link.get_text())
        else:
            if '<td class="col1' in str(Link):
                dur = i.interpret(str(Link.get_text()))
            else:
                if '<td class="col2' in str(Link):
                    ofs = i.interpret(str(Link.get_text()))
                else:
                    if '<td class="col3">' in str(Link):
                        name = Link.get_text()
                        Xmlm.write1(Id, dur, ofs, name, 'PDF', Id, maintenancefile)
Xmlm.finish(maintenancefile)
print("Maintenance.xml file created.")
