import math;

N = int(input())
ans = 0

# if (N % 4 == 0):
#     ans += 1
    
# if (N % 5 == 0):
#     ans += 1
    
# if ((N % 4) % 5 == 0) or ((N % 5) % 4 == 0):
#     ans += 1
    
for i in range(math.floor(N / 4)):
    if ( (N - 4*i) % 5 == 0):     # if (N - multiples of 4) is divisible by 5
        ans += 1

if (N % 4 == 0) :     # the case that there are only 4s and no 5s
    ans += 1



print(ans)