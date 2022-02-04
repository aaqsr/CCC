#!/usr/bin/python3

def takeInput(n):
    grid = []
    for i in range(n):
        temp = input()
        grid.append(temp)
        if temp.find("S") != -1:
            startY = i
            startX = temp.find("S")
    return grid, [startY, startX]


def breadSearch(frontier, fpointer):
    global NodeVals
    a=ValidNode(frontier[fpointer])
    if a[0]:
        NodeVals[tuple(frontier[fpointer])]=0
        while fpointer < len(frontier):
            checkAdj(frontier[fpointer],NodeVals[tuple(frontier[fpointer])])
            #temp1, temp2 = checkAdj(frontier[fpointer], cost[fpointer])
            # if len(temp1) != 0:
            #     frontier.extend(temp1)
            #     cost.extend(temp2)
            fpointer += 1


def checkAdj(coords, currCost):
    global NodeVals
    global frontier
    #Clist = []
    temp= [coords[0]-1, coords[1]]
    temp = ValidNode([coords[0]-1, coords[1]])
    if temp[0]:
        frontier.append(temp[1])
        NodeVals[tuple(temp[1])]=currCost+1
        #Clist.append(currCost+1)

    temp = ValidNode([coords[0]+1, coords[1]])
    if temp[0]:
        frontier.append(temp[1])
        NodeVals[tuple(temp[1])]=currCost+1
        #Clist.append(currCost+1)

    temp = ValidNode([coords[0], coords[1]-1])
    if temp[0]:
        frontier.append(temp[1])
        NodeVals[tuple(temp[1])]=currCost+1
        # Clist.append(currCost+1)

    temp = ValidNode([coords[0], coords[1]+1])
    if temp[0]:
        frontier.append(temp[1])
        NodeVals[tuple(temp[1])]=currCost+1
        # Clist.append(currCost+1)
            
    #return frontier, Clist


def ValidNode(coords):
    validity = True
    #global allNodes
    global NodeVals
    global grid
    if tuple(coords) in NodeVals:
        validity = False
    else:
        NodeVals[tuple(coords)]=-1
        # allNodes.append(coords.copy())
        temp = grid[coords[0]][coords[1]]
        if temp == "W":
            validity = False
        else:
            if temp in ["U", "D", "L", "R"]:
                testCoords = coords
                if temp == "U":
                    testCoords[0] -= 1
                elif temp == "D":
                    testCoords[0] += 1
                elif temp == "L":
                    testCoords[1] -= 1
                elif temp == "R":
                    testCoords[1] += 1
                validity, coords = ValidNode(testCoords)

            else:
                row = grid[coords[0]]
                col = getCol(coords[1])
                if "C" in row or "C" in col:
                    validity = checkCam(coords, col, row)
    return [validity, coords]


def checkCam(coords, col, row):
    left = row[:coords[1]][::-1]
    right = row[coords[1]+1:]
    up = col[:coords[0]][::-1]
    down = col[coords[0]+1:]
    rflag=True
    if not(checkDir(right)):
        rflag=False
    elif not(checkDir(left)):
        rflag=False
    elif not(checkDir(up)):
        rflag=False
    elif not(checkDir(down)):
        rflag=False
    return rflag


def checkDir(dir):
    for i in dir:
        if i == "C":
            rflag = False
            break
        if i == "W":
            rflag = True
            break
    return rflag


def getCol(colNum):
    col = []
    global n
    global grid
    for i in range(n):
        col.append(grid[i][colNum])
    return col


def Display(n, m):
    global frontier
    global cost
    global NodeVals
    for r in range(n):
        for c in range(m):
            coords = [r, c]
            if grid[r][c] == ".":
                print(NodeVals.get(tuple(coords), -1))
                # if coords in frontier:
                #     print(cost[frontier.index(coords)])
                # else:
                #     print(-1)


temp = input().split()
n = int(temp[0])
m = int(temp[1])
grid, startCoords = takeInput(n)
frontier = [startCoords]
fpointer = 0
#cost = [0]
NodeVals = {}
breadSearch(frontier, fpointer)
Display(n, m)
