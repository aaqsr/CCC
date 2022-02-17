N = int(input())

fences = []

vals = list(map(int, input().split()))

pair = []

for n in range(len(vals)-1):
    fences.append([vals[n], vals[n+1]])

w = list(map(int, input().split()))

print(fences)

for n in range(N):
    fences[n].append(w[n])

A = 0
total = 0

for f in fences:
    total += (f[0] +f[1]) * f[2]

total = total / 2

newtotal = str(total)
if ".0" in newtotal:
    print(int(total))
else:
    print(total)
