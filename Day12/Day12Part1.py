import sys
import os
from collections import defaultdict

registers = defaultdict(int)
registers['c'] = 1
this_dir = os.path.dirname(__file__)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def figureJump(s):
    try:
        return int(s)
    except:
        return registers[s]

with open(os.path.join(this_dir, 'input.txt')) as f:
    data = f.read().split('\n')

    size = len(data)
    print size
    counter = 0

    while counter < size:
        currentInstr = data[counter]
        breakout = currentInstr.split(' ')

        if breakout[0] == 'cpy':
            toRegister = breakout[2]
            value = breakout[1]
            if is_number(value):
                registers[toRegister] = int(value)
            else:
                copyVal = registers[value]
                registers[toRegister] = copyVal
        elif breakout[0] == 'inc':
            registers[breakout[1]]+=1
        elif breakout[0] == 'dec':
            registers[breakout[1]]-=1
        elif breakout[0] == 'jnz':
            x = figureJump(breakout[1])
            if (x != 0):
                counter += figureJump(breakout[2])
                counter = counter - 1
        counter += 1

print registers