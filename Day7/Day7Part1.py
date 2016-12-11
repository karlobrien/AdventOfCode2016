import re
import sys

def isValid(n):
    result = any(a == d and b == c and a != b for a, b, c, d in zip(n, n[1:], n[2:], n[3:]))
    return result

file_name = '/Users/karlobrien/projects/python/AdventOfCode2016/Day7/input.txt'
#file_name = '/Users/karlobrien/projects/python/AdventOfCode2016/Day7/sample.txt'

tlsCount = 0
for line in open(file_name).read().split('\n'):
    reg = re.split('\[([^\]]+)\]', line)
    positivePart = ' '.join(reg[::2])
    negativePart = ' '.join(reg[1::2])
    if not isValid(negativePart) and isValid(positivePart):
        tlsCount = tlsCount + 1

print tlsCount