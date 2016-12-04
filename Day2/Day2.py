import numpy as np
import sys

def CalCoord(row, col, d):
    if d == 'U':
        derivedRow = row - 1
        derivedCol = col
        if derivedRow >= 0:
            return (derivedRow, derivedCol)
        else:
            return (row, col)
    if d == 'L':
        derivedRow = row
        derivedCol = col - 1
        if derivedCol >= 0:
            return (derivedRow, derivedCol)
        else:
            return (row, col)
    if d == 'R':
        derivedRow = row
        derivedCol = col + 1
        if derivedCol <= 2:
            return (derivedRow, derivedCol)
        else:
            return (row, col)
    if d == 'D':
        derivedRow = row + 1
        derivedCol = col
        if derivedRow <= 2:
            return (derivedRow, derivedCol)
        else:
            return (row, col)

pad = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print pad

ex = "ULL;RRDDD;LURDL;UUUUD"

input = open('/Users/karlobrien/projects/python/AdventOfCode2016/Day2/input.txt').read().split(',')

#need to link char to bytearray
# U, (0, -1)
# L, (-1, 0)
# R, (1, 0)
# D, (0, 1)
# check if within bounds of array

lineByLine = input
#ex.split(',')

x, y = (1, 1)

for item in lineByLine:
    for c in item:
        x, y = CalCoord(x, y, c)
        #print c
        #print pad[x][y]
    print '--- Row complete --', pad[x][y]

