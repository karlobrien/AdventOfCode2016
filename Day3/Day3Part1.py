import sys
import numpy as np
import pandas as pd

input = open('/Users/karlobrien/projects/python/AdventOfCode2016/Day3/input.txt').read().split('\n')

result = sum(vals[0] + vals[1] > vals[2]
            for vals in [sorted([int(x) for x in line.split()])
            for line in input])

print result
