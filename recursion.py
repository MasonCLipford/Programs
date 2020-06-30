class Digraph(dict):
    def add(self, v):
        self[v] = set()

    def add_edge(self, u, v):
        self[u].add(v)

MAX = 1
MIN = 2

def minimax(v, player):
    #basecase for recursion
    c = utility(v)
    if c != -1:
        return c
    results = [minimax(w, MAX if player == MIN else MIN) for w in G[v]] #loop and append
    return max(results) if player ==MAX else min(results) 


    #call itself

def utility(v):
    util = {'e':6, 'f':3, 'g':2, 'h':4, 'l':3, 'm':7, 'j':1, 'k':5}
    return util[v] if v in util else -1 #returns -1 if not an end state


def choose_move(v, player):
    results = [(minimax(w, MAX if player == MIN else MIN), w) for w in G[v]] #loop and append
    #stores a tuple so that we can have a letter and value
    print(sorted(results, key =lambda x:x[1])) #x:x[1] makes it sort by second thing in tuple
    return max(results)[1] if player == MAX else min(results)[1]


V = 'abcdefghijklm' # list of verices
E = 'ab ac ad be bf bg ch ci dj dk il im' # list of edges

G = Digraph() 
for v in V:
    G.add(v)

for x, y in E.split():
    G.add_edge(x, y)
    
    
