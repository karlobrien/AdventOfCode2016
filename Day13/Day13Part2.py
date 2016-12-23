import heapq

class CurrentView(object):
    TARGET = None
    NUM = None
    MAX = None

    def __init__(self, x, y, step=None):
        self.x = x
        self.y = y

        if step is None:
            self.thisstep = []
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

def SetPriority(x, y, p):
    return abs(p[0] - x) + abs(p[1]- y)

def isOpenSpace(x, y, favNum):
    if x < 0 or y < 0:
        return False
    gennum = x*x + 3*x + 2*x*y + y + y*y + favNum
    return bin(gennum).count('1') % 2 == 0

def findWay(favNum, destination, maxNum):
    CurrentView.TARGET = destination
    CurrentView.NUM = favNum
    CurrentView.MAX = maxNum

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = []
    start = CurrentView(1, 1)
    heapq.heappush(heap, (start.priority, start))

    visited = set()
    visited.add(start)

    count = 0
    while heap:
        state = heapq.heappop(heap)

        visited.add(state[1])

        for m in moves:
            x = state[1].x + m[0]
            y = state[1].y + m[1]

            if isOpenSpace(x, y, favNum):
                combinedStep = state[1].thisstep + [state[1]]
                genstate = CurrentView(x, y, step=combinedStep)

                if len(genstate.thisstep) < state[1].MAX:
                    if genstate not in visited:
                        heapq.heappush(heap, (genstate.priority, genstate))
                        count+=1

    print len(visited)
    print count

findWay(input, (-1, -1), 50)
