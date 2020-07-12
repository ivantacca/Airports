import sys

aps = [
    ['LAX','NYC'],
    ['LAX','TOR'], 
    ['LAX','PAR'],
    ['LAX','LON'],
    ['LAX','SFO'],
    ['SFO','TOR'],
    ['TOR','NYC'],
    ['NYC','LON'],
    ['LON','FRA'],
    ['FRA','MPX'],
    ['FRA','LAX'],
    ['FRA','MOS'],
    ['FRA','AMS'],
    ['MPX','BCN'],
    ['MPX','FRA'],
    ['MPX','MAD'],
    ['AMS','BCN'],
    ['AMS','MPX'],
    ['PAR','FRA']
]

class Node:
    def __init__(self,source,parent):
        self.source = source
        self.parent = parent

class bfs:
    FRONTIER = set()
    EXPLORED = set()
    def __init__(self,data,source,target):
        self.data = data
        self.tg = target
        self.src = source
    def explore(self,node):
        for i in self.data:
            if i[0] == node.source:
                self.FRONTIER.add(Node(i[1],node))
    def best_path(self):
        self.explore(Node(self.src,None))
        self.EXPLORED.add(self.src)
        while True:
            if len(self.FRONTIER) == 0:
                return None
            n = self.FRONTIER.pop()
            if n.source not in self.EXPLORED:
                self.EXPLORED.add(n.source)
                # if the current node is the target
                if n.source == self.tg:
                    p = []
                    while not (n.parent == None):
                        p +=[n.source]
                        n = n.parent
                    p +=[n.source]
                    return p
                else:
                    self.explore(n)


bfs = bfs(aps,sys.argv[1],sys.argv[2])
print(f"Flights from {sys.argv[1]} to {sys.argv[2]}")

best_path = bfs.best_path()
for i,a in enumerate(best_path[::-1]):
    print (a, end='')
    try:
        if(best_path[i+1]):
            print(" -> ", end='')
    except:
        print("")
