import os

def get_imlist(path):

    """return all file name in the dir"""

    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]