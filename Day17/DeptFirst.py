import hashlib

class MazePath(object):

    def __init__(self, x, y, l, step):
        self.x = x
        self.y = y
        self.path = step
        self.num_steps = l

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.x, self.y))

def is_door_open(directions):
    #up, down, left, right
    states = []
    open_doors = ['b', 'c', 'd', 'e', 'f']

    for item in directions:
        if item in open_doors:
            states.append(True)
        else:
            states.append(False)
    return states

def FindWay(destination, hsh):
    dir_moves = ['U', 'D', 'L', 'R'] 
    queue = []
    start = MazePath(0, 0, 1, hsh)
    queue.append(start)

    moves = {
        'U': lambda x, y: (x, y - 1),
        'D': lambda x, y: (x, y + 1),
        'L': lambda x, y: (x - 1, y),
        'R': lambda x, y: (x + 1, y)
    }

    while queue:
        state = queue.pop(0)
        decode = hashlib.md5(state.path).hexdigest()
        four_chars = decode[:4]
        open_doors = is_door_open(four_chars)

        for idx, item in enumerate(open_doors):
            if item:
                i = dir_moves[idx]
                nxt = moves[i](state.x, state.y)
                nx, ny = nxt
                if not (0 <= nx < 4 and 0 <= ny < 4):
                    continue
                elif nxt == destination:
                    yield state.num_steps
                else:
                    genState = MazePath(nx, ny, state.num_steps + 1, state.path + i)
                    queue.append(genState)


input = 'ihgpwlah' #370
input = 'kglvqrro' #492
input = 'ulqzkmiv' #830
input = 'qtetzkpl' #706

des = (3,3)

#print FindWay(des, input)
data = list(FindWay(des, input))

print data[-1]