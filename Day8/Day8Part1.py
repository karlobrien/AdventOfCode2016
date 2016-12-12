import sys
import numpy as np
import pandas as pd

file_path = '/Users/karlobrien/projects/python/AdventOfCode2016/Day8/input.txt'
grid = np.zeros((6, 50), dtype=bool)

with open(file_path) as fp:
    for line in fp.readlines():
        lineSplit = line.split(' ')
        if lineSplit[0] == 'rect':
            wide, tall = map(int, lineSplit[1].split('x'))
            grid[:tall, :wide] = True
        elif lineSplit[0] == 'rotate':
            shift = int(lineSplit[4])
            location = int(lineSplit[2].split('=')[1])
            if lineSplit[1] == 'row':
                grid[location] = np.roll(grid[location], shift)
            else:
                grid[:, location] = np.roll(grid[:, location], shift)

print grid
print np.sum(grid)



x = np.arange(10)
print x
x[:5] = 20
print x
#print np.roll(x, 2)
#print np.roll(grid, 2, axis=1)
