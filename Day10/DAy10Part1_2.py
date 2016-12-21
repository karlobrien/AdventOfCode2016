from collections import defaultdict

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

complete = set()
myState = defaultdict(list)
output = defaultdict(list)

while len(complete) < len(input):
    for line in input:
        if line in complete:
            continue

        if 'value' in line:
            [number, toBot] = parseValue(line)
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

        if lowDesc.startswith('out'):
            output[lowBot].append(currentLBot)
        else:
            myState[lowBot].append(currentLBot)

        if highDesc.startswith('out'):
            output[highBot].append(currentHBot)
        else:
            myState[highBot].append(currentHBot)

        complete.add(line)

for x in myState:
    for y in myState[x]:
        print x, y
    print "---"