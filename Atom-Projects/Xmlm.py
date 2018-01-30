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


def write(id, period, offset, task, help, url):
    the_doc = ROOT(
        DOC(
            ID(str(id)),
            Period(str(period)),
            Offset(str(offset)),
            Task(str(task)),
            Help(str(help)),
            URL(str(url))
        )
    )

    print lxml.etree.tostring(the_doc, pretty_print=True)


write(1, 2, 3, 4, 5, 6)

tree.write(open(r 'C:\maintenance.xml', 'w'))
