from PIL import Image
import pytesseract
from os import listdir
from os.path import isfile, join

path = './docs'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

name_coordinates = (362, 299, 198+362, 20+299)
school_coordinates = (616, 299, 198+616, 20+299)

for file in onlyfiles:
    im = Image.open("./docs/{}".format(file))
    print(im.format, im.size, im.mode)
    name_image = im.crop(name_coordinates)
    school_image = im.crop(school_coordinates)

    name = pytesseract.image_to_string(name_image, lang='eng')
    school = pytesseract.image_to_string(school_image, lang='eng')

    print(name, school)
