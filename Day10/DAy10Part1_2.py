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

def parseCmd(entry):
    cmd = entry.split(' ')
    return cmd[1], cmd[5], cmd[6], cmd[10], cmd[11]

input = open(file_name).read().split('\n')
items = [ex1, ex2, ex3, ex4, ex5, ex6]
#input = items

state = defaultdict(list)
commands = defaultdict(list)

for line in items:
    if 'value' in line:
        number, toBot = parseValue(line)
        #print number, toBot    
        lenOfToBot = len(state[toBot])
        if lenOfToBot == 0:
            state[toBot].append(number)
        elif lenOfToBot == 1:
            state[toBot].append(number)
            sorted(state[toBot])
        else:
            #execute command and clear
            print 'execute command'
            #botCmds = commands[]

    else:
        fromBot, lowDesc, lowBot, highDesc, highBot = parseCmd(line)
        commands[fromBot] = (lowDesc, lowBot, highDesc, highBot)

#print state
#print commands

allCommands = defaultdict(list)
for line in input:
    if 'value' not in line:
        fromBot, lowDesc, lowBot, highDesc, highBot = parseCmd(line)
        allCommands[fromBot] = (lowDesc, lowBot, highDesc, highBot)

for line in input:
    if 'value' in line:
        number, toBot = parseValue(line)

        lenOfToBot = len(state[toBot])
        if lenOfToBot == 0:
            state[toBot].append(number)
        elif lenOfToBot == 1:
            state[toBot].append(number)
            sorted(state[toBot])
        else:
            #execute command and clear
            print 'execute command'
            #botCmds = commands[]

complete = set()
myState = defaultdict(list)
output = defaultdict(list)

while len(complete) < len(input):
    for line in input:
        if line in complete:
            continue
        if 'value' in line:
            number, toBot = parseValue(line)
            myState[toBot].append(number)
            complete.add(line)
            continue

        #parse the command here
        fromBot, lowDesc, lowBot, highDesc, highBot = parseCmd(line)
        thisBot = myState[fromBot]

        if len(thisBot) < 2:
            continue

        currentLBot = min(thisBot)
        currentHBot = max(thisBot)

        if lowDesc == 'output':
            output[lowBot].append(currentLBot)
        else:
            myState[lowBot].append(currentLBot)

        if highDesc == 'output':
            output[highBot].append(currentHBot)
        else:
            myState[highBot].append(currentHBot)

        complete.add(line)

for x in myState:
    for y in myState[x]:
        print x, y
    print "---"

print output