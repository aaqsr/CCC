#!/usr/bin/python3

def takeinput():
    n = int(input())
    
    villages = []
    
    for i in range(n):
        villages.append(int(input()))
    
    return n, villages

n, vill = takeinput()   

sortedVill = sorted(vill)

neighbourhood = []

for i in range(1, len(sortedVill) - 1):
    diff = sortedVill[i + 1] - sortedVill[i - 1]
    neighbourhood.append(diff / 2)

ans = min(neighbourhood)

print(round(ans, 1))