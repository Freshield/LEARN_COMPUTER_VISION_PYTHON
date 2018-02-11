import os
from PIL import Image
import numpy as np
from pylab import *

def get_imlist(path):

    """return all file name in the dir"""

    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im, sz):
    pil_im = Image.fromarray(uint8(im))

    try:
        pil_im = pil_im.resize(sz)
    except:
        print 'The resize same meet some problem...'

    return array(pil_im)

def histeq(im, nbr_bins=256):

    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]

    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf

def compute_average(imlist):

    averageim = array(Image.open(imlist[0]), 'f')
    sz = Image.open(imlist[0]).size
    print sz

    for imname in imlist[1:]:
        try:
            im_tmp = array(Image.open(imname))
            im_resize = imresize(im_tmp, sz)
            print im_resize.shape
            averageim += im_resize
        except:
            print imname + '...skipped'


    averageim /= len(imlist)

    return array(averageim, 'uint8')