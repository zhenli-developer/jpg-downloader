import os
import re
import sys
import urllib

local_path = os.getcwd()
o_path = os.path.abspath(os.path.join(local_path, "../.."))
sys.path.append(o_path)

from src.core.downloader import PicDownload


def main():
    print("Starting...\n")
    # url = input("Enter the url of the PDF:")
    url = 'https://issuu.com/nat_arc/docs/bioplastic_cook_book_3'
    book_name = url.split('/')[-1]
    start, end = 1, 17
    # start = int(input("Page Start:"))
    # end = int(input("Page End:"))
    try:
        os.mkdir(o_path + '/pic/' + book_name)
    except:
        pass
    # Check that the URL provided by the user points to the entire document
    # and not to a specific page (e.g. https://issuu.com/user/docs/doc
    # instead of https://issuu.com/user/docs/doc/18)
    # url_end = re.search(r'(.+)/\d+/?$', url)
    # if url_end:
    #     # If there is a page number at the end of the URL
    #     print('The URL provided points to a specific page in the document.')
    #     url_without_page_number = url_end.group(1)
    #     print('Using the following URL instead:')
    #     print(url_without_page_number)
    #     url = url_without_page_number
    # else:
    #     # If the URL points to the entire document, without any page number
    #     pass

    pd = PicDownload(url=url, book_name=book_name, start=start, end=end)
    pd.download_pic()
    pd.create_pdf()


if __name__ == '__main__':
    main()
