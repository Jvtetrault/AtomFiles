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


def write1(id, period, offset, task, help, name, file):
    Path = "C:/ProgramData/Inovatech Engineering Corp/SteelPRO Director/Documentation/Maintenance/en-US/"
    dest = str(Path + name)


    the_doc = ROOT(
        DOC(
            ID(str(id)),
            Period(str(period)),
            Offset(str(offset)),
            Task(str(task)),
            Help(str(help)),
            URL(str(dest))

        )
    )
    print lxml.etree.tostring(the_doc, pretty_print=True)
    file.Element.append(str(id))


def build(path):
        destination = path + "/Maintenance.xml"
        file = open(destination, "w")
        file.write('<?xml version="1.0" encoding="UTF-8"?>')
        return str(destination)
        # root = etree.Element("Tasks")
        # tree = etree.ElementTree(root)
        # tree.write("C:/Users/Jonathan Tetrault/Desktop/New folder/filename.xml")


# print(build("C:\Users\Jonathan Tetrault\Desktop"))
