import numpy as np
from pylab import *
from PIL import Image

data_path = '../example/data/'

im = array(Image.open(data_path + 'empire.jpg'))

im1 = array(Image.open(data_path + 'empire.jpg').convert('L'))

def test1():
    print im.shape, im.dtype
    print im1.shape, im1.dtype

    print im[:100,:50].sum()
    print im[100].mean()
    print im[:,-1]

def test2():
    figure(1)
    subplot(231)
    gray()
    imshow(im)
    subplot(232)
    gray()
    imshow(im1)

    im2 = 255 - im1
    subplot(233)
    gray()
    imshow(im2)

    im3 = (100. / 255) * im1 + 100
    subplot(234)
    gray()
    imshow(im3)

    im4 = 255. * (im1 / 255.) ** 2
    subplot(235)
    gray()
    imshow(im4)

    im5 = array(Image.fromarray(uint8(im2)))
    subplot(236)
    gray()
    imshow(im5)

    show()

test2()

