from heapq import heappush, heappop


def astar(start, goal, get_neighbors, heuristic):
    info = {start: (0, None)}
    heap = [(0, start)]
    while len(heap) > 0:
        pri, v = heappop(heap)
        if v == goal:
            L = []
            x = v
            while x != None:
                L.append(x)
                x = info[x][1]
            L.reverse()
            return L

        cost = info[v][0]
        for weight, u in get_neighbors(v):
            if u not in info or weight + cost < info[u][0]:
                info[u] = (weight+cost, v)
                heappush(heap, (weight+cost+heuristic(u,goal), u))

    return []

board = """
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000"""        

        
from tkinter import *
root = Tk() # creates window
canvas = Canvas(width=600, height=600, bg='white')
canvas.grid() # displays canvas on screen
#canvas.create_rectangle(x1, y1, x2, y2, fill='yellow')
#canvas.create_text(x, y, text='hello', anchor=CENTER, font=('Verdana', 16))


def get_neighbors2(v):
    r,c = v
    N = [(r+1,c), (r-1,c), (r,c+1), (r,c-1), (r+1,c-1), (r+1,c+1), (r-1,c-1), (r-1,c+1)]
    return [(1,(a,b)) for a,b in N if 0<=a<20 and 0<=b<20 and board[a][b]=='0']

def euclidean(v, goal):
    r, c = v
    rg, cg = goal
    return ((rg-r)**2 + (cg-c)**2)**.5


L = astar((0,0), (21, 21), get_neighbors2, euclidean)


for i in range(len(L)):
    r, c = L[i]
    board[r][c] = str(i)

for i in range(len(board)):
    for j in range(len(board[i])):
        print('{:>3s} '.format(board[i][j]), end='')
    print()

