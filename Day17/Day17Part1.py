import hashlib
import heapq

class MazePath(object):
    TARGET = None
    PASSCODE = None

    def __init__(self, x, y, step=None):
        self.x = x
        self.y = y
        self.path = ''

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
    #up, down, left, right
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
    start = MazePath(0, 0)
    heapq.heappush(heap, (start.priority, start))

    while heap:
        p, state = heapq.heappop(heap)

        if (state.x, state.y) == destination:
            return state.path

        decode = hashlib.md5(state.path).hexdigest()
        firstFourChars = decode[:4]
        open_doors = is_door_open(firstFourChars)
        for idx, item in enumerate(open_doors):
            if item:
                x = state.x + coMoves[idx][0]
                y = state.y + coMoves[idx][1]
                if (x > -1 and x < 4) and (y > -1 and y < 4):
                    to_append = moves[idx]
                    genState = MazePath(x, y, state.path + to_append)
                    heapq.heappush(heap, (genState.priority, genState))


input = 'ihgpwlah'
input = 'kglvqrro'
input = 'ulqzkmiv'
input = 'qtetzkpl'


des = (3,3)
result = FindWay(des)
print 'Result:', result