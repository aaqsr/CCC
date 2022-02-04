M = int(input())
N = int(input())
grid = []
numCoords = {}

for r in range(M):
    
    row = input().split()
    
    # opt
    gridRow = []
    
    for c in range(len(row)):
        num = int(row[c])

        # opt
        gridRow.append(int(num))
        
        if num in numCoords:
            numCoords[num].append([r+1, c+1])
        else: 
            numCoords[num] = [[r+1, c+1]]
    
    # opt
    grid.append(gridRow)

goal = grid[0][0]
start = grid[M-1][N-1]

frontier = [[M, N]]
explored = [start]

def expand(coords):
    num = int((coords[0]) * (coords[1]))
    if num == goal:
        return 1
    else:
        if not (num in explored): 
            if num in numCoords:
                
                explored.append(num)

                if len(numCoords[num]) > 1:
                    for val in numCoords[num]:
                        expand(val)
                else:
                    frontier.append([numCoords[num][0][0], numCoords[num][0][1]])
        return 0
        

# for val in frontier:
#     if len(frontier) != 0:
#         temp = expand(val)
#         frontier.pop(0)
#         if temp == 1:
#             print("yes")
#             break

# if len(frontier) == 0:
#     print("no")

def explore():
    if len(frontier) != 0:
        for val in frontier:
            temp = expand(val)
            frontier.pop(0)
            if temp == 1:
                print("yes")
                return
        explore()
    else:
        print("no")
        return

explore()