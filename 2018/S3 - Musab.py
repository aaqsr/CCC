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


def breadSearch(frontier, fpointer, cost):
    a=ValidNode(frontier[fpointer])
    if a[0]:
        while fpointer < len(frontier):
            temp1, temp2 = checkAdj(frontier[fpointer], cost[fpointer])
            if len(temp1) != 0:
                frontier.extend(temp1)
                cost.extend(temp2)
            fpointer += 1


def checkAdj(coords, currCost):
    Rlist = []
    Clist = []
    temp = ValidNode([coords[0]-1, coords[1]])
    if temp[0]:
        Rlist.append(temp[1])
        Clist.append(currCost+1)

    temp = ValidNode([coords[0]+1, coords[1]])
    if temp[0]:
        Rlist.append(temp[1])
        Clist.append(currCost+1)

    temp = ValidNode([coords[0], coords[1]-1])
    if temp[0]:
        Rlist.append(temp[1])
        Clist.append(currCost+1)

    temp = ValidNode([coords[0], coords[1]+1])
    if temp[0]:
        Rlist.append(temp[1])
        Clist.append(currCost+1)
    return Rlist, Clist


def ValidNode(coords):
    validity = True
    global allNodes
    global grid
    if coords in allNodes:
        validity = False
    else:
        allNodes.append(coords.copy())
        row = grid[coords[0]]
        col = getCol(coords[1])
        temp = grid[coords[0]][coords[1]]
        if temp == "W":
            validity = False

        elif temp in ["U", "D", "L", "R"]:
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

        elif "C" in row or "C" in col:
            validity = checkCam(coords, col, row)
    return [validity, coords]


def checkCam(coords, col, row):
    left = row[:coords[1]][::-1]
    right = row[coords[1]+1:]
    up = col[:coords[0]][::-1]
    down = col[coords[0]+1:]
    rflag = checkDir(right) and checkDir(
        left) and checkDir(up) and checkDir(down)
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
    for r in range(n):
        for c in range(m):
            coords = [r, c]
            if grid[r][c] == ".":
                if coords in frontier:
                    print(cost[frontier.index(coords)])
                else:
                    print(-1)


temp = input().split()
n = int(temp[0])
m = int(temp[1])
grid, startCoords = takeInput(n)
frontier = [startCoords]
fpointer = 0
cost = [0]
allNodes = []
breadSearch(frontier, fpointer, cost)
Display(n, m)
