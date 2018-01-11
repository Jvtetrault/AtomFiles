import tkinter
import sys

print(sys.executable)
print(sys.version)

def doNothing():
    print("ok ok I won't...")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="Now Project...", command=doNothing)
subMenu.add_command(label="Now...", command=doNothing)
subMenu.add_seperator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=subMenu)
editMenu.add_command(label="Redo", command=doNothing)
root.mainloop()
