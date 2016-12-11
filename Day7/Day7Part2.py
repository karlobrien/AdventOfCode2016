import re
import sys

def isValid(pos, neg):

    result = any(a == c and a != b and b+a+b in neg for a, b, c in zip(pos, pos[1:], pos[2:]))
    return result

file_name = '/Users/karlobrien/projects/python/AdventOfCode2016/Day7/input.txt'

tlsCount = 0
for line in open(file_name).read().split('\n'):
    reg = re.split('\[([^\]]+)\]', line)
    positivePart = ' '.join(reg[::2])
    negativePart = ' '.join(reg[1::2])
    if isValid(positivePart, negativePart):
        tlsCount = tlsCount + 1

print tlsCount