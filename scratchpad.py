import sys
from itertools import izip_longest
import numpy as np
import pandas as pd

a = b = c = range(9)

combine = zip(a,b,c)
print combine

data = np.array(combine).T.reshape(-1, 3).T
data.sort(axis=0)
print data

print '----- iter ----'
print '--This allow us to iter over a step'
args = [iter (int(x) for x in a)] * 2
for x in izip_longest(*args):
    print x

