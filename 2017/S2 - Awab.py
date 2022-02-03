from math import ceil

def usrIn():
    N = int(input())

    table = [int(x) for x in input().split()]
        
    return (N, table)

N, table = usrIn()

table.sort()

lowTable = table[:ceil(N/2)]
lowTable.sort(reverse=True)

highTable = table[ceil(N/2):]

if N % 2 == 0:
    for i in range(N//2):
        print(f"{lowTable[i]} {highTable[i]}", end= " " )
else:
    for i in range(ceil(N/2) - 1):
        print(f"{lowTable[i]} {highTable[i]}", end=" ")
    print(f"{lowTable[N//2]}")
