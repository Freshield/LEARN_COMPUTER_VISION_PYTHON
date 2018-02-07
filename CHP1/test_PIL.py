from PIL import Image
from pylab import *
import os

data_path = "../example/data/"

def test1():
    pil_im = Image.open(data_path + 'empire.jpg').convert('L')

    im = array(pil_im)

    imshow(im)

    show()

def test2():
    outfile = 'test.jpg'
    infile = Image.open(data_path + 'empire.jpg').convert('L')
    try:
        infile.save(outfile)
    except IOError:
        print'cannot convert', infile

test2()