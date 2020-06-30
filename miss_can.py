# This is a program to solve the missionaries and cannibals problem.  The setup
# is that there are 3 missionaries and 3 cannibals who have to cross a river.
# There is a boat that holds two people at a time.  The catch is that there can
# never be more cannibals than missionaries on one side of the river or else
# bad things will happen.  This also means that if there are is a missionary and
# a cannibal on one side, and a cannibal alone in the boat on the same side,
# then that would also be bad.  It's okay if there are no missionaries on one
# side.
#
# We do this by representing the states of the puzzle as tuples of the form
# (left side, right side, boat location)
# The missionaries are denoted by numbers 1, 2, and 3, and the cannibals by the
# letters A, B, and C.  A typical state of the puzzle would be
# ('12AB', '3C', 'R')
# indicating that Missionaries 1 and 2 are on the left side of the river along
# with Cannibals A and B, Missionary 3 and Cannibal 3 are on the right, and the
# boat is also on the right.
# Note that we have to maintain the strings in a consistent order.  For
# instance, '12AB' and '1AB2' both have the same people.  So in the code below,
# will sort the strings to account for this.

from itertools import combinations

def bfs_path_no_graph(start, goal):
    waiting = [start]
    parent = {start:None} 
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

# helper functions to count how many letters and digits are in a string.
def count_letters(s):
    return sum(1 for x in s if x.isalpha())

def count_digits(s):
    return sum(1 for x in s if x.isdigit())

def get_children(w):
    children = []
    left, right, boat = w
    if boat == 'L':
        for x in left: # move one person from left to right
            new_left = left.replace(x, '')
            new_right = ''.join(sorted(right + x))
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and
            (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0):
                children.append((new_left, new_right, 'R'))
        for x, y in combinations(left, 2): # move two people from left to right
            new_left = left.replace(x, '').replace(y, '')
            new_right = ''.join(sorted(right+x+y))
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and
            (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0):
                children.append((new_left, new_right, 'R'))

    # This code is nearly a mirror image of the above                                 
    if boat == 'R':
        for x in right:
            new_right = right.replace(x, '')
            new_left = ''.join(sorted(left + x))
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and
            (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0):
                children.append((new_left, new_right, 'L'))
        for x, y in combinations(right, 2):
            new_right = right.replace(x, '').replace(y, '')
            new_left = ''.join(sorted(left+x+y))
            if (count_digits(new_left) >= count_letters(new_left) or count_digits(new_left) == 0) and
            (count_digits(new_right) >= count_letters(new_right) or count_digits(new_right) == 0):
                children.append((new_left, new_right, 'L'))
                                 
    return children

# Display the answer, replacing the individual missionary and cannibal names with M and C
for x in bfs_path_no_graph(('123ABC', '', 'L'), ('', '123ABC', 'R')):
    l,r,b = x
    l = l.replace('A', 'C').replace('B', 'C')
    r = r.replace('A', 'C').replace('B', 'C')
    l = l.replace('1', 'M').replace('2', 'M').replace('3', 'M')
    r = r.replace('1', 'M').replace('2', 'M').replace('3', 'M')
    print(l, r, b)
        

