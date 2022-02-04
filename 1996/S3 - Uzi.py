# Take inputs
N = int(input())
a = []

for _ in range(N):
    a.append(list(map(int, input().split())))

import itertools

for A in a:
    # Replace numbers with bit patterns
    n = A[0]
    k = A[1]
    temp = []

    for _ in range(k):
        temp.append('1')

    for _ in range(n-k):
        temp.append('0')

    b = "".join(temp)
    nums = list(b)
    perms = list(itertools.permutations(nums))
    final = []
    perms = list(dict.fromkeys(perms))
    
    for p in perms:
        z = "".join(p)
        final.append(z)
        
    final.sort(key=lambda x: int(x, 2), reverse=True)

    print("The bit patterns are:")
    
    for f in final:
        print(f)
        
        
    
    
