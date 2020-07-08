aps = [
    ['LAX','NYC'],
    ['LAX','TOR'], 
    ['LAX','PAR'],
    ['LAX','LON'],
    ['SFO','TOR'],
    ['TOR','NYC'],
    ['NYC','LON'],
    ['LON','FRA'],
    ['FRA','MPX'],
    ['FRA','LAX'],
    ['FRA','SFO'],
    ['FRA','MOS'],
    ['FRA','AMS'],
    ['MPX','BCN'],
    ['MPX','FRA'],
    ['MPX','MAD'],
    ['AMS','BCN'],
    ['AMS','MPX'],
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
        while True:
            if len(self.FRONTIER) == 0:
                return []
            n = self.FRONTIER.pop()
            if n.source not in self.EXPLORED:
                self.EXPLORED.add(n.source)
                if n.source == self.tg:
                    path = []
                    while not (n.parent == None):
                        path +=[n.source]
                        n = n.parent
                    path +=[n.source]
                    return path
                self.explore(n)
        
        return ['LAX','SFO','NYC']


bfs = bfs(aps,'SFO','AMS')
best_path = bfs.best_path()

if not best_path == None: 
    print('found a path')
    print(best_path[::-1])
    
