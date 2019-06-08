"""
doc_parser
this script will remove the unnecessery background from the scanned picture
and parse the text in predifined coordinates
"""

from os import listdir
from os.path import isfile, join
import cv2
import numpy as np
import pytesseract

CONFIG = dict({
    'name': (362, 299, 198, 20),
    'school': (616, 299, 198, 20)
})

PATH = './docs'
IMAGE_FILES = [f for f in listdir(PATH) if isfile(join(PATH, f))]

for file in IMAGE_FILES:
    img = cv2.imread("{}/{}".format(PATH, file), cv2.IMREAD_UNCHANGED)

    # convert img to grey
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # set a thresh
    thresh = 26
    ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

    # find where the white pixels are
    points = np.argwhere(thresh_img == 255)
    # store them in x,y coordinates instead of row,col indices
    points = np.fliplr(points)
    # create a rectangle around those points
    x, y, w, h = cv2.boundingRect(points)

    # remove unnecunnecessary background
    # img = img[y:y+h, x:x+w]

    parsed_results = dict()
    for param in CONFIG:
        x, y, w, h = CONFIG[param]
        parsed_results[param] = pytesseract.image_to_string(img[y:y+h, x:x+w], lang='eng')

    print(parsed_results)
