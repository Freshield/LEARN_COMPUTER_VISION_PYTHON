from PIL import Image
from pylab import *
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

data_path = '../example/data/'

im = array(Image.open(data_path + 'empire.jpg'))

def test0():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # make up some data in the interval ]0, 1[
    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[(y > 0) & (y < 1)]
    y.sort()
    x = np.arange(len(y))

    # plot with various axes scales
    plt.figure(1)

    # linear
    plt.subplot(221)
    plt.plot(x, y)
    plt.yscale('linear')
    plt.title('linear')
    plt.grid(True)

    # log
    plt.subplot(222)
    plt.plot(x, y)
    plt.yscale('log')
    plt.title('log')
    plt.grid(True)

    # symmetric log
    plt.subplot(223)
    plt.plot(x, y - y.mean())
    plt.yscale('symlog', linthreshy=0.01)
    plt.title('symlog')
    plt.grid(True)

    # logit
    plt.subplot(224)
    plt.plot(x, y)
    plt.yscale('logit')
    plt.title('logit')
    plt.grid(True)
    # Format the minor tick labels of the y-axis into empty strings with
    # `NullFormatter`, to avoid cumbering the axis with too many labels.
    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    # Adjust the subplot layout, because the logit one may take more space
    # than usual, due to y-tick labels like "1 - 10^{-3}"
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)

    plt.show()



def test1():
    imshow(im)

    x = [100,100,400,400]
    y = [200,500,200,500]

    plot(x,y,'ks')
    #plot(x,'r*')
    #plot(y,'g*')

    plot(x[:2],y[:2])

    title('Plotting: "empire.jpg')

    #axis('off')

    show()

def test2():
    im = array(Image.open(data_path + 'empire.jpg').convert('L'))

    figure(1)

    gray()

    contour(im, origin='image')
    axis('equal')
    axis('off')

    figure(2)

    hist(im.flatten(), 128)


    show()

def test3():
    t = np.arange(10)
    plt.plot(t, np.sin(t))
    print("Please click")
    x = plt.ginput(3)
    print("clicked", x)
    plt.show()




test3()