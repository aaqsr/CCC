# Problem 1

print("Perfect numbers: \n")

for i in range(1000, 9999):
    s = 0
    factors = []
    
    for g in range(1, i-1):
        if i % g == 0:
            factors.append(g)

    for n in factors:
        s += n

    if s == i:
        print(i)

# Problem 2

print("P2: \n")

for j in range(100, 999):
    s = 0

    for p in range(0, 2):
        s += int(str(j)[p]) ** 3

    if s == j:
        print(j)

#Crossword answers:

import math

for q in range(8000, 8990):
    root = math.sqrt(q)
    if int(root + 0.5) ** 2 == q:
        print(q, "is a perfect square")

#1 = 8128
#2 = 1113
#3 = 8100
#4 = 0110
#5 = 17
#6 = 370
    
