import math

def checkPrime(p):
    rflag=True
    for i in range(2, math.floor(p**0.5)+1):
        if p % i == 0:
            rflag=False
            break
    #print(p, rflag)
    return rflag

def FindAB(testCase):
    for i in range(testCase, 2*testCase+1):
        if checkPrime(i):
            if checkPrime(2*testCase-i):
                outList.append([2*testCase-i, i])
                break

n=int(input())
outList=[]
for i in range(n):
    testCase=int(input())
    FindAB(testCase)

for i in range(n):
    print(outList[i][0] , outList[i][1])