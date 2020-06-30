def bfs_path(start, goal):
    waiting = [start] #list
    parent = {start:None} #set - faster to check to see if items are in found
    while len(waiting) > 0: #while they're something inside waiting
        w = waiting.pop()
        for x in get_children(w):
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


def get_children(w):
    children = []
    #one, two, three, four = hanoi
        
    left, middle, right = w

    #create a tuple and check if the top peg can be moved
    #has to check if left, middle, right is empty or has higher/lower number

    """ Left """
    for x in left:
        new_left = left.replace(x, '')
        new_middle = 0
        new_right = 0
        #print(new_left)
        #print(new_middle)
        
        if(int(new_left) > int(new_middle)):
            children.append((new_left, new_middle, new_right))

        if(int(new_left) == 0) or (int(new_left) < int(new_right)):
            children.append((new_left, new_middle, new_right))
            
    print(left)
    print(new_middle)
    print(new_right)

    """ Middle """
    for x in middle:
        new_middle = middle.replace(x, '')
                             
        if(int(new_middle) == 0) or (int(new_middle) < int(new_right)):
            children.append((new_left, new_middle, new_right))

        if(int(new_middle) == 0) or (int(new_middle) < int(new_left)):
            children.append((new_left, new_middle, new_right))

    """ Right """
    for x in right:
        new_right = right.replace(x, '')
        if(int(new_right) == 0) or (int(new_right) < int(new_left)):
            children.append((new_left, new_middle, new_right))

        if(int(new_right) == 0) or (int(new_right) < int(new_middle)):
            children.append((new_left, new_middle, new_right))

    #print("hello")
    return children
    
    

for x in bfs_path(('1234', '', ''), ('', '', '1234')):
    print(left, middle, right)
    print(children)

print(bfs_path(('1234','',''), ('','','1234')))

