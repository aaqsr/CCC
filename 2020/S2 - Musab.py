from logging.config import valid_ident


def takeInp(grid,m,n):
    for r in range(m):
        temp=[int(x) for x in input().split()]
        for c in range(n):
            grid[temp[c]]=grid.get(temp[c],[])+[[r,c]]
    
def recPath(r,c):
    global frontier
    val=(r+1)*(c+1)
    global grid
    global Validity
    if val==1:
        Validity=True
    elif val in grid:
        for cord in grid[val]:
            if not(cord in frontier):
                frontier.append(cord)

m=int(input())
n=int(input())
frontier=[[m-1,n-1]]
fpointer=0
grid={}
takeInp(grid,m,n)
# if recPath(m-1,n-1,[]):
#     print("yes")
# else:
#     print("no")

Validity=False
while fpointer<len(frontier) and Validity == False:
    recPath(frontier[fpointer][0],frontier[fpointer][1])
    fpointer+=1

if Validity:
    print("yes")
else:
    print("no")