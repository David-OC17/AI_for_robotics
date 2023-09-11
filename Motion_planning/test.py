import search
import expansion

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1
delta = [[-1, 0], #go up
         [0, -1], #go left
         [1, 0], #go down
         [0, 1]] #go right
delta_name = ['^', '<', 'v', '>'] #Used to show the best path

for i in range(len(grid)):
    print(grid[i])

print('------------------')
print('Expansion of the search:')

#Shows the order in which the cells where expanded to
expansion = expansion.expansion(init, cost, goal, grid, delta)
for i in range(len(expansion)):
    print(expansion[i])
   
print('------------------')
print('Best route found:')