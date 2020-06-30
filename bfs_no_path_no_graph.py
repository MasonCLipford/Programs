# This is an alternate approach to the word ladders problem that does not
# explicitly create a graph.  Instead, when we need the children of a node,
# we generate them right then.  This is a little faster than the other way that
# creates a graph because it avoids setting up the entire graph at the start
# (including all the edges and vertices that are irrelevant to the search we
# are interested in.)

from itertools import combinations

words = [line.strip() for line in open('wordlist.txt')]
words = set(words)
alpha = 'abcdefghijklmnopqrstuvwxyz'

def bfs_path_no_graph(start, goal):
    waiting = [start]
    parent = {start:None} # for each found vertex, keep track of its parent
    while len(waiting) > 0:
        w = waiting.pop(0)
        
        for x in get_children(w):
            if x == goal:
                path = [x]
                x = w
                while parent[x] != None:
                    path.append(x)
                    x = parent[x]
                path.append(x)
                path.reverse()
                return path
                
            if x not in parent:
                parent[x] = w 
                waiting.append(x)
    return []

def count_letters(s):
    return sum(1 for x in s if x.isalpha())

def count_digits(s):
    return sum(1 for x in s if x.isdigit())

def get_children(w):
    children = []
    left, right, boat = w #creates the setup
    if boat == 'L': #sending 1 person to the right
        for x in left:
            
            new_left = left.replace(x, '')
            new_right = ''.join(sorted(right + x)) #keeps the people sorted so that they dont get mixed up
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0):
                children.append((new_left, new_right,'R')) #as long as their are more cannibals than missionaries


        for x, y in combinations(left, 2): #sending 2 people to the right
            new_left = left.replace(x, '').replace(y, '') #chain replace calls
            new_right = ''.join(sorted(right+x+y))
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right == 0)):
                children.append((new_left, new_right,'R'))

    if boat == 'R': 
        for x in right: #sending one person to the left
            
            new_right = left.replace(x, '')
            new_left = ''.join(sorted(right + x)) #keeps the people sorted so that they dont get mixed up

            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0):
                children.append((new_left, new_right,'L')) #as long as their are more cannibals than missionaries

        for x, y in combinations(left, 2): #sending 2 people to the left
            new_right = left.replace(x, '').replace(y, '') #chain replace calls
            new_left = ''.join(sorted(right+x+y))
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left == 0) and (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0)):
                children.append((new_left, new_right,'L'))

    return children
                
for x in bfs_path_no_graph(('123ABC', '', 'L'), (('', '123ABC', 'R'))):
    print(x)
    l.replace
            


