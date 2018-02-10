#!/usr/bin/python
import lxml.etree
import lxml.builder
from lxml import etree
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree


E = lxml.builder.ElementMaker()
ROOT = E.Tasks
DOC = E.Task
ID = E.ID
Period = E.Period
Offset = E.Offset
Task = E.Task
Help = E.Help
URL = E.URL


# Testing Parameter
murl = "https://docs.python.org/2/library/xml.etree.elementtree.html"


def write(id, period, offset, task, help, url):
    # Path = "C:/ProgramData/Inovatech Engineering Corp/SteelPRO Director/Documentation/Maintenance/en-US/"
    # dest = Path + url

    the_doc = ROOT(
        DOC(
            ID(str(id)),
            Period(str(period)),
            Offset(str(offset)),
            Task(str(task)),
            Help(str(help)),
            # URL(str(dest))

        )
    )


    print lxml.etree.tostring(the_doc, pretty_print=True)
    print type(lxml.etree.tostring(the_doc, pretty_print=True))

write(0,0,0,0,0,1)
