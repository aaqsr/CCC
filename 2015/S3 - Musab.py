def check(i):
    global occ
    flag=False
    for k in range(i,0,-1):
        if not(k in occ):
            flag=True
            occ[k]=1
            break
    return flag
            


g=int(input())
p=int(input())
occ={}
parked=True
park=0

for i in range(p):
    i = int(input())
    if not(check(i)):
        parked= False
    elif(parked==True):
        park+=1


print(park)

    
