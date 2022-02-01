def userIn():
    N = int(input())
    Sw = input().split(" ")
    Se = input().split(" ")
    return N, Sw, Se

def checkDay(N, Sw, Se):
    SwSum = 0
    SeSum = 0
    
    
    ans = 0
    
    for i in range(0, N):
        SwSum += int(Sw[i])
        SeSum += int(Se[i])
        
        if SwSum == SeSum:
            ans = i + 1
        
    return int(ans)


N, Sw, Se = userIn()

print(checkDay(N, Sw, Se))

