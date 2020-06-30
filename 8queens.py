
def hill_climb(start, h):
    v = start
    while h(v) != 0:
        N = sorted([ (h(n), n) for n in get_neighbors(v)])
        best = N[0][0]
        Poss = choice([n[1] for n in N if n[0] == best])

def get_neighbors(t):
    N = []

    for i in range(len(t)):
        for j in range(BOARD_SIZE):
            if j != t[i]:
                N.append(t[:i] + (j,) + t[i+1:])
    return N

def num_attacking(t):

    vertical = len(t) - len(set(t)) #number of dupliactions
    #used to be set(t-1) but this cut out the last row 


    coords = list(enumerate(t))
    diagonal = 0

    for r in range(len(t)-1):
        column = t[r]
        rc = column + 1
        lc = column - 1
        
        for nr in range(r + 1, len(t)):
            if(nr, rc) in coords or (nr, lc) in coords:
                diagonal += 1

            rc += 1
            lc -= 1

    return vertical + diagonal


def display(t):
    #display tuple
    #turn it into 4x4

    coord = list(enumerate(t))

    for i in range(len(BOARD_SIZE)):
        for j in len(i):
            if BOARD_SIZE[i][j] == coord:
                print("Q")
            else:
                print("-")
            
    return coord

BOARD_SIZE = 4

t = (1, 0, 1, 3)

#print(num_attacking((1, 0, 1, 3)))
#print(num_attacking((0, 2, 0, 2)))
#print(num_attacking((0, 0, 0, 0)))


"""
BOARD_SIZE(x):
    if x = 0:
        new_x = (0, x + 1, x + 2, x + 3)
        N.append(new_x)
    if x = 1:
        new_x = (x - 1, x, x + 1, x + 2)
        N.append(new_x)
    if x = 2:
        new_x = (x - 2, x - 1, x, x + 1)
        N.append(new_x)
    if x = 3:
        new_x = (x - 3, x - 2, x - 1, x)
        N.append(new_x)
"""

print (display(t))
