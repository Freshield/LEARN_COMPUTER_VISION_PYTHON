import pickle
import test_PCA as pca
import numpy as np

V,S,immean = pca.test_pca()

def test_dump():
    f = open('font_pca_modes.pkl', 'wb')
    pickle.dump(immean, f)
    pickle.dump(V, f)
    f.close()

def test_load():
    f = open('font_pca_modes.pkl', 'rb')
    immean = pickle.load(f)
    V = pickle.load(f)
    f.close()
    print immean.shape

def test_with_dump():
    with open('font_pca_modes.pkl', 'wb') as f:
        pickle.dump(immean, f)
        pickle.dump(V,f)

def test_with_load():
    with open('font_pca_modes.pkl', 'rb') as f:
        immean = pickle.load(f)
        V = pickle.load(f)
        print immean.shape

def test_numpy_save():
    np.savetxt('test.txt', immean, '%i')

def test_numpy_load():
    x = np.loadtxt('test.txt')
    print x.shape

test_numpy_load()