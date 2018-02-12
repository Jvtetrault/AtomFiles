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


# print(sys.executable)
# print(sys.version)


url = "http://wiki.inovkh.com/doku.php?id=xpr_component_table"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

tdTest = soup.find_all('td')
AllTitle = soup.find_all('td', "col3")
AllDura = soup.find_all('td', "col1")
AllDelay = soup.find_all('td', "col2")
RawLinks = soup.find_all("a")

# none valid expression, url is not passed yet as HMTL content
pudding = BeautifulSoup(url, "html.parser")


# lobbying = {}
# for element in tdTest:
#     lobbying[element.a.get_text()] = {}
#
# tdTest[0].a["href"]
def getLink(name):
    if link in name.get('href'):
        if "/doku.php?id=item" in link.get("href"):
            print(link.get("title"))

# Testing Objects (call these to test different parsing HLTM methods from
# BeautifulSoup4


def test1():
    for tr in tdTest:
        for td in tr.descendants:
            print(td)

# Test 2 <td class="col3">Visual inspection for drops</td>


def test2():
    print(AllTitle)

# Test 3 Prints form <td class="col1"> Daily </td>, <td class="col1 centeralign">


def test3():
    print(AllDura)

# Test 3 Result Link is not defined*


def test4():
    getLink(tdTest)

# Test 5 prints form  <td class="col2"> - </td>, <td class="col2 centeralign">


def test5():
    print(AllDelay)

# Test 6 Will need more time to sift throught output properly


def test6():
    print(RawLinks)

# Test 8 Failed, HTML tree was not printed: USERWARNING: URL looks like a url
# "Beautiful Soup is not an HTTP client. You should probably use an HTTP client
# like requests to get the docuement behind the URL, and feed that document to
# Beatuiful Soup."


def test8():
    hey = page.prettify()
    print(hey)


def test9():
    for td in soup.find_all('tr'):
        print (td.get_text())

def test10():
    for string in soup.find_all('tr'):
        for Link in string:
            print(Link)

def test11():
    print (soup.find('td', "Visual inspection for drops"))



test10()

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
