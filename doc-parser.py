import cv2
import numpy as np
import pytesseract
from os import listdir
from os.path import isfile, join

path = './docs'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

name_coordinates = (362, 299, 198, 20)
school_coordinates = (616, 299, 198, 20)

for file in onlyfiles:
    im = cv2.imread("{}/{}".format(path, file))

    x, y, w, h = name_coordinates
    name = pytesseract.image_to_string(im[y:y+h, x:x+w], lang='eng')

    x, y, w, h = school_coordinates
    school = pytesseract.image_to_string(im[y:y+h, x:x+w], lang='eng')

    print(name, school)
