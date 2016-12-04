import numpy as np
import sys

advancedPad = np.array([['NA', 'NA', '1', 'NA', 'NA'],
                        ['NA', '2', '3', '4', 'NA'],
                        ['5', '6', '7', '8', '9'],
                        ['NA', 'A', 'B', 'C', 'NA'],
                        ['NA', 'NA', 'D', 'NA', 'NA'],])

print advancedPad

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
        if derivedCol <= 4:
            return (derivedRow, derivedCol)
        else:
            return (row, col)
    if d == 'D':
        derivedRow = row + 1
        derivedCol = col
        if derivedRow <= 4:
            return (derivedRow, derivedCol)
        else:
            return (row, col)

x, y = (2, 0)
print advancedPad[x][y]

input = open('/Users/karlobrien/projects/python/AdventOfCode2016/Day2/input.txt').read().split(',')

for item in input:
    for c in item:
        newX, newY = CalCoord(x, y, c)
        advancedPAdValue = advancedPad[newX][newY]
        if advancedPAdValue != 'NA':
            x, y = newX, newY
    print '--- Row complete --', advancedPad[x][y]

