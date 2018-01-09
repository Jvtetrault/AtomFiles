from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw()
filename = askdirectory()
print(filename)
