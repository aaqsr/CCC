def fillLists():
    return [int(x) for x in input().split()]

def type1(Dmo, Peg, n):
    total=0
    Dmo.sort()
    Peg.sort()
    for i in range(n):
        total+=max(Dmo[i],Peg[i])
    print(total)

def type2(Dmo, Peg, n):
    All=Dmo+Peg
    All.sort()
    total=0
    for i in range(n):
        total+=All[-i-1]
    print(total)

CaseType=int(input())
n=int(input())
Dmo=fillLists()
Peg=fillLists()

if CaseType==1:
    type1(Dmo,Peg,n)
else:
    type2(Dmo,Peg,n)
