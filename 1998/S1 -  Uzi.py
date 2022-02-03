a = []

# Take Inputs
N = int(input())

for i in range(N):
    a.append(input())

for line in range(0, len(a)):
    d = []
    d.append(a[line].split(" "))
    for z in range(1, len(d[0])):
        if len(d[0][z]) == 4:
            d[0][z] = "****"
            
    print(" ".join(d[0]))
