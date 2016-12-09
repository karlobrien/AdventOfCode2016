import re, string
from collections import Counter

file_path = '/Users/karlobrien/projects/python/AdventOfCode2016/Day4/input.txt'
sample = '/Users/karlobrien/projects/python/AdventOfCode2016/Day4/sample_input.txt'
sectorSum = 0

def myCypher(entry, n):
    num_chars = string.ascii_lowercase
    decrypted = ''
    for c in entry:
        if c == '-':
            decrypted = decrypted + ' '
        else:
            pos = num_chars.index(c) 
            shifted_forward =  n % len(num_chars)
            p = (shifted_forward + pos) % 26
            ch = num_chars[p]
            decrypted = decrypted + ch
    return decrypted

def parse(name):
    regex = r'([a-z-]+)(\d+)\[(\w+)\]'
    with open(name) as file:
        for code, sectorId, chk in re.findall(regex, file.read()):
            secID = int(sectorId)
            decoded = myCypher(code, secID)
            if 'north' in decoded:
                print decoded, secID

parse(file_path)