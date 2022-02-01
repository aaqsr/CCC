def inputVal():
    n = input()
    swi = input().split()
    sem = input().split()
    return n, swi, sem


n, swi, sem = inputVal()
TSwi = [0]
TSem = [0]
lastDay = 0
for i in range(1, int(n)+1):
    TSwi.append(TSwi[i-1] + int(swi[i-1]))
    TSem.append(TSem[i-1]+int(sem[i-1]))
    if TSwi[i] == TSem[i]:
        lastDay = i

print(lastDay)
