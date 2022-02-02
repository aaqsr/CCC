runningTotal=[0]*100001
pointer=0
n=int(input())
for i in range(n):
    value = int(input())
    if value == 0:
        pointer -= 1
    else:
        pointer+=1
        runningTotal[pointer] = ( value + runningTotal[pointer-1] )
        #print(runningTotal[:pointer+1])

print(runningTotal[pointer])