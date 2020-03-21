import os
import re
import sys
import time

import urllib

local_path = os.getcwd()
o_path = os.path.abspath(os.path.join(local_path, "../.."))
sys.path.append(o_path)

from src.core.pdf import creator


class PicDownload:
    def __init__(self, **info):
        for k, v in info.items():
            self.__setattr__(k, v)

    def download_pic(self):
        url_open1 = str(urllib.request.urlopen(self.url).read().decode("utf-8"))

        # Credits to https://txt2re.com/ for the regex (Almost all of it)
        # Sorry, I'm not lazy, but I hate making regex's
        re1 = '.*?'
        re2 = '((?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*)(?:png|jpg))'

        rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)
        m = rg.search(url_open1)
        if m:
            self.url = m.group(1)
            print('Starting from URI: ' + self.url)
        else:
            self.url = None
            print("Error! No image was found")

        print('Started download process...')
        # List to create the PDF
        files = []

        formatter = self.url.replace('page_1.jpg', '')
        for index in range(self.start, self.end + 1):
            jpg_url = formatter + 'page_%s.jpg' % index
            filename = o_path + '/pic/%s/%s.jpg' % (self.book_name, index)
            # Download images
            while True:
                try:
                    with open(filename, 'wb') as w_file:
                        w_file.write(urllib.request.urlopen(jpg_url).read())
                    break
                except Exception as e:
                    print(e)
                    print('retrying' + filename + ' From URI: ' + jpg_url)
                    time.sleep(5)
            print('Correctly saved file ' + filename + ' From URI: ' + jpg_url)
            files.append(filename)
            time.sleep(5)

        print('Completed download process...')
        # Time to create the pdf

    def create_pdf(self):
        creator(self.book_name)
