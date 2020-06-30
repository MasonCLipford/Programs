from heapq import heappush, heappop

def ucs(start, goal):
    info = {start:(0, None)} #none = null

    heap = [(0, start)] #orders by the cost/ first thing

    while len(heap) > 0:
        cost, v = heappop(heap) #current cost, actual vertex

        if v == goal:
            L.appex(x)
            x = info[x][1] #vertices info
        L.reverse() #ends up in backwards order so flip it
        #print(info[goal])
        return L

        for weight, u in get_neighbors(v): #returns the weight and vertex neighbor
            
            if u not in info or cost + weight < info[u][0]: #check picture of weight in graph 
                info[u] = (cost+weight, v) #update info, new cost and parent of that node
                hpeappush(heap, (cost+weight, u)) #push onto heap

    return []

def get_neighbors(v):
    N = []
    left, right, flashliht = v

    for x in left:
        new_left = left.replace(x, '')
        new_right = ''.join(sorted(right + x)) #creates a sorted list
        N.append((int(x, 16),(new_left, new_right, 'R'))
    if x, y in combinations(left, 2):

    return N

print(ucs(('125a', '', 'L'), ('', '125a', 'R')) 

"""Testing code
def get_neighbors():
    if v =='A':
        return[(2, 'B'), (7, 'C')]
    elif v == 'B':
        return [(1,'D'), (4, 'C'), (2, 'A')]
    elif v == 'C':
        return [(4,'B'), (7, 'A'), (6, 'E')]
    elif v == 'D':
        return [(1,'B'), (10, 'E'), (8, 'F')]
    elif v == 'E':
        return [(4,'F'), (10, 'D'), (5, 'C')]
    elif v == 'F':
        return [(4,'E'), (8, 'D')]

print(ucs('A', 'F'))
"""
