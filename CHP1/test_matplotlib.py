from PIL import Image
from pylab import *
import numpy as np

data_path = '../example/data/'

im = array(Image.open(data_path + 'empire.jpg'))

def test0():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')

    show()


def test1():
    imshow(im)

    x = [100,100,400,400]
    y = [200,500,200,500]

    #plot(x,y,'r*')
    #plot(x,'r*')
    #plot(y,'g*')

    #plot(x[:2],y[:2])

    title('Plotting: "empire.jpg')

    #axis('off')

    show()

test0()