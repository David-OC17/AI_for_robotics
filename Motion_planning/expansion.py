def expansion(init, cost, goal, grid, delta):
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1 #initial position is closed
    
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))] 
    #expand is a 2D array that shows the order in which the elements were expanded
    
    x = init[0]
    y = init[1]
    g = 0
    
    open = [[g, x, y]]
    
    found = False #flag that is set when search complete
    resign = False #flag set if we can't find expand
    count = 0 
    
    while found is False and resign is False:
        if len(open) == 0:
            resign = True
            print('fail')
        else:
            open.sort()
            open.reverse()
            next = open.pop() #pop the element with the lowest cost (g-value)
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] = count #count is the order in which the elements were expanded
            count += 1
            
            if x == goal[0] and y == goal[1]:
                found = True
                print(next)
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
    return expand #returns the expansion of the search