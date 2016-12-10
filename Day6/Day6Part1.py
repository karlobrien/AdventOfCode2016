import sys
from collections import Counter

file_path = '/Users/karlobrien/projects/python/AdventOfCode2016/Day6/input.txt'

#with open(file_path) as file:
#    for line in file:

file = open(file_path).read()

data = [Counter(x).most_common() for x in zip(*file.split('\n'))]

for d in data:
    print d[-1][0]
    


