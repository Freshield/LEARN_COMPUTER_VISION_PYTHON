from PIL import Image
from pylab import *
import os

data_path = "../example/data/"

pil_im = Image.open(data_path + 'empire.jpg')

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

def test3():
    pil_im = Image.open(data_path + 'empire.jpg')

    print(pil_im)

    pil_im.thumbnail((128,128))

    print(pil_im)

    imshow(pil_im)

    show()

def test4():
    box = (100,100,400,400)
    region = pil_im.crop(box)
    region = region.transpose(Image.ROTATE_180)
    pil_im.paste(region,box)
    imshow(pil_im)
    show()

def test5():
    out = pil_im.resize((128,128))
    print(out.size)
    out2 = out.rotate(45)
    print(out2.size)
    imshow(out2)
    show()

test5()