import heapq

class CurrentView(object):
    TARGET = None
    NUM = None

    def __init__(self, x, y, step=None):
        self.x = x
        self.y = y

        if step is None:
            self.thisstep = 0
        else:
            self.thisstep = step

        self.priority = SetPriority(x, y, self.TARGET)

    def __str__(self):
        return '%s, %s' % (self.x, self.y)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.x, self.y))




input = 1362
initialX, initialY = 1, 1

def SetPriority(x, y, p):
    return abs(p[0] - x) + abs(p[1]- y)

def isOpenSpace(x, y, favNum):
    if x < 0 or y < 0:
        return False
    gennum = x*x + 3*x + 2*x*y + y + y*y + favNum
    return bin(gennum).count('1') % 2 == 0

def findWay(favNum, destination):
    CurrentView.TARGET = destination
    CurrentView.NUM = favNum

    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    heap = []
    start = CurrentView(1, 1)
    heapq.heappush(heap, (start.priority, start))

    visited = set()
    visited.add(start)

    stepCount = 0
    while heap:
        p, state = heapq.heappop(heap)

        if (state.x, state.y) == destination:
            return state.thisstep
        visited.add(state)

        for m in moves:
            x = state.x + m[0]
            y = state.y + m[1]

            if isOpenSpace(x, y, favNum):
                genstate = CurrentView(x, y, state.thisstep + 1)
                if genstate not in visited:
                    heapq.heappush(heap, (genstate.priority, genstate))
                    print x, y

result = findWay(input, (31, 39))
#result = findWay(input, (7, 4))

print result
