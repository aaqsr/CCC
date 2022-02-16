N = int(input())

F = []

for _ in range(N):
    P, W, D = map(int, input().split()) # Position, rate(1/W), Range
    F.append([P, W, D])
    

# We need to output min time that is calculated using a binary search. Basically performs SGD

def getScore(p): # Calculates time taken to walk the difference of the distances between the left and right friends
    global F
    out = 0
    for f in F:
        walk = abs(p-f[0]) -f[2] # 
        if walk > 0: # Friend does have to walk to reach speaker
            out += walk*f[1] # Time

    return out

low = 10000000000
high = 0

for f in range(len(F)):
    if F[f][0] > high:
        high = F[f][0]
    if F[f][0] < low:
        low = F[f][0]

mid = 0 # Position of speaker
s = 0

while low <= high:
    mid = (low+high)/2
    s = getScore(mid)
    sLeft = getScore(mid-1)
    sRight = getScore(mid+1)
    if s < sRight and s < sLeft:
        break
    if s == sRight or s == sLeft:
        break
    if s < sRight: # We are on the right side of the parabola
        high = mid-1
    elif s < sLeft: # We are on the left side of the parabola
        low = mid-1

print(int(s))
