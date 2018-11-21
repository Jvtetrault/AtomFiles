from clint.textui import progress
import requests
import sys


def pbar(path, url):


    response = requests.get(url, stream=True, timeout=100)
    if response.ok:
        with open(path, "wb") as f:
            print "Downloading %s" % path
            total_length = int(response.headers.get('content-length'))

            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50*dl/total_length)
                    sys.stdout.write("\r[%s%s]" % ('#' * done, ' '*(50-done)))
                    sys.stdout.flush()
    else:
        print("Failed to download: " + str(path))
