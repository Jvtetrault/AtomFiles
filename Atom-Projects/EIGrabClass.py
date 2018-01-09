import requests
import time
import errno
import os
from Tkinter import Tk
from tkFileDialog import askdirectory


class EIGrab:


    pic_url = raw_input("Please copy the url of the table you would like to extract the pdf documents from")
    Tk().withdraw()
    location = askdirectory()
    # pic_url = "http://wiki.inovkh.com/doku.php?id=item_00014602"
    addPDFExport = "&do=export_pdf"
    PDFURL = pic_url + addPDFExport
    print(PDFURL)


    baseFolder = location
    datestr = time.strftime("%Y%m%d")
    timestr = time.strftime("%H%M%S") + '.pdf'

    def mkdir_p(path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

# figure out where to save the screengrab
    dayPath = os.path.join(baseFolder, datestr)
    fullPicPath = os.path.join(dayPath, timestr)

    mkdir_p(dayPath)

# Get the image from the edgeTi web app and save to computed location
    try:
        response = requests.get(PDFURL, stream=True, timeout=2)

        if response.ok:
            with open(fullPicPath, 'wb') as handle:
                for block in response.iter_content(1024):
                    if not block:
                        break
                        handle.write(block)
    except:
        print('fail')

    pass
