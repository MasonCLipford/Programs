
words = [line.strip() for line in open('wordlist.txt')] #download wordlist to file
words = set(w for w in words if len(w) == 4) #set vs list because of On vs O1

alpha = 'abcdefghijklmnopqrstuvwxyz'

# create graph and new verticies 


def bfs_path(start, goal):
    waiting = [start] #list
    parent = {start:None} #set - faster to check to see if items are in found
    while len(waiting) > 0: #while they're something inside waiting
        w = waiting.pop(0)

        N = [] #calculate the children of w
        for i in range(len(w)):
            for a in alpha:
                n = w[:i] + a + w[i+1:] #grabbing everthing before i and everthing after i
                if n in words and n != w:
                    N.append(n)

        
        for x in N:
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
    return

print(bfs_path('lift', 'wait'))
