import math
n=int(input())
sortedTides=[int(x) for x in input().split()]
sortedTides.sort()
for i in range(math.ceil(n/2)):
    print(sortedTides[math.ceil(n/2)-i-1], end=" ")
    try:
        print(sortedTides[math.ceil(n/2 + i)], end=" ")
    except:
        pass