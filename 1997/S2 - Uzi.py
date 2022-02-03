# Take inputs

A = []

N = int(input())

for i in range(N):
    A.append(int(input()))

# Algo

def rec(arr, start):
    t = False
    # Traverse through factors for equals
    for m in range(start, len(arr)-2):
        count = 0
        for jump in range(1, len(arr)-(m+1)):
            count += 1
            if arr[m][0] == arr[m+jump][1] or arr[m][1] == arr[m+jump][0]:
               t = True
               return t

for num in A:
    n = False
    ans = "is not"
    factors = []
    k = []
        
    # Find factor pairs + sums and diffs
    for g in range(1, num):
        pair = [] # sum, diff
        if num % g == 0:
            z = num/g
            factors.append([z, g])
            pair.append(z+g)
            if z > g:
                pair.append(z-g)
            else:
                pair.append(g-z)
            k.append(pair)

    n = rec(k, 0)

    if n == True:
        ans = "is"

    print("{0} {1} nasty".format(num, ans))
