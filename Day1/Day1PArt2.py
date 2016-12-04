#Build facing Index

# North 0 L: -1, R = 1
# East 1 L: 1, R = -1
# South 2 L: 1, R = -1
# West 3 L: -1, R = 1

input = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"

ex1 = "R2, L3"
ex2 = "R2, R2, R2"
ex3 = "R5, L5, R5, R3"

part2 = "R8, R4, R4, R8" 
instructions = input.split(', ')

visitedSet = set()
x, y = 0, 0
visitedSet.add((0, 0))
state = 'N'

#need to separate steps and rotating
lookup = {'N': {'L': -1, 'R': 1}, 'E': {'L': 1, 'R': -1}, 'S': {'L': 1, 'R': -1}, 'W': {'L': -1, 'R': 1}}

for item in instructions:
    direction = item[0]
    steps = int(item[1:])
    sign = lookup[state][direction]

    for i in range(steps):
        if (state == 'N') or (state == 'S'):
            x = x + sign
        elif (state == 'W') or (state == 'E'):
            y = y + sign
        if ((x, y) in visitedSet):
            print "Already Visited:", abs(x) + abs(y)
        visitedSet.add((x,y))

    if state == 'N' and direction == 'L':
        state = 'W'
    elif state == 'N' and direction == 'R':
        state = 'E'

    elif state == 'E' and direction == 'L':
        state = 'N'
    elif state == 'E' and direction == 'R':
        state = 'S'

    elif state == 'W' and direction == 'L':
        state = 'S'
    elif state == 'W' and direction == 'R':
        state = 'N'

    elif state == 'S' and direction == 'L':
        state = 'E'
    elif state == 'S' and direction == 'R':
        state = 'W'

print x, y
result = abs(x) + abs(y)
print result

