import sys
import re
from collections import defaultdict

#only process when you have two processors
#dict of bot name => tuple of chips

#process and add values checking for two entries
# if two entries, 

file_name = '/Users/karlobrien/projects/python/AdventOfCode2016/Day10/input.txt'

ex1 = 'value 5 goes to bot 2'
ex2 = 'bot 2 gives low to bot 1 and high to bot 0'
ex3 = 'value 3 goes to bot 1'
ex4 = 'bot 1 gives low to output 1 and high to bot 0'
ex5 = 'bot 0 gives low to output 2 and high to output 0'
ex6 = 'value 2 goes to bot 2'

def parseValue(entry):
    divide = entry.split(' ')
    return (divide[1], divide[5])

def compareEntries(one, two):
    if one < two:
        return (one, two)
    return (two, one)

input = open(file_name).read().split('\n')
items = [ex1, ex2, ex3, ex4, ex5, ex6]

#items = input

commands = {}
output = {}
result = {}

for i in items:
    if 'value' in i:
        number, bot = parseValue(i)
        if bot not in result:
            result[bot] = number
        else:
            value = result[bot]
            result[bot] = compareEntries(value, number)
            if len(result[bot]) == 2:
                cmd = commands[bot]       
                if cmd[0] == 'output':
                    l, h = output[bot]
                    output[bot] = (result[bot][0], h)
                if cmd[2] == 'output':
                    l, h = output[bot]
                    output[bot] = (l, result[bot][1])
                if cmd[0] == 'bot':
                    l, h = result[bot]
                    toLowBot = cmd[1]
                    ll, hh = result[toLowBot]
                    result[toLowBot] = compareEntries(l, hh)
                if cmd[2] == 'bot':
                    l, h = result[bot]
                    toHighBot = cmd[3]
                    ll, hh = result[toHighBot]
                    result[toHighBot] = compareEntries(ll, h)
                commands[bot] = ()
    else:
        cmd = i.split(' ')
        fromBot = cmd[1]
        lowDesc = cmd[5]
        lowBot = cmd[6]
        highDesc = cmd[10]
        highBot = cmd[11]
        commands[fromBot] = (lowDesc, lowBot, highDesc, highBot)

#ex2 = 'bot 2 gives low to bot 1 and high to bot 0 '
print result
print commands
