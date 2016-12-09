import re, string
from collections import Counter

file_path = '/Users/karlobrien/projects/python/AdventOfCode2016/Day4/input.txt'
sample = '/Users/karlobrien/projects/python/AdventOfCode2016/Day4/sample_input.txt'
input = open(file_path).read().split('\n')

sectorSum = 0

def myCypher(n):
    num_chars = string.ascii_lowercase
    shifted_forward =  n % len(num_chars)
    ch = num_chars[shifted_forward]
    print ch

for line in input:
    parsed = line.split('-')
    sectorAndChk = parsed[-1].split('[')

    sectorId = int(sectorAndChk[0])
    checkSum = sectorAndChk[1][:-1]
    encryptedName = parsed[:-1]

    sortedLetters = filter(lambda x: x != '-', encryptedName)
    concat = [x for sublist in sortedLetters for x in sublist]
    test = sorted(concat)
    items = [(-n, c) for c,n in Counter(test).most_common()]
    inOrder = ''.join(j for i, j in sorted(items))

    if inOrder.startswith(checkSum):
        sectorSum += sectorId
        

print sectorSum

#from https://www.reddit.com/r/adventofcode/comments/5gdvve/2016_day_4_solutions/
ans1 = 0
regex = r'([a-z-]+)(\d+)\[(\w+)\]'
with open(file_path) as fp:
    for code, sid, checksum in re.findall(regex, fp.read()):
        sid = int(sid)
        letters = ''.join(c for c in code if c in string.ascii_lowercase)
        tops = [(-n,c) for c,n in Counter(letters).most_common()]
        ranked = ''.join(c for n,c in sorted(tops))
        if ranked.startswith(checksum):
            ans1 += sid

print ans1

myCypher(123)

