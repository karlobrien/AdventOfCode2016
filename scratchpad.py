import sys
import numpy as np
import pandas as pd

a = b = c = range(9)

combine = zip(a,b,c)
print combine

data = np.loadtxt(input).T.reshape(-1, 3).T
data.sort(axis=0)
print data