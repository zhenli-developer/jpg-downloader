import os
import sys

from PIL import Image

local_path = os.getcwd()
o_path = os.path.abspath(os.path.join(local_path, "../.."))
sys.path.append(o_path)


def creator(book_name):
    image_list = []
    length = len(os.listdir(o_path + '/pic/%s/' % book_name))
    for index in range(1, length + 1):
        filename = o_path + '/pic/%s/%s.jpg' % (book_name, index)
        image = Image.open(filename).convert('RGB')
        image_list.append(image)
    image_list[0].save(o_path + '/pdf/%s.pdf' % book_name, save_all=True, append_images=image_list[1:])
    print("Finished PDF File :", o_path + '/pdf/%s.pdf' % book_name)


if __name__ == "__main__":
    book_name_list = ['rapport_upload_issue', 'sustainable_fashion_-_new_approches',
                      'the-recycling-myth-malaysia-and-the', 'the_secrets_of_bioplastic_']
    for book in book_name_list:
        creator(book)
