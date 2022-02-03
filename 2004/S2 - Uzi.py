# Take inputs

nums = input()

n = int(nums[0]) # Yodellers
k = int(nums[2]) # Rounds

s = [0 for N in range(n)]
ranks = []

# Take data from rounds

for K in range(k):
    m = []
    r = list(map(int,input().split()))
    for R in range(0, len(r)):
        s[R] += r[R]

    for l in s:
        m.append(l)
    ranks.append(m)

# Find Output data

count = 0
mx = 0
mxnum = 0

for S in s:
    count += 1
    if S > mx:
        mx = S
        mxnum = count

worst = 1

for a in ranks:
    score = a[mxnum-1]
    x = sorted(a, reverse=True)
    if (x.index(score)+1) > worst:
        worst = x.index(score) + 1

print("Yodeller {0} is the TopYodeller: score {1}, worst rank {2}".format(mxnum, mx, worst))
                 

    


            

    

        
     
    
