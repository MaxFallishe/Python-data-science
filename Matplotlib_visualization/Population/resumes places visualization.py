import os
import tarfile
from six.moves import urllib
import numpy as np

RESUMES_PATH = os.path.join("datasets")


def fetch_resumes_data(resumes_path = RESUMES_PATH):
    if not os.path.isdir(resumes_path):
        os.makedirs(resumes_path)


fetch_resumes_data()

import pandas as pd

pd.set_option('display.expand_frame_repr', False)


def load_resumes_data(resumes_path = RESUMES_PATH):
    csv_path = os.path.join(resumes_path,'resumes_v3.csv')
    return pd.read_csv(csv_path, encoding='latin-1')

resumes = load_resumes_data()


import matplotlib.pyplot as plt

from sklearn.model_selection import StratifiedShuffleSplit


def pltcolor(lst):
    cols=[]
    for l in lst:
        if l=="computerprogrammer":
            cols.append('red')
        else:
            cols.append('green')
    return cols


cols = pltcolor(resumes["profession"])
resumes.plot(kind="scatter", x="longitude", y ="latitude",c = cols, alpha=0.5)
x = resumes["longitude"]
y = resumes["latitude"]
#plt.xticks(np.arange(min(x), max(x)+1,50))
#plt.yticks(np.arange(min(y), max(y)+1,25))
plt.savefig("1_visualization_plot")
plt.show()












