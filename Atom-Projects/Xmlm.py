#!/usr/bin/python
# import lxml.etree
# import lxml.builder
# from lxml import etree
# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import ElementTree
# from xml.etree.ElementTree import Element


# E = lxml.builder.ElementMaker()
# ROOT = E.Tasks
# DOC = E.Task
# ID = E.ID
# Period = E.Period
# Offset = E.Offset
# Task = E.Task
# Help = E.Help
# URL = E.URL


def write1(id, period, offset, task, help, name, files):
    Path = "C:/ProgramData/Inovatech Engineering Corp/SteelPRO Director/Documentation/Maintenance/en-US/"
    dest = str(Path + name)

    items = [id, period, offset, task, help, dest]
    titles = ["ID", "Period", "Offset", "Task", "Help", "URL"]

    # openfile = open(files, 'a')
    # tree = ET.parse(openfile)
    # root = tree.getroot()
    #
    # doc = root.append("Task")
    openfile = open(files, "a")
    openfile.write("  <Task>\n")
    for i in range(len(items)):
        a = "    <" + titles[i] + ">" + items[i] + "</" + titles[i] + ">"
        openfile.write(a + "\n")
    openfile.write("  </Task>\n")



    # tree = etree.parse(files)
    # root = tree.getroot()

    # a = root.find('Tasks')
    # Doc = a.etree.SubElement("Task")
    # ID = etree.SubElement(Doc, str(id))
    # Period = etree.SubElement(Doc, str(period))
    # Task = etree.SubElement(Doc, str(task))
    # Help = etree.SubElement(Doc, str(help))
    # Name = etree.SubElement(Doc, str(name))





    # the_doc = ROOT(
    #     DOC(
    #         ID(str(id)),
    #         Period(str(period)),
    #         Offset(str(offset)),
    #         Task(str(task)),
    #         Help(str(help)),
    #         URL(str(dest))
    #
    #     )
    # )
    # print lxml.etree.tostring(the_doc, pretty_print=True)


def build(path):
        destination = path + "/Maintenance.xml"
        file = open(destination, "w")
        file.write('<?xml version="1.0" encoding="UTF-8"?>')
        file.write("\n")
        file.write("<Tasks>\n")
        file.close()
        return str(destination)
        # root = etree.Element("Tasks")
        # tree = etree.ElementTree(root)
        # tree.write("C:/Users/Jonathan Tetrault/Desktop/New folder/filename.xml")

def finish(files):
    openfile = open(files, "a")
    openfile.write("</Tasks>")
    openfile.close()


# do = build("C:\Users\Jonathan Tetrault\Desktop")
# write1("1","1","1","1",'PDF',"1",do)
# finish(do)
