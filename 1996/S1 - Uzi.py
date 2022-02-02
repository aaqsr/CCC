# Function to compute sum of divisors

def classify(num):
    factors = []
    answer = ""
    s = 0
        
    for g in range(1, num-1):
        if num % g == 0:
            factors.append(g)

    for n in factors:
        s += n

    if s == num:
        ans = "perfect"
    elif s > num:
        ans = "abundant"
    else:
        ans = "deficient"

    print("{0} is a {1} number".format(num, ans))

# Take inputs

a = []

x = True

while x == True:
    i = input()
    if len(i) == 0:
        x = False
    else:
        a.append(int(i))

# Output

for j in a:
    classify(j)
        
    
    
