M = int(input())
N = int(input())
K = int(input())

# Initialize array
canvas = []
for _ in range(M):
    canvas.append([0 for _ in range(N)])

# Keep amount of gold updated
gold = 0

def fillRow(i, arr):
    global gold, N
    g = gold
    
    for x in range(N):
        if arr[x] == 0:
            arr[x] = 1
            g += 1
        else:
            arr[x] = 0
            g -= 1

    return arr, g

def fillCol(i, arr):
    global gold, M

    for x in range(M):
        if arr[x][i] == 0:
            arr[x][i] = 1
            gold += 1
        else:
            arr[x][i] = 0
            gold -= 1

for _ in range(K):
    choice, strnum = map(str, input().split())
    num = int(strnum)
    if choice == "R":
        canvas[num-1], gold = fillRow(num, canvas[num-1])
    else:
        fillCol(num, canvas)


print(gold)


