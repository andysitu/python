import ffile

try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract
import re
import os, time, os.path

def get_img_string(filename):
    if not filename.endswith('.jpg'):
        msg = filename + " is not a jpg file."
        raise Exception(msg)
    img_string = pytesseract.image_to_string(Image.open(filename))
    return img_string

ffile.move_dir("jpg_raw")

file_list = os.listdir()

for filename in file_list:

    img_string = get_img_string(filename)

    pattern = re.compile("RCV\d+-\d+")

    re_result = pattern.search(img_string)

    if re_result != None:
        new_filename = ''
        for i in range(0, 100):
            new_filename = re_result[0] + '_' + str(i) + '.jpg'
            if not os.path.isfile(new_filename):
                break

        os.rename(filename, new_filename)

ffile.dir_back()