def UserInp():
    n=int(input())
    timeDist={}
    
    for i in range(n):
        keyV=[int(x) for x in input().split()]
        timeDist[keyV[0]]=keyV[1]
    return n,timeDist

n, timeDist=UserInp()
time=list(timeDist.keys())
time.sort()
max_speed=0

for i in range(n-1):
    CDist = abs(timeDist[time[i]] - timeDist[time[i+1]])
    CTime = abs(time[i+1] - time[i])
    speed = CDist / CTime
    if speed > max_speed:
        max_speed=speed

print(round(max_speed,1))