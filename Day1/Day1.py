#Build facing Index

# North 0 L: -1, R = 1
# East 1 L: 1, R = -1
# South 2 L: 1, R = -1
# West 3 L: -1, R = 1

input = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"

ex1 = "R2, L3"
ex2 = "R2, R2, R2"
ex3 = "R5, L5, R5, R3"

instructions = input.split(', ')

visitedSet = set()
x, y = 0, 0
visitedSet.add((0, 0))
state = 'N'

for item in instructions:
    direction = item[0]
    steps = int(item[1:])

    if state == 'N':
        if direction == 'L':
            x = x - steps
            state = 'W'
        elif direction == 'R':
            x = x + steps
            state = 'E'
    elif state == 'E':
        if direction == 'L':
            y = y + steps
            state = 'N'
        elif direction == 'R':
            y = y - steps
            state = 'S'
    elif state == 'W':
        if direction == 'L':
            y = y - steps
            state = 'S'
        elif direction == 'R':
            y = y + steps
            state = 'N'
    elif state == 'S':
        if direction == 'L':
            x = x + steps
            state = 'E'
        elif direction == 'R':
            x = x - steps
            state = 'W'

print x, y
result = abs(x) + abs(y)
print result

