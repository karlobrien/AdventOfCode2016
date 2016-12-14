import sys
import re

file_path = '/Users/karlobrien/projects/python/AdventOfCode2016/Day9/input.txt'

ex1 = '(3x3)XYZ' #XYZXYZXYZ
ex2 = 'X(8x2)(3x3)ABCY' #XABCABCABCABCABCABCY
ex3 = '(27x12)(20x12)(13x14)(7x10)(1x12)A' #A repeated 241920 times
ex4 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN' #445 long

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
        return first + BreakDown(line[lengthOfGroup:lengthOfGroup+numberOfItems]) * repeat + BreakDown(line[lengthOfGroup+numberOfItems:])

print 'Result:',  BreakDown(ex1)
print 'Result:',  BreakDown(ex2)
print 'Result:',  BreakDown(ex3)
print 'Result:',  BreakDown(ex4)

r = open(file_path).read()
print BreakDown(r)