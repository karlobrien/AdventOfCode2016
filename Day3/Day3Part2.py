import sys
import numpy as np
import pandas as pd

file_name = '/Users/karlobrien/projects/python/AdventOfCode2016/Day3/input.txt'
txt = open(file_name).read()
input = txt.split('\n')

result = sum(vals[0] + vals[1] > vals[2]
            for vals in [sorted([int(x) for x in line.split()])
            for line in input])

print result

items = ['330 143 338', '769 547 83', '930 625 317']

import sys
from itertools import izip_longest

args = [iter([int(x) for x in line.split()] for line in items)] * 3

print sum(sum(y[0] + y[1] > y[2]
              for y in [sorted(tri) for tri in zip(*x)])
              for x in izip_longest(*args))

a = b = c = range(9)

combine = zip(a,b,c)
print combine

data = np.loadtxt(input).T.reshape(-1, 3).T
data.sort(axis=0)
print data
