import numpy as np
from pylab import *
from PIL import Image
import imtools

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

def test3():
    im = array(Image.open(data_path + 'AquaTermi_lowcontrast.JPG').convert('L'))
    im2, cdf = imtools.histeq(im)

    figure()

    subplot(321)
    hist(im.flatten(), 128)

    subplot(322)
    hist(im2.flatten(), 128)

    subplot(323)
    imshow(im)
    gray()

    subplot(324)
    imshow(im2)
    gray()

    print cdf.shape
    subplot(325)
    plot(cdf)

    show()


test3()

