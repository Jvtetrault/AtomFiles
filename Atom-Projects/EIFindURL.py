import requests
from bs4 import BeautifulSoup
import sys
import EIGrabClass

print(sys.executable)
print(sys.version)

# Transforms HTML Tree into easily navigatable Python Tree.
# Beginning of Tree Parsing to find specific objects
url = "http://wiki.inovkh.com/doku.php?id=xpr_component_table"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Finds all links in page
RawLinks = soup.find_all("a")


# Test Out the code by printing
# Rolls through each link from the URL page
# Find maintenance items
# Call EdgeTIGrabber class to download specific file
for link in RawLinks:
    if "doku.php?id=item" in link.get("href"):
        print("<a href='%s'>%s</a>" % (link.get("href"), link.text))

# soup2 = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
# test_pull = soup.find(class_='BodyText')
# Pull text from all instances of <a> tag within BodyText div
# test_pull_items = test_pull.find_all('a.wikilink1')


# Create for loop to print out all artists' name
# for test_pull in test_pull_items:
#    print(test_pull.prettify())

# Sorting throught the list
for link in RawLinks:
    if "doku.php?id=item" in link.get("href"):
        # Call EdgeTiGrabber function
        # Transform EdgeTiGrabber into Class
