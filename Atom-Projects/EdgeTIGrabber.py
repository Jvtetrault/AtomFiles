import requests
import time
import errno
import os


def getFile(ChosenUrl, Chosenlocation):
    baseFolder = Chosenlocation
    pic_url = ChosenUrl
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
        response = requests.get(pic_url, stream=True, timeout=2)

        if response.ok:
            with open(fullPicPath, 'wb') as handle:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
    except:
        print('fail')
