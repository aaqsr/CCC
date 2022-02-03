# Take inputs

N = int(input())

streams = [] # Structure: original, left, right

for i in range(N):
    streams.append(int(input()))

x = 0
seq = []

while x != 77:
    x = int(input())
    seq.append(x)

# Algo

def split(arr, y, p): # streamnum, % flow split to left
    original = arr[y-1]
    left = original * (p/100)
    right = original - left

    arr.remove(original)
    arr.insert(y-1, left)
    arr.insert(y, right)

def join(arr, k): # streamnum to join to right
    old = arr[k-1]
    arr[k] += old
    arr.remove(old)


for j in range(0, len(seq)-1):
    r = seq[j]
    if r == 99:
        split(streams, seq[j+1], seq[j+2])
    elif r == 88:
        join(streams, seq[j+1])


# Output

line = ""

for s in streams:
    line = line + " " + str(round(s))

print(line)
