import os
from PIL import Image
import numpy as np
from pylab import *

def get_imlist(path):

    """return all file name in the dir"""

    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im, sz):
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))