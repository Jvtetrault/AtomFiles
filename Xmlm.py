def write1(id, period, offset, task, help, name, files):
    Path = "C:/ProgramData/Inovatech Engineering Corp/SteelPRO Director/Documentation/Maintenance/en-US/"
    dest = str(Path + name + ".pdf")
    newtask = task.replace("&", "and")
    ID8 = id.encode("utf-8")
    PER8 = str(period)
    OFF8 = str(offset)
    TAS8 = newtask.encode("utf-8")
    HEL8 = help

    items = [ID8, PER8, OFF8, TAS8, HEL8, dest]
    titles = ["ID", "Period", "Offset", "Task", "Help", "URL"]


    openfile = open(files, "a")
    openfile.write(("  <Task>\n").encode("utf-8"))
    for i in range(len(items)):
        a = "    <" + titles[i] + ">" + items[i] + "</" + titles[i] + ">"
        openfile.write(a + "\n")
    openfile.write(("  </Task>\n").encode("utf-8"))


def build(path):
        destination = path + "/Maintenance.xml"
        file = open(destination, "w")
        file.write(('<?xml version="1.0" encoding="UTF-8"?>').encode("utf-8"))
        file.write("\n")
        file.write(("<Tasks>\n").encode("utf-8"))
        file.close()
        return str(destination)


def finish(files):
    openfile = open(files, "a")
    openfile.write(("  <Task>\n").encode("utf-8"))
    openfile.write(("    <ID/>\n").encode("utf-8"))
    openfile.write(("  </Task>\n").encode("utf-8"))
    openfile.write(("  <Task>\n").encode("utf-8"))
    openfile.write(("    <ID/>\n").encode("utf-8"))
    openfile.write(("  </Task>\n").encode("utf-8"))
    openfile.write(("  <Task>\n").encode("utf-8"))
    openfile.write(("    <ID/>\n").encode("utf-8"))
    openfile.write(("  </Task>\n").encode("utf-8"))
    openfile.write(("  <Task>\n").encode("utf-8"))
    openfile.write(("    <ID/>\n").encode("utf-8"))
    openfile.write(("  </Task>\n").encode("utf-8"))
    openfile.write(("</Tasks>").encode("utf-8"))
    openfile.close()
