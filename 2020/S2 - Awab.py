#!/usr/bin/python3

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
explored = {start: True}

def expand(coords):
    num = int((coords[0]) * (coords[1]))
    if num == goal:
        return 1
    else:
        try:
            explored[num]
        except:
            if num in numCoords:
                
                explored[num] = True

                if len(numCoords[num]) > 1:
                    for val in numCoords[num]:
                        frontier.append(val)
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
flag = False

while len(frontier) != 0:
    temp = expand(frontier[0])
    frontier.pop(0)
    if temp == 1:
        flag = True
        break

if flag:
    print("yes")
else:
    print ("no")