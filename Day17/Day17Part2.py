import hashlib
import heapq

class MazePath(object):
    TARGET = None
    PASSCODE = None

    def __init__(self, x, y, l, step=None):
        self.x = x
        self.y = y
        self.path = ''
        self.num_steps = l

        if step is None:
            self.path = self.PASSCODE
        else:
            self.path = self.path + step

        self.priority = SetPriority(x, y, self.TARGET)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.x, self.y))

def SetPriority(x, y, p):
    return abs(p[0] - x) + abs(p[1] - y)

def is_door_open(directions):

    states = []
    open_doors = ['b', 'c', 'd', 'e', 'f']

    for item in directions:
        if item in open_doors:
            states.append(True)
        else:
            states.append(False)
    return states


def FindWay(destination):
    MazePath.TARGET = (3, 3)
    MazePath.PASSCODE = input

    coMoves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    moves = ['U', 'D', 'L', 'R']
    heap = []
    start = MazePath(0, 0, 1)
    heapq.heappush(heap, (start.priority, start))

    curr_max = 0
    while heap:
        p, state = heapq.heappop(heap)

        if (state.x, state.y) == destination:
            curr = state.num_steps
            if curr > curr_max:
                curr_max = curr
                print curr_max
                #yield curr_max

        decode = hashlib.md5(state.path).hexdigest()
        firstFourChars = decode[:4]
        open_doors = is_door_open(firstFourChars)
        for idx, item in enumerate(open_doors):
            if item:
                x = state.x + coMoves[idx][0]
                y = state.y + coMoves[idx][1]
                if (x >= 0 and x <= 3) and (y >= 0 and y <= 3):
                    to_append = moves[idx]
                    genState = MazePath(x, y, state.num_steps + 1, state.path + to_append)
                    heapq.heappush(heap, (genState.priority, genState))

input = 'ihgpwlah'
#input = 'kglvqrro'
#input = 'ulqzkmiv'
#input = 'qtetzkpl'
print 'running'
des = (3,3)
FindWay(des)