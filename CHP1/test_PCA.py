from PIL import Image
from numpy import *
from pylab import *
from imtools import *


def pca(X):
    num_data, dim = X.shape

    mean_X = X.mean(axis=0)
    X = X - mean_X

    if dim > num_data:
        M = dot(X, X.T)
        e, EV = linalg.eigh(M)
        tmp = dot(X.T, EV)
        V = tmp[::-1]
        S = sqrt(e)[::-1]
        for i in range(V.shape[1]):
            V[:,i] /= S

    else:

        U,S,V = linalg.svd(X)
        V = V[:num_data]

    return V,S,mean_X

def test_pca():
    data_path = '/media/freshield/COASAIR/LEARN_COMPUTER_VISION_PYTHON/example/data/a_thumbs/'
    imlist = get_imlist(data_path)

    im = array(Image.open(imlist[0]))
    m,n = im.shape[0:2]
    imnbr = len(imlist)

    immatrix = array([array(Image.open(im)).flatten() for im in imlist], 'f')

    V,S,immean = pca(immatrix)

    return V,S,immean

def test_show_pca():
    data_path = '/media/freshield/COASAIR/LEARN_COMPUTER_VISION_PYTHON/example/data/a_thumbs/'
    imlist = get_imlist(data_path)

    im = array(Image.open(imlist[0]))
    m,n = im.shape[0:2]
    imnbr = len(imlist)

    immatrix = array([array(Image.open(im)).flatten() for im in imlist], 'f')

    V,S,immean = pca(immatrix)

    figure()
    gray()
    subplot(2,4,1)
    imshow(immean.reshape(m,n))
    for i in range(7):
        subplot(2,4,i+2)
        imshow(V[i].reshape(m,n))

    show()