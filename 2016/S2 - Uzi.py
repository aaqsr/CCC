# Take inputs

qs = int(input())
N = int(input())

dm = []
pg = []

dm = list(map(int,input().split())) 

pg = list(map(int,input().split())) 

# Algo

s = 0

if qs == 2:
    dm.sort()
    pg.sort(reverse=True)

    for p in range(0, N):
        if dm[p] >= pg[p]:
            put = dm[p]
        else:
            put = pg[p]
        s += put

else:
    dm.sort(reverse=True)
    pg.sort(reverse=True)

    for p in range(0, N):
        if dm[p] >= pg[p]:
            put = dm[p]
        else:
            put = pg[p]
        s += put

print(s)
