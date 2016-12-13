import sys
import re

file_path = '/Users/karlobrien/projects/python/AdventOfCode2016/Day9/input.txt'

ex2 = '(3x3)XYZ'
ex3 = 'A(2x2)BCD(2x2)EFG'
ex4 = '(6x1)(1x3)A'
ex5 = 'X(8x2)(3x3)ABCY'

ex1 = 'A(1x5)BC'
reg = r'\((\d+)x(\d+)\)'

def BreakDown(line):
    byRegex = re.search(reg, line)
    if not byRegex:
        return len(line)
    else:
        firstPostion = byRegex.start(0) # Our first match
        lengthOfGroup = len(byRegex.group()) + firstPostion
        numberOfItems = int(byRegex.group(1))
        repeat = int(byRegex.group(2))
        first = len(line[:firstPostion])
        lengthOfRepeatingItems = len(line[lengthOfGroup:lengthOfGroup+numberOfItems] * repeat)
        segmentLength = first + lengthOfRepeatingItems
        return segmentLength + BreakDown(line[lengthOfGroup+numberOfItems:])

print 'Result:',  BreakDown(ex1)
print 'Result:',  BreakDown(ex2)
print 'Result:',  BreakDown(ex3)
print 'Result:',  BreakDown(ex4)
print 'Result:',  BreakDown(ex5)

r = open(file_path).read()
print BreakDown(r)