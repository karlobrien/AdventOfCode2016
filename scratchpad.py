import sys
from itertools import izip_longest
import numpy as np
import pandas as pd

a = b = c = range(9)

print '---- Zip example ---'
combine = zip(a,b,c)
print combine

print '---- Numpy to reshape an array ----'
data = np.array(combine).T.reshape(-1, 3).T
data.sort(axis=0)
print data

print '----- iter ----'
print '--- We can also iter through a file and zip the contents'
print '-- ie. for z in zip(*file.split())'
print '--This allow us to iter over a step'
args = [iter (int(x) for x in a)] * 2
for x in izip_longest(*args):
    print x


print '--- List Comprehension example -----'
a_list = [1, 4, 9, 0, 4]
squared_ints = [ e**2 for e in a_list if e > 2]
print squared_ints

print '---- Lamda Example ----'
print map(lambda e: e**2, a_list)
print map(lambda e: e**2, filter(lambda e: e>2 ,a_list))

# filer from list
print '--- Filter from list ---'
letters = 'den-ags-df'
items = filter(lambda x: x != '-', letters)

# flatten a list
print '--- Flatten the list ----'
sortedLetters = ['abc', 'fwe', 'cewf']
flatten = [x for sublist in sortedLetters for x in sublist]
print flatten



