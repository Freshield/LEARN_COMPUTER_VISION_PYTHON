from PIL import Image
from pylab import *
import numpy as np

data_path = '../example/data/'

im = array(Image.open(data_path + 'empire.jpg'))

def test0():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.title(r'$\sigma_i=15$')
    plt.show()



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