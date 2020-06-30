from heapq import heappush, heappop

def ucs(start, goal, get_neighbors):
    info = {start: (0, None)}
    heap = [(0, start)]
    count = 0
    while len(heap) > 0:
        pri, v = heappop(heap)
        count += 1
        if v == goal:
            L = []
            x = v
            while x != None:
                L.append(x)
                x = info[x][1]
            L.reverse()
            print(count)
            return L

        cost = info[v][0]
        for weight, u in get_neighbors(v):
            if u not in info or weight + cost < info[u][0]:
                info[u] = (weight+cost, v)
                heappush(heap, (weight+cost, u))

    return []

def astar(start, goal, get_neighbors, heuristic):
    info = {start: (0, None)}
    heap = [(0, start)]
    count = 0
    while len(heap) > 0:
        pri, v = heappop(heap)
        count += 1
        if v == goal:
            L = []
            x = v
            while x != None:
                L.append(x)
                x = info[x][1]
            L.reverse()
            print(count)
            return L

        cost = info[v][0]
        for weight, u in get_neighbors(v):
            if u not in info or weight + cost < info[u][0]:
                info[u] = (weight+cost, v)
                heappush(heap, (weight+cost+heuristic(u,goal), u))

    return []

def greedy_best(start, goal, get_neighbors, heuristic):
    info = {start: None} # just store parent info
    heap = [(0, start)]
    count = 0
    while len(heap) > 0:
        pri, v = heappop(heap)
        count += 1
        if v == goal:
            L = []
            x = v
            while x != None:
                L.append(x)
                x = info[x]
            L.reverse()
            print(count) 
            return L

        for weight, u in get_neighbors(v):
            if u not in info:
                info[u] = v
                heappush(heap, (heuristic(u, goal), u))

    return []

def get_neighbors(v):
    z = v.index(0)
    N = []
    if z >= 3:
        N.append((1, v[:z-3]+(v[z],)+v[z-2:z]+(v[z-3],)+v[z+1:]))
    if z < 6:
        N.append((1, v[:z]+(v[z+3],)+v[z+1:z+3]+(v[z],)+v[z+4:]))
    if z % 3 != 0:
        N.append((1, v[:z-1]+(v[z],v[z-1])+v[z+1:]))
    if z % 3 != 2:
        N.append((1, v[:z]+(v[z+1],v[z])+v[z+2:]))
    return N
    

def num_tiles_out_of_place(t, goal):
    return sum(1 for i in range(len(t)) if t[i] != (i+1)%9)


def manhattan(t, goal):
    #current location = i//3, i%3
    #correct location = (t[i]-1)//3, (t[i]-1)%3

    total = 0
    for i in range(9):
        x = t[i]
        if t[i] == 0:
            x = 9
        cur_row = i//3
        cur_col = i%3

        prop_row = (x-1)//3
        prop_col = (x-1)%3
        
        total += abs(prop_row - cur_row) + abs(prop_col - cur_col)

    return total

start = (5,8,2,4,0,6,3,1,7)
goal = (1,2,3,4,5,6,7,8,0)


astar(start, goal, get_neighbors, manhattan)
astar(start, goal, get_neighbors, num_tiles_out_of_place)


greedy_best(start, goal, get_neighbors, manhattan)
greedy_best(start, goal, get_neighbors, num_tiles_out_of_place)


ucs(start, goal, get_neighbors)

M = astar(start, goal, get_neighbors, manhattan)
for x in M:
    for i in range(len(x)):
        print(x[i], end = ' ')
        if i%3 ==2:
            print()
    print()

