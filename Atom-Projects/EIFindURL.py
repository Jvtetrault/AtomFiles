import requests
from bs4 import BeautifulSoup
import sys

print(sys.executable)
print(sys.version)

# Transforms HTML Tree into easily navigatable Python Tree.
# Beginning of Tree Parsing to find specific objects
url = "http://wiki.inovkh.com/doku.php?id=xpr_component_table"
page = requests.get(url)
soup = BeautifulSoup(page.content)

# Finds all links in page
RawLinks = soup.find_all("a")

# Only uses links to maintenance manual
for link in RawLinks:
    if "http" in link.get("href"):
        print("<a href='%s'>%s</a>" % (link.get("href"), link.text))

# soup2 = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
# test_pull = soup.find(class_='BodyText')
# Pull text from all instances of <a> tag within BodyText div
# test_pull_items = test_pull.find_all('a.wikilink1')


# Create for loop to print out all artists' name
# for test_pull in test_pull_items:
#    print(test_pull.prettify())
