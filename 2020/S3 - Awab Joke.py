# joke solution

import itertools

N = input()
H = input()
    

permN = itertools.permutations(N, len(N))
uniquePerm = {}

count = 0
for val in permN:
    # H.find(val)
    temp = ""

    for i in val:
        temp += i

    try:
        uniquePerm[temp]
    except:
        uniquePerm[temp] = 1
        if temp in H:
            count += 1

print(count)