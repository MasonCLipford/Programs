class Graph(dict):
    def add(self, v):
        self[v] = set()

    def add_edge(self, u, v):
        self[u].add(v) #add each thing both way
        self[v].add(u)


def bfs(G, start, goal):
    waiting = [start] #list
    found = {start} #set - faster to check to see if items are in found
    while len(waiting) > 0: #while they're something inside waiting
        w = waiting.pop(0)
        for x in G[w]:
            if x == goal:
                return True
            if x not in found:
                found.add(x)
                waiting.append(x)
    return False


def dfs(G, start, goal):
    waiting = [start] #list
    found = {start} #set - faster to check to see if items are in found
    while len(waiting) > 0: #while they're something inside waiting
        w = waiting.pop() #take out the 0
        for x in G[w]:
            if x == goal:
                return True
            if x not in found:
                found.add(x)
                waiting.append(x)
    return False


def bfs_path(G, start, goal):
    waiting = [start] #list
    parent = {start:None} #set - faster to check to see if items are in found
    while len(waiting) > 0: #while they're something inside waiting
        w = waiting.pop(0)
        for x in G[w]:
            if x == goal: #follows the dictionary backwards 
                path = [x]
                x = w
                while parent[x] != None: #getting the order right
                    path.append(x)
                    x = parent[x]
                path.append(x)
                path.reverse()
                return path
            
            if x not in parent:
                parent[x] = w
                waiting.append(x)
    return[]

def dfs_path(G, start, goal):
    waiting = [start] #list
    parent = {start:None} #set - faster to check to see if items are in found
    while len(waiting) > 0: #while they're something inside waiting
        w = waiting.pop()
        for x in G[w]:
            if x == goal: #follows the dictionary backwards 
                path = [x]
                x = w
                while parent[x] != None: #getting the order right
                    path.append(x)
                    x = parent[x]
                path.append(x)
                path.reverse()
                return path
            
            if x not in parent:
                parent[x] = w
                waiting.append(x)
    return[]

words = [line.strip() for line in open('wordlist.txt')] #download wordlist to file
words = set(w for w in words if len(w) == 4) #set vs list because of On vs O1

alpha = 'abcdefghijklmnopqrstuvwxyz'

# create graph and new verticies 
G = Graph()
for w in words:
    G.add(w)

for w in words:
    for i in range(len(w)):
        for a in alpha:
            n = w[:i] + a + w[i+1:] #grabbing everthing before i and everthing after i
            if n in words and n != w:
                G.add_edge(w, n)

"""
print(G["wait"])
print(dfs(G, 'wait', 'lift'))
print(bfs_path(G, 'fear', 'rain'))
print(dfs_path(G, 'fear', 'rain'))
"""

print(bfs_path(G, 'fear', 'jump'))


